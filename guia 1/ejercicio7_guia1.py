"""7. Últimos dígitos ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por teclado, y muestre
el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado).
entrada
________________________________
numero
________________________________
proceso
________________________________
ultimo=numero%10
ante_ultimo=numero//10
________________________________
salida
ultimo
ante_ultimo
________________________________"""

"declaracion de variables"
numero=int
ultimo=int
ante_ultimo=int
"inicializacion del programa"
numero=int(input("ingrese un numero entero: "))#ingreso de numero entero
ultimo=numero%10;#el ultimo numero es el resto de numero/10
ante_ultimo=(numero/10)%10;#el anteultimo numero es el resto de ultimo/10
print("el ultimo numero es: ",ultimo)#muestro por pantalla el ultimo numero
print("los ultimos dos digitos es: ",round(ante_ultimo),ultimo)#muestro por pantalla el anteultimo numero
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO     ENTRADA      SALIDA  
 **********************************************************************************************************
 *     1     * ingrese un numero entero: 34         * el ultimo numero es:  4                                                                                              
 *           *                                      * los ultimos dos digitos es:  3 4                                                                                 
 * ********************************************************************************************************
 *     2     * ingrese un numero entero: 245        *  el ultimo numero es:  5                                                                                                   
 *           *                                      *   los ultimos dos digitos es:  4 5                                                                                                   
 * ********************************************************************************************************
 *"""