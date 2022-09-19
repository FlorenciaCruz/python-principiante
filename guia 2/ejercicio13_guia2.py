"""Desarrollar un programa que permita procesar los datos del último censo de un apequeña población.
Por cada habitantes e ingresa:sexo(M/F)y edad. La carga de datos analiza al ingresar cualquier otro valor para sexo.
 El programa debe informar:
 Aqué sexo corresponde la mayor cantidad de habitantes(considerar que puede ser igual)
 Cantidad de mujeres en edad escolar(4 a 18 años inclusive)Si hay algún varón que supere los 80 años de edad.
 _____________________________________________________
 entrada
 _____________________________________________________
 sexo
 edad
 _____________________________________________________
 proceso
 _____________________________________________________
 contador_masculino
 contador_femenino
 mayor_habitantes
 mujeres_escolar
 varones_mayores
 _____________________________________________________
 salida
 _____________________________________________________
 mator_habitantes
 mujeres_escolar
 varones_mayores
 _____________________________________________________"""
contador_masculino=0
contador_femenino=0
edad=0
hombres_mayores=0
mujeres_escolar=0
mayor_habitantes=None
sexo = "M"

while (sexo == "M")or(sexo=="F"):
    sexo = str(input("Ingrese su sexo: "))
    edad=int(input("ingrese la edad: "))
    if(sexo=="M"):
        contador_masculino=contador_masculino+1
        if(edad>80):
            hombres_mayores=hombres_mayores+1
        
    if(sexo=="F"):
        contador_femenino=contador_femenino+1
        if(edad>4 and edad<=18):
            mujeres_escolar=mujeres_escolar+1

    if(bool(contador_masculino)==False):
        mayor_habitantes=contador_masculino
    if(bool(contador_femenino)==False):
        mayor_habitantes=contador_femenino

    if(contador_masculino>contador_femenino):
        mayor_habitantes=contador_masculino
        mensaje=("la mayor cantidad de habitantes corresponde a el sexo masculino:",mayor_habitantes)

    if(contador_masculino<contador_femenino):
        mayor_habitantes=contador_femenino
        mensaje=("la mayor cantidad de habitantes corresponde a el sexo femenino:",mayor_habitantes)
    if(contador_masculino==contador_femenino):
        mensaje=("la cantidad de habitantes son iguales")
print(mensaje)
print("mujeres en edad escolar:",mujeres_escolar)
print("hombres mayores de 80:",hombres_mayores)

