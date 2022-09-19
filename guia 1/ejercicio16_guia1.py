"""Se desea un programa que:
solicite al usuario un nombre,un apellido y el dominio y luego,proponga una dirección de mail para el nombre
y apellido ingresado de acuerdo a las siguientes reglas: Componer la dirección de
correo de la siguiente manera: @ Por ejemplo para Nombre = Felipe, Apellido= Steffolani
y Dominio= umet.edu.ar la dirección de mail sería: fsteffolani@umet.edu.ar. Pero si la
primera primera letra del nombre y la primera letra del apellido son la misma entonces
uƟlizar:.@ Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar
la dirección de mail sería: soledad.steffolani@umet.edu.ar

entrada
_____________________
nombre
apellido
dominio
mail
_____________________
proceso
_____________________
_____________________
salida
_____________________"""
#declara las variables
nombre=""
apellido=""
dominio=""
#inicio el programa
nombre=(input("ingrese su nombre: "))#ingreso nombre por teclado
apellido=(input("ingrese su apellido: "))#ingreso apellido por teclado
dominio=(input("ingrese su dominio: "))#ingreso dominio por teclado
if nombre[0]==apellido[0]:#si la primera letra de nombre es igual a la primera letra de apellido entonces
    print(nombre+"."+apellido+"@"+dominio)#se separa nombre y apellido con un punto
else:
    print(nombre+apellido+"@"+dominio)#se escribe nombre al lado de apellido
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO   ENTRADA                                 SALIDA         
 **********************************************************************************************************
 *   1   *  ingrese su nombre: Felipe            *   FelipeSteffolani@umet.edu.ar
 *       *    ingrese su apellido: Steffolani    *
 *       *    ingrese su dominio: umet.edu.ar    *                              
 * ********************************************************************************************************
 *"""
