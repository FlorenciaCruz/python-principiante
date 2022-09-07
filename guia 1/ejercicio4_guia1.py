"División con resto. Plantear un algoritmo que permita informar, para dos valores a y b el resultado de la división a/b y el resto de esa división."
"""entrada
________________________________
a
b
________________________________
proceso
________________________________
a/b
a%b
________________________________
salida
division
resto_division
________________________________"""
"declaro las variables"
division=float
resto_division=float
"inicializo el programa"
a=float(input("ingrese el valor de a:"))
b=float(input("ingrese el valor de b:"))
division=(a/b);
resto_division=(a%b);
print("la division de los dos numeros es:",division)
print("el resto de la division de los dos numeros es: ",resto_division)
"""***********************************************************************************************
                            PRUEBA DE ESCRITORIO
 *************************************************************************************************
  INTENTO               ENTRADA                         SALIDA
 *************************************************************************************************
 *   1   *   ingrese el valor de a:  10 *   la diviaion de los dos numeros es:0.5                                                                                 
 *       *   ingrese el valor de b: 20  *   el resto de la division de los dos numeros es: 10.0                                     
 *       *                              *                    
 * **********************************************************************************************
 *"""