from .symbol_table import SymbolTable
from .errors import SemanticError
from gen.MarkovLangVisitor import MarkovLangVisitor

# Tabla de compatibilidad aritmética (vista en clases)
ARITH_COMPAT = {
    ('int', 'int'): 'int',
    ('int', 'float'): 'float',
    ('float', 'int'): 'float',
    ('float', 'float'): 'float',
}

class SemanticVisitor(MarkovLangVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []
        self.current_chain = None
        self.simulations = [] # Para el generador de código de bajo nivel
        self.seed = None

    def _error(self, msg, ctx):
        e = SemanticError(msg, ctx.start.line)
        self.errors.append(e)
        return 'error'

    # -- punto de entrada
    def visitProgram(self, ctx):
        for gc in ctx.globalConfig():
            self.visit(gc)
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.errors

    def visitSeedStmt(self, ctx):
        self.seed = int(ctx.INT_LIT().getText())

    # -- varDecl: var id : tipo ;
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        type_ = ctx.typeSpec().getText()
        line = ctx.start.line

        try:
            self.symtab.declare(name, type_, line)
        except SemanticError as e:
            self.errors.append(e)

    # -- assignment: id := expr ;
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        sym = self.symtab.lookup(name)

        if sym is None:
            self._error(f"Variable '{name}' no declarada", ctx)
            return
        sym.used = True

        expr_type = self.visit(ctx.expression())
        if expr_type == 'error':
            return

        ok = (
            sym.type_ == expr_type or
            (sym.type_ == 'float' and expr_type == 'int')
        )
        if not ok:
            self._error(f"No se puede asignar '{expr_type}' a '{sym.type_}'", ctx)
        else:
            sym.initialized = True

    # -- ifStmt
    def visitIfStmt(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool' and cond_type != 'error':
            self._error('Condición de if debe ser bool', ctx)

        for block in ctx.block():
            self.symtab.enter_scope(f'if_L{ctx.start.line}')
            self.visit(block)
            self.symtab.exit_scope()

    # -- whileStmt
    def visitWhileStmt(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool' and cond_type != 'error':
            self._error('Condición de while debe ser bool', ctx)

        self.symtab.enter_scope(f'while_L{ctx.start.line}')
        self.visit(ctx.block())
        self.symtab.exit_scope()

    # -- printStmt
    def visitPrintStmt(self, ctx):
        self.visit(ctx.expression())

    # -- block: { stmt* }
    def visitBlock(self, ctx):
        for stmt in ctx.statement():
            self.visit(stmt)

    # =========================================================
    # REGLAS DEL DOMINIO: CADENAS DE MARKOV
    # =========================================================

    def visitChainDecl(self, ctx):
        name = ctx.ID().getText()
        try:
            chain = self.symtab.declare_chain(name, ctx.start.line)
        except SemanticError as e:
            self.errors.append(e)
            return

        self.current_chain = chain
        self.symtab.enter_scope(f'chain_{name}')

        # 1. Visitar declaraciones de estados y transiciones
        for body in ctx.chainBody():
            self.visit(body)

        # 2. Validación Semántica de Dominio: Propiedad Estocástica
        # Para cada estado, la suma de probabilidades salientes debe ser 1.0
        for s in chain.states:
            prob_sum = 0.0
            has_transitions = False
            for target_s in chain.states:
                if (s, target_s) in chain.transitions:
                    prob_sum += chain.transitions[(s, target_s)]
                    has_transitions = True

            if has_transitions and abs(prob_sum - 1.0) > 1e-4:
                self._error(
                    f"Violación de propiedad estocástica en estado '{s}': las probabilidades salientes suman {round(prob_sum, 4)} (deben sumar exactamente 1.0)",
                    ctx
                )

        self.symtab.exit_scope()
        self.current_chain = None

    def visitStateDecl(self, ctx):
        state_name = ctx.ID().getText()
        if state_name in self.current_chain.states:
            self._error(f"Estado '{state_name}' ya declarado en la cadena '{self.current_chain.name}'", ctx)
            return
        self.current_chain.states.append(state_name)

    def visitTransitionStmt(self, ctx):
        from_state = ctx.ID(0).getText()
        to_state = ctx.ID(1).getText()

        if from_state not in self.current_chain.states:
            self._error(f"Estado de origen '{from_state}' no declarado en la cadena '{self.current_chain.name}'", ctx)
            return
        if to_state not in self.current_chain.states:
            self._error(f"Estado de destino '{to_state}' no declarado en la cadena '{self.current_chain.name}'", ctx)
            return

        # Evaluar tipo y valor de la probabilidad
        expr_type = self.visit(ctx.expression())
        if expr_type not in ('int', 'float'):
            self._error("La probabilidad de transición debe ser de tipo numérico (float)", ctx)
            return

        # Extraer valor constante si es posible
        try:
            prob_val = float(ctx.expression().getText())
            if prob_val < 0.0 or prob_val > 1.0:
                self._error(f"Probabilidad de transición {prob_val} fuera del rango [0.0, 1.0]", ctx)
                return
            self.current_chain.transitions[(from_state, to_state)] = prob_val
        except ValueError:
            self.current_chain.transitions[(from_state, to_state)] = 0.5

    def visitSimulateStmt(self, ctx):
        chain_name = ctx.ID(0).getText()
        start_state = ctx.ID(1).getText()

        if chain_name not in self.symtab.chains:
            self._error(f"Cadena de Markov '{chain_name}' no declarada", ctx)
            return

        chain = self.symtab.chains[chain_name]
        if start_state not in chain.states:
            self._error(f"Estado inicial '{start_state}' no pertenece a la cadena '{chain_name}'", ctx)
            return

        steps_type = self.visit(ctx.expression())
        if steps_type != 'int' and steps_type != 'error':
            self._error("La cantidad de pasos en 'simulate' debe ser de tipo int", ctx)
            return

        steps = 10
        try:
            steps = int(ctx.expression().getText())
        except ValueError:
            pass

        self.simulations.append({
            'type': 'simulate',
            'chain': chain,
            'start_state': start_state,
            'steps': steps
        })

    def visitStationaryStmt(self, ctx):
        chain_name = ctx.ID().getText()
        if chain_name not in self.symtab.chains:
            self._error(f"Cadena de Markov '{chain_name}' no declarada", ctx)
            return

        chain = self.symtab.chains[chain_name]
        self.simulations.append({
            'type': 'stationary',
            'chain': chain
        })

    # =========================================================
    # EXPRESIONES
    # =========================================================

    def visitRelationalExpr(self, ctx):
        if ctx.RELOP() is None:
            return self.visit(ctx.additiveExpr())

        t1 = self.visit(ctx.relationalExpr())
        t2 = self.visit(ctx.additiveExpr())
        if 'error' in (t1, t2):
            return 'error'

        # Control de tipos en comparaciones relacionales (Guía Semana 6)
        ok = (
            (t1 in ('int', 'float') and t2 in ('int', 'float')) or
            (t1 == t2)
        )
        if not ok:
            return self._error(f"Comparación relacional entre tipos incompatibles '{t1}' y '{t2}'", ctx)

        return 'bool'

    def visitAdditiveExpr(self, ctx):
        if ctx.ADDOP() is None:
            return self.visit(ctx.multiplicativeExpr())

        t1 = self.visit(ctx.additiveExpr())
        t2 = self.visit(ctx.multiplicativeExpr())
        if 'error' in (t1, t2):
            return 'error'

        op = ctx.ADDOP().getText()
        if op == '+' and t1 == 'string' and t2 == 'string':
            return 'string'

        result = ARITH_COMPAT.get((t1, t2))
        if result is None:
            return self._error(f"Operación '{t1} {op} {t2}' no válida", ctx)
        return result

    def visitMultiplicativeExpr(self, ctx):
        if ctx.MULOP() is None:
            return self.visit(ctx.factor())

        t1 = self.visit(ctx.multiplicativeExpr())
        t2 = self.visit(ctx.factor())
        if 'error' in (t1, t2):
            return 'error'

        op = ctx.MULOP().getText()

        # Validación de división por cero con constantes (Guía Semana 6)
        if op in ('/', 'DIV', 'MOD'):
            right_factor = ctx.factor()
            if right_factor.INT_LIT() and right_factor.INT_LIT().getText() == '0':
                return self._error("División por cero con constante", ctx)
            if right_factor.FLOAT_LIT() and float(right_factor.FLOAT_LIT().getText()) == 0.0:
                return self._error("División por cero con constante", ctx)

        result = ARITH_COMPAT.get((t1, t2))
        if result is None:
            return self._error(f"Operación '{t1} {op} {t2}' no válida", ctx)
        if op == '/':
            return 'float'
        return result

    def visitFactor(self, ctx):
        if ctx.INT_LIT():
            return 'int'
        if ctx.FLOAT_LIT():
            return 'float'
        if ctx.STRING_LIT():
            return 'string'
        if ctx.TRUE() or ctx.FALSE():
            return 'bool'
        if ctx.expression():
            return self.visit(ctx.expression())

        # Verifica si ID fue declarada e inicializada (Guía Semana 6)
        name = ctx.ID().getText()
        sym = self.symtab.lookup(name)
        if sym is None:
            return self._error(f"Variable '{name}' no declarada", ctx)
        if not sym.initialized:
            return self._error(f"Variable '{name}' usada sin haber sido inicializada", ctx)

        sym.used = True
        return sym.type_
