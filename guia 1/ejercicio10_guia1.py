"""Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.
entrada
____________________________
numero
____________________________
proceso
____________________________
contador
suma
____________________________
salida
____________________________
suma
____________________________"""
"declaracion de variables"
numero=int
contador=int
primer_numero=int
segundo_numero=int
suma=int
"inicio del programa"
numero=int(input("ingrese un numero:"))#ingreso un numero por teclado
primer_numero=0#el primer numero empieza en 0
segundo_numero=1#el segundo numero empieza en 1
suma=0#suma se inicializa en 0
contador=1#contador se inicializa en 1
while(contador<=numero):#repite el bucle hasta que que el contador sea igual a el numero ingresado
    print(suma)#imprime la variable suma por pantalla
    contador=contador+1;#contador
    primer_numero=segundo_numero#asigno el valor del segundo_numero a primer_numero
    segundo_numero=suma#asigno suma a la variable segundo_numero
    suma=primer_numero+segundo_numero;#suma es la suma de el primer numero y el segundo numero
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO         
 **********************************************************************************************************
 *     1     *  ingrese un numero:4          *   0                                                                                     
 *           *                               *   1                        
 *           *                               *   1
 *           *                               *   2
 * ********************************************************************************************************
 *"""
