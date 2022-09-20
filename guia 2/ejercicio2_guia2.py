"Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente."
"""entrada
____________________
numero1
numero2
____________________
proceso
____________________
resto = i % 2
____________________
salida
____________________
i
____________________"""
#declaracion de variables
resto=int
i=int
#inicio del programa
numero1=int(input("ingrese un numero: "))#ingreso numero1 por teclado
numero2=int(input("ingrese otro numero: "))#ingreso numero2 por teclado
#forma decendente
for i in range(numero1,numero2+1):#numeros comprendidos entre numero1 y numero2
    if(i%2!=0):#si el resto de i/2 es cero significa que es impar
       print(i)#imprimo numero impar
#fomra ascendente
for i in range (numero1, numero2, -1):
    resto = i % 2
    if resto != 0:
        print(i)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO       ENTRADA                     SALIDA
 **********************************************************************************************************
 *     1     *  ingrese un numero: 1      * 1                                                                                  
 *           *  ingrese otro numero: 15   * 3
 *           *                            * 5
 *           *                            * 7
 *           *                            * 9
 *           *                            * 11
 *           *                            * 13
 *           *                            * 15                                          
 * ********************************************************************************************************
 *"""
