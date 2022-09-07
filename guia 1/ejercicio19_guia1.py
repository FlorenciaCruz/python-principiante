"""Galería de Arte. Una galería de arte desea preparar un catálogo
de sus cuadros más famosos. Se realiza
una prueba con tres cuadros y por cada
uno se ingresa el año en que fue creado
. El programa deberá verificar si todos
los cuadros son anteriores al siglo XX
(El siglo XX es el siglo pasado. Se inició
 en el año 1901 y terminó en el año 2000).
Determinar cuántos tienen antigüedad inferior
a 10 años. Si no hay ninguno, imprimir el mensaje “Renovar stock”."""

cuadro1=int
cuadro2=int
cuadro3=int
cuadro1=int(input("ingrese el cuadro 1:"))
cuadro2=int(input("ingrese el cuadro 2:"))
cuadro3=int(input("ingrese el cuadro 3:"))
if((cuadro1<2000)or(cuadro1>1901))or((cuadro2<2000)or(cuadro>1901))or((cuadro3<2000)or(cuadro3>2000)):
    print("el cuadro es anteior al siglo 20")
if ((cuadro1<1891)or(cuadro2<1891)or(cuadro3<1891)):
    print("antiguedad menor a 10 años del sigo 20")
else:
    print("renovar stock")
