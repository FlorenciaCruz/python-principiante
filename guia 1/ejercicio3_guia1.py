"Escriba un programa que transforme todas las letras de una palabra en mayúsculas, minúsculas y la primera con minúsculas(capitalización)."
"""entrada
________________________________
palabra
________________________________
proceso
________________________________

________________________________
salida
palabra
________________________________"""
#ingreso de palabra
palabra=input("Ingrese una palabra:")
#muestra palabra en mayuscula
print(palabra,"en mayuscula: ",palabra.upper())
#muestra palabra en minuscula
print(palabra,"en minuscula: ",palabra.lower())
#muestra palabra con la primera letra en mayuscula
print(palabra,"con primera letra mayuscula es:",palabra.capitalize())
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA       SALIDA
 **********************************************************************************************************
 *     1     *  palabra   *  palabra en mayuscula: PALABRA                                                                                                                     
 *           *            *  palabra en minuscula: palabra                                                                       
 *           *            *  palabra con primera letra en mayuscula es: Palabra                                                                      
 * ********************************************************************************************************"""