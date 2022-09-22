"""Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero)."
entrada
____________________________
numeros
____________________________
proceso
____________________________
acumulador_numeros=acumulador_numeros+numeros
contador_numeros=contador_numeros+1
promedio=acumulador_numeros/contador_numeros
____________________________
salida
____________________________
promedio
contador_numeros
____________________________"""
#declaracion de variables
promedio=int
acumulador_numeros=int
acumulador_numeros=0
contador_numeros=int
contador_numeros=-1
numeros=int
numeros=1
#inicio del programa
while(numeros!=0):#termina el bucle cuando el usuario ingresa 0
    numeros=int(input("ingrese un numero: "))#ingreso numeros por teclado
    acumulador_numeros=acumulador_numeros+numeros#acumulador de numeros
    contador_numeros=contador_numeros+1#contador de numeros ingresados
    
promedio=acumulador_numeros/contador_numeros#promedio de los numeros ingresados
#imprimo los resultados por pantalla
print("el promedio de los numeros es:",promedio)
print("la cantidad de numeros ingresados es de: ",contador_numeros)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA                    SALIDA   
 **********************************************************************************************************
 *     1     *    ingrese un numero: 2   *  el promedio de los numeros es: 8.25                                           
 *           *    ingrese un numero: 10  *  la cantidad de numeros ingresados es de:  4
 *           *    ingrese un numero: 20  *
 *           *    ingrese un numero: 1   *
 *           *    ingrese un numero: 0   *                                                                                        
 *           *                           *                  
 *           *                           *                 
 * ********************************************************************************************************
 *"""
