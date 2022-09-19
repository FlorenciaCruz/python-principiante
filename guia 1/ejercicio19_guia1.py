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
#declaracion de variables
cuadro=0
contador=1
while(contador<=3):
    cuadro=int(input("ingrese el año del cuadro: "))
    if((cuadro>1901)and(cuadro<2000)):
        print("el cuadro es anterior al siglo 20")
    if (cuadro<1891):
        print("antiguedad menor a 10 años del sigo 20")   
    if(cuadro>2000):
        print("renovar stock")
    contador=contador+1

"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO       ENTRADA                                         SALIDA    
 **********************************************************************************************************
 *     1    *     ingrese el año del cuadro: 2022             *renovar stock
 *----------*-------------------------------------------------*-------------------------------------------      
 *          *     ingrese el año del cuadro: 1700             *antiguedad menor a 10 años del sigo 20
 *----------*-------------------------------------------------*-------------------------------------------                                                   
 *          *     ingrese el año del cuadro: 1980             *el cuadro es anterior al siglo 20 
 *----------*-------------------------------------------------*-------------------------------------------
 * ********************************************************************************************************                        
 *"""
