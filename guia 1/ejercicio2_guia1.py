"2. Escribir un programa que pregunte un nombre de usuario, y que después muestre por pantalla si su cantidad de letras es par o impar."
"""entrada
________________________________
nombre
________________________________
proceso
________________________________
division
________________________________
salida
________________________________
nombre
caracteres
________________________________"""
"declaracion de variables"
caracteres=int
division=float
"inicializacion del programa"
nombre=(input("ingrese un nombre:"))
caracteres=(len(nombre))
division=caracteres%2;
if division == 0:
    print(nombre,"tiene",caracteres,"letras es par");
else:
    print(nombre,"tiene",caracteres,"letras es impar")

"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA       SALIDA
 **********************************************************************************************************
 *     1     *  pepito    *   pepito tiene 6 letras es par                                                                                                                    
 *           *            *                                                                      
 *           *            *                                                                        
 * ********************************************************************************************************
 *     2     *  sofia     *   sofia tiene  5 letras es impar                                                                                                                                    
 *           *            *                                                                        
 *           *            *                                                                                                                                                     
 * ********************************************************************************************************"""