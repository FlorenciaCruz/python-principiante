"""Ahorros. Escribir un programa en el cual muestre a fin de año el total de ahorro obtenido, si se pide en cada mes el 10% del sueldo ganado."
entrada
______________________________
sueldo
______________________________
proceso
______________________________
porcentaje
total_ahorros
______________________________
salida
______________________________
porcentaje
total_ahorros+
______________________________"""
"declaracion de variables"
contador=1
sueldo=int
acumulador=0.0
porcentaje=float
porcentaje=0.0
meses=int
meses=12
print("AHORRO COMENZADO EN ENERO DEL AÑO 2022")
print("su sueldo es de ",sueldo,"pesos")
sueldo=int(input("ingrese su sueldo: "))
while(contador<=12):
  porcentaje=((sueldo)*10/100)
  acumulador=acumulador+porcentaje
  print("mes",contador,"tiene un ahorro de",acumulador)
  contador=contador+1
