"17. Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo."
numero1=int
numero2=int
numero=int
suma=int
numero1=int(input("ingrese el numero1: "))#ingreso numero 1 por teclado
numero2=int(input("ingrese el numero2: "))#ingreso numero 2 por teclado
numero3=int(input("ingrese el numero3: "))#ingreso numero 3 por teclado
suma=numero1+numero2+numero3#suma de todos los numeros
print("la suma de todos los numeros es: ",suma)#imprimo los resultados
if(suma>10):#si la suma de todos los numeros es mayor a 10
    print("division:",round(suma/2))#divido por 2
else:
    print("potencia",suma*suma*suma)#elevo al cubo
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA                      SALIDA
 **********************************************************************************************************
 *     1     * ingrese el numero1: 2  *   la suma de todos los numeros es:  9                                        
 *           * ingrese el numero2: 4  *     potencia 729
 *           * ingrese el numero3: 3  *                                                                                                                    
 * ********************************************************************************************************
 *"""
