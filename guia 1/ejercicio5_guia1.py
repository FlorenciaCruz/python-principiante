"""Cuadrado de un binomio. Plantear un script directamente en el shell de Python, que permita mostrar,
para dos valores 𝑎 y 𝑏, que: Un binomio al cuadrado (suma) es igual al cuadrado del primer término, más 
el doble producto del primero por el segundo más el cuadrado del segundo.
entrada
________________________________
a
b
________________________________
proceso
________________________________
primer_termino=a*a
segundo_termino=2*a*b
tercer_termino=b*b
cuadrado=primer_termino+segundo_termino+tercer_termino
________________________________
salida
cuadrado
________________________________"""
primer_termino=int
segundo_termino=int
tercer_termino=int
cuadrado=int
a=int(input("ingrese un numero entero: "))#ingreso del primer numero
b=int(input("ingrese otro numero entero: "))#ingreso del segundo numero
primer_termino=a*a;#formula del primer termino
segundo_termino=2*a*b;#formula del segundo termino
tercer_termino=b*b;#formula del tercer termino
cuadrado=primer_termino+segundo_termino+tercer_termino;#resultado del cuadrado
print("El cuadrado de un binomio de a: ",a,"y b: ",b,"es: ",cuadrado)#muestro por pantalla el resultado
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO        ENTRADA                                  SALIDA
 **********************************************************************************************************
 *     1     *   ingrese un numero entero: 2        *   El cuadrado de un binomio de a:  2 y b:  3 es:  25             *                                                                                                 
 *           *   ingrese otro numero entero: 3      *                    *                                             
 *           *                          *           *                                                 
 * ********************************************************************************************************
 *     2     *   ingrese un numero entero: 5        *  El cuadrado de un binomio de a:  5 y b:  8 es:  169          *                                                                                                    
 *           *   ingrese otro numero entero: 8      *                                                           
 *           *                                      *                                              
 *           *                                      *                                               
 * ********************************************************************************************************
 *"""
