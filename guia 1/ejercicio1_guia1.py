"1. Desarrolle un programa que pase un peso de kilogramo a libras teniendo en cuenta que cada kilogramo equivale a 2.2 libras."
"""entrada
_______________________________
kilogramos
_______________________________
proceso
_______________________________
operacion=kilogramos*2.2
_______________________________
salida
_______________________________
kilogramos
operacion
_______________________________"""
"declaracion de variables"
operacion=float
"inicializacion del programa"
Kilogramos=float(input("Escriba un peso en Kilogramos:"))
operacion=Kilogramos*2.2;
print("El peso ingresado de",Kilogramos,"es de:",operacion,"libras")
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      kilogramos   OPERACION
 **********************************************************************************************************
 *     1     *     34     *    74.8000000000000001 *                                                                                          
 *           *            *                        *                                            
 *           *            *                        *                                                
 * ********************************************************************************************************
 *     2     *      39    *   85.80000000000000001  *                                                                                                                      
 *           *            *                         *                                               
 *           *            *                         *                                     
 *           *            *                         *                                      
 * ********************************************************************************************************
 *"""