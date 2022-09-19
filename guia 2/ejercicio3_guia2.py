"""Sueldos y aguinaldo. Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:
a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.
b) Determinar en qué mes recibió el sueldo más bajo del período.
c) Informar el sueldo promedio del semestre."""
acumulador_sueldo=0
promedio=0
sueldo_minimo=int
sueldo_minimo=0
contador_minimo=int
contador_minimo=0
contador=int
contador=0
#aguinaldo=int
aguinaldo=float
mes_bajo=int
maximo=None
minimo=None
sueldo=int
i=int
for i in range(0,6):
    sueldo=int(input("ingrese el sueldo: "))
    print(bool(maximo))
    if(bool(maximo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        maximo=sueldo#toma el primer valor que tenga sueldo
    if(bool(minimo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        minimo=sueldo#toma el primer valor que tenga sueldo
        
    if(maximo<=sueldo):
        maximo=sueldo
        print(maximo)
        aguinaldo=maximo/2
        mes_alto=i
    
    if(minimo>=sueldo):
        minimo=sueldo
        sueldo_minimo=sueldo
        minimo=i

    acumulador_sueldo=acumulador_sueldo+sueldo
    promedio=acumulador_sueldo/6
print(aguinaldo)
print("el mes que recibio el sueldo mas bajo:",minimo)
print("el total del sueldo es:",acumulador_sueldo)
print("el promedio es:",promedio)


