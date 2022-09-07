"""6. Área de un triángulo.Desarrolle un programa para calcularel área de un triángulo,
cargando por teclado el valor de la base, pero sabiendo que su altura es igual al cuadrado de la base.
entrada
________________________________
base
________________________________
proceso
________________________________
altura=base*base
area=(base*altura)/2
________________________________
salida
area
________________________________"""
"declaracion de variables"
altura=float
area=float
"inicializacion del programa"
base=int(input("ingrese la base del triangulo:"))#ingreso por teclado la base del triangulo
altura=base*base;#formula de base al cuadrado
area=(base*altura)/2;#formula del area
print("el area del triangulo con base: ",base,", es de,",area)#imprimo por pantalla los resultados
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO       ENTRADA     SALIDA 
 **********************************************************************************************************
 *     1     *  ingrese la base del triangulo:2          *  el area del triangulo con base:  2 , es de, 4.0                                                                                              
                                                                        
 * ********************************************************************************************************
 *     2     *   ingrese la base del triangulo:8         *   el area del triangulo con base:  8 , es de, 256.0                                                                                                   
                                                   
 * ********************************************************************************************************
 *"""
