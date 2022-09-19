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
#declaracion de variables
contador=1
sueldo=int
acumulador=0.0
porcentaje=float
porcentaje=0.0
meses=int
meses=12
#inicio del programa
print("AHORRO COMENZADO EN ENERO DEL AÑO 2022")
sueldo=int(input("ingrese su sueldo: "))#ingreso sueldo por teclado
while(contador<=12):#repite el bucle hasta 12 que son los meses del año suponiendo que empieza en enero
  porcentaje=((sueldo)*10/100)#calculo el porcentaje del 10%
  acumulador=acumulador+porcentaje#acumulo el porcentaje
  print("mes",contador,"tiene un ahorro de",acumulador)#imprimo los resultados
  contador=contador+1#contador
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO    ENTRADA                    SALIDA  
 **********************************************************************************************************
 *     1    * ingrese su sueldo: 100  *  mes 1 tiene un ahorro de 10.0
 *          *                         *    mes 2 tiene un ahorro de 20.0
 *          *                         *    mes 3 tiene un ahorro de 30.0
 *          *                         *    mes 4 tiene un ahorro de 40.0
 *          *                         *    mes 5 tiene un ahorro de 50.0
 *          *                         *    mes 6 tiene un ahorro de 60.0
 *          *                         *    mes 7 tiene un ahorro de 70.0
 *          *                         *    mes 8 tiene un ahorro de 80.0
 *          *                         *    mes 9 tiene un ahorro de 90.0
 *          *                         *    mes 10 tiene un ahorro de 100.0
 *          *                         *    mes 11 tiene un ahorro de 110.0
 *          *                         *    mes 12 tiene un ahorro de 120.0                                                                                                            
 * ********************************************************************************************************
 *"""
