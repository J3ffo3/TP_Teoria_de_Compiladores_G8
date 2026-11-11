from __future__ import annotations
from llvmlite import ir
import ast_voltio as A
from errores import ErrorCompilacion

I1 = ir.IntType(1)
I8 = ir.IntType(8)
I32 = ir.IntType(32)
I64 = ir.IntType(64)
F64 = ir.DoubleType()
I8P = I8.as_pointer()
VOID = ir.VoidType()

class GeneradorLLVM:
    def __init__(self, nombre_modulo: str = "voltio"):
        self.modulo = ir.Module(name=nombre_modulo)
        self.variables = {}
        self.cadenas = {}
        self._declarar_printf()

    def _declarar_printf(self):
        func_type = ir.FunctionType(I32, [I8P], var_arg=True)
        self.printf = ir.Function(self.modulo, func_type, name="printf")

    def _cadena(self, texto: str):
        if texto not in self.cadenas:
            datos = bytearray(texto.encode("utf-8")) + b"\x00"
            tipo = ir.ArrayType(I8, len(datos))
            g = ir.GlobalVariable(self.modulo, tipo, name=f".str.{len(self.cadenas)}")
            g.global_constant = True
            g.linkage = "private"
            g.initializer = ir.Constant(tipo, datos)
            self.cadenas[texto] = g
        return self.b.bitcast(self.cadenas[texto], I8P)

    def generar(self, programa: A.Programa) -> ir.Module:
        main_type = ir.FunctionType(I32, [])
        self.fn = ir.Function(self.modulo, main_type, name="main")
        self.bloque_entrada = self.fn.append_basic_block("entrada")
        cuerpo = self.fn.append_basic_block("inicio")
        
        self.b = ir.IRBuilder(cuerpo)
        self.b_alloca = ir.IRBuilder(self.bloque_entrada)

        for s in programa.sentencias:
            self._sentencia(s)

        self.b.ret(ir.Constant(I32, 0))
        self.b_alloca.branch(cuerpo)
        return self.modulo

    def _tipo_llvm(self, tipo: A.Tipo):
        if tipo.nombre == "entero":
            return I64
        if tipo.nombre in ("decimal", "porcentaje") or tipo.es_dominio:
            return F64
        if tipo.nombre == "booleano":
            return I1
        return I8P

    def _sentencia(self, s):
        metodo = getattr(self, "_s_" + type(s).__name__, None)
        if metodo:
            metodo(s)

    def _s_Declaracion(self, d: A.Declaracion):
        t_llvm = self._tipo_llvm(d.tipo_decl)
        ptr = self.b_alloca.alloca(t_llvm, name=d.nombre)
        self.variables[id(d.simbolo)] = ptr
        if d.valor is not None:
            val = self._expr(d.valor)
            if t_llvm == F64 and val.type == I64:
                val = self.b.sitofp(val, F64)
            self.b.store(val, ptr)

    def _s_Asignacion(self, a: A.Asignacion):
        ptr = self.variables[id(a.simbolo)]
        val = self._expr(a.valor)
        if ptr.type.pointee == F64 and val.type == I64:
            val = self.b.sitofp(val, F64)
        self.b.store(val, ptr)

    def _s_Si(self, s: A.Si):
        fin_bb = self.fn.append_basic_block("si.fin")
        for i, (cond, bloque) in enumerate(s.ramas):
            entonces_bb = self.fn.append_basic_block(f"si.entonces{i}")
            siguiente_bb = self.fn.append_basic_block(f"si.sig{i}")
            cond_val = self._expr(cond)
            self.b.cbranch(cond_val, entonces_bb, siguiente_bb)
            
            self.b.position_at_end(entonces_bb)
            for st in bloque.sentencias:
                self._sentencia(st)
            if not self.b.block.is_terminated:
                self.b.branch(fin_bb)
            
            self.b.position_at_end(siguiente_bb)

        if s.sino:
            for st in s.sino.sentencias:
                self._sentencia(st)
        if not self.b.block.is_terminated:
            self.b.branch(fin_bb)
        self.b.position_at_end(fin_bb)

    def _s_Mientras(self, m: A.Mientras):
        cond_bb = self.fn.append_basic_block("mientras.cond")
        cuerpo_bb = self.fn.append_basic_block("mientras.cuerpo")
        fin_bb = self.fn.append_basic_block("mientras.fin")
        
        self.b.branch(cond_bb)
        self.b.position_at_end(cond_bb)
        cond_val = self._expr(m.condicion)
        self.b.cbranch(cond_val, cuerpo_bb, fin_bb)
        
        self.b.position_at_end(cuerpo_bb)
        for st in m.cuerpo.sentencias:
            self._sentencia(st)
        if not self.b.block.is_terminated:
            self.b.branch(cond_bb)
        self.b.position_at_end(fin_bb)

    def _s_Mostrar(self, m: A.Mostrar):
        fmt = []
        args_val = []
        for a in m.args:
            val = self._expr(a)
            if a.tipo.nombre == "texto":
                fmt.append("%s")
                args_val.append(val)
            elif a.tipo.nombre == "entero":
                fmt.append("%lld")
                args_val.append(val)
            elif a.tipo.nombre == "booleano":
                fmt.append("%s")
                str_v = self.b.select(val, self._cadena("verdadero"), self._cadena("falso"))
                args_val.append(str_v)
            else: # float / dominio
                fmt.append("%.2f")
                args_val.append(val)
        
        fmt_str = " ".join(fmt) + "\n"
        ptr_fmt = self._cadena(fmt_str)
        self.b.call(self.printf, [ptr_fmt] + args_val)

    def _expr(self, e: A.Expr):
        metodo = getattr(self, "_e_" + type(e).__name__, None)
        return metodo(e) if metodo else None

    def _e_Literal(self, e: A.Literal):
        if e.clase == "entero":
            return ir.Constant(I64, e.valor)
        if e.clase in ("decimal", "dominio"):
            return ir.Constant(F64, float(e.valor))
        if e.clase == "porcentaje":
            return ir.Constant(F64, float(e.valor) / 100.0)
        if e.clase == "booleano":
            return ir.Constant(I1, int(e.valor))
        return self._cadena(e.valor)

    def _e_Variable(self, e: A.Variable):
        ptr = self.variables[id(e.simbolo)]
        return self.b.load(ptr, name=e.nombre)

    def _e_Binaria(self, e: A.Binaria):
        izq = self._expr(e.izq)
        der = self._expr(e.der)
        
        # Coercion automatica si uno es float y otro int
        if izq.type == I64 and der.type == F64:
            izq = self.b.sitofp(izq, F64)
        elif izq.type == F64 and der.type == I64:
            der = self.b.sitofp(der, F64)

        es_flotante = (izq.type == F64)

        if e.op == "+":
            return self.b.fadd(izq, der, name="sum") if es_flotante else self.b.add(izq, der, name="sum")
        if e.op == "-":
            return self.b.fsub(izq, der, name="sub") if es_flotante else self.b.sub(izq, der, name="sub")
        if e.op == "*":
            return self.b.fmul(izq, der, name="mul") if es_flotante else self.b.mul(izq, der, name="mul")
        if e.op == "/":
            if not es_flotante:
                izq = self.b.sitofp(izq, F64)
                der = self.b.sitofp(der, F64)
            return self.b.fdiv(izq, der, name="div")

        # Comparaciones
        if e.op in ("<", "<=", ">", ">=", "==", "!="):
            if es_flotante:
                return self.b.fcmp_ordered(e.op, izq, der, name="cmp")
            return self.b.icmp_signed(e.op, izq, der, name="cmp")

        if e.op == "y":
            return self.b.and_(izq, der, name="and")
        if e.op == "o":
            return self.b.or_(izq, der, name="or")
        return izq

    def _e_Unaria(self, e: A.Unaria):
        val = self._expr(e.expr)
        if e.op == "no":
            return self.b.not_(val, name="not")
        if e.op == "-":
            return self.b.fneg(val, name="neg") if val.type == F64 else self.b.neg(val, name="neg")
        return val
