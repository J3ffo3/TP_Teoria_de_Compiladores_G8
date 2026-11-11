; ModuleID = "voltio"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entrada:
  %"tensionRed" = alloca double
  %"cargaResistiva" = alloca double
  %"cargaIluminacion" = alloca double
  %"potenciaTotal" = alloca double
  %"corrienteLinea" = alloca double
  br label %"inicio"
inicio:
  store double 0x406b800000000000, double* %"tensionRed"
  store double 0x40b1300000000000, double* %"cargaResistiva"
  store double 0x4091300000000000, double* %"cargaIluminacion"
  %"cargaResistiva.1" = load double, double* %"cargaResistiva"
  %"cargaIluminacion.1" = load double, double* %"cargaIluminacion"
  %"sum" = fadd double %"cargaResistiva.1", %"cargaIluminacion.1"
  store double %"sum", double* %"potenciaTotal"
  %"potenciaTotal.1" = load double, double* %"potenciaTotal"
  %"tensionRed.1" = load double, double* %"tensionRed"
  %"div" = fdiv double %"potenciaTotal.1", %"tensionRed.1"
  store double %"div", double* %"corrienteLinea"
  %"corrienteLinea.1" = load double, double* %"corrienteLinea"
  %"cmp" = fcmp ogt double %"corrienteLinea.1", 0x4040000000000000
  br i1 %"cmp", label %"si.entonces0", label %"si.sig0"
si.fin:
  ret i32 0
si.entonces0:
  %".8" = bitcast [44 x i8]* @".str.0" to i8*
  %".9" = bitcast [4 x i8]* @".str.1" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i8* %".8")
  br label %"si.fin"
si.sig0:
  %".12" = bitcast [21 x i8]* @".str.2" to i8*
  %"corrienteLinea.2" = load double, double* %"corrienteLinea"
  %".13" = bitcast [9 x i8]* @".str.3" to i8*
  %".14" = call i32 (i8*, ...) @"printf"(i8* %".13", i8* %".12", double %"corrienteLinea.2")
  br label %"si.fin"
}

@".str.0" = private constant [44 x i8] c"Alerta: Sobrecarga en alimentador principal\00"
@".str.1" = private constant [4 x i8] c"%s\0a\00"
@".str.2" = private constant [21 x i8] c"Corriente de diseno:\00"
@".str.3" = private constant [9 x i8] c"%s %.2f\0a\00"