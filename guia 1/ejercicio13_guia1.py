""Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.
entrada
________________
pesos
________________
proceso
________________
pesos_conversion=(pesos/295)
dolares_conversion
________________
salida
________________
pesos
conversion
________________"""
conversion=float
valor_pesos=float
dolares_conversion=float
#ingreso de valores
valor_pesos=float(input("ingrese el valor de 1 dolar: "))#ingreso el valor del dolar
pesos=valor_pesos
#conversion de dolar a peso
dolares=float(input("ingrese la cantidad de dolares a convertir a pesos: "))#ingreso la cantidad de dolares
dolares_conversion=(dolares*pesos)#conversion de dolares a pesos
print("dolares:",dolares,"son",round(dolares_conversion),"pesos")#imprimo resultados por pantalla
#conversion de pesos a dolar
pesos=float(input("ingrese la cantidad de pesos a convertir a dolar: "))#ingreso la cantidad de pesos a dolar
pesos_conversion=(pesos/valor_pesos)#conversion de pesos a dolares
print("pesos:",pesos,"son",round(pesos_conversion),"dolares")#imprimo resultados por pantalla
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO   ENTRADA                                                     SALIDA      
 **********************************************************************************************************
 *  1   *   ingrese el valor de 1 dolar: 295                         *   dolares: 1.0 son 295 pesos
 *      *   ingrese la cantidad de dolares a convertir a pesos: 1    *  pesos: 295.0 son 1 dolares
 *      *   ingrese la cantidad de pesos a convertir a dolar: 295    *             
 *      *                                                            *
 * ********************************************************************************************************
                          
 * ********************************************************************************************************
 *"""
