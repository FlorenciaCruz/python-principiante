"""Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.
entrada
___________________
numero
___________________
proceso
___________________
contador=contador+1
tabla=contador*numero
___________________
salida
___________________
contador
numero
tabla
___________________"""
"declaracion de variables"
contador=int#clase entero
contador=0#inicializo en 0
"inicializacion del programa"
numero=(int(input("ingrese un numero y se mostrata su tabla de multiplicar hasta el 10: ")))#ingreso numero por teclado
while(contador<=9):#se repite el bucle hasta que contador sea 9
    contador=contador+1;#contador
    tabla=contador*numero;#es el contador por el numero ingresado anteriormente, de esta manera muestra la tabla del 1 al 10
    print(contador,"x",numero,"=",tabla)#muestro la tabla por pantalla
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO         ENTRADA                                                                   SALIDA
 **********************************************************************************************************
 *     1         *  ingrese un numero y se mostrata su tabla de multiplicar hasta el 10: 1*        
 *               *                                                                        *  1 x 1 = 1
 *               *                                                                        *  2 x 1 = 2
 *               *                                                                        *  3 x 1 = 3
 *               *                                                                        *  4 x 1 = 4
 *               *                                                                        *  5 x 1 = 5
 *               *                                                                        *  6 x 1 = 6
 *               *                                                                        *  7 x 1 = 7
 *               *                                                                        *  8 x 1 = 8
 *               *                                                                        *  9 x 1 = 9
 *               *                                                                        *  10 x 1 = 10                                                                                        
 *               *                                                                        *
 *               *                                                                        *
 * ********************************************************************************************************
 *"""
