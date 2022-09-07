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
nombre=""
apellido=""
dominio=""
nombre=(input("ingrese su nombre: "))
apellido=(input("ingrese su apellido: "))
dominio=(input("ingrese su dominio: "))
if nombre[0]==apellido[0]:
    print(nombre+"."+apellido+"@"+dominio)
else:
    print(nombre+apellido+"@"+dominio)
