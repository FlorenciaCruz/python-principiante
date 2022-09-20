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
aguinaldo=float
mes_bajo=int
maximo=None
minimo=None
sueldo=int
i=int
for i in range(1,7):
    sueldo=int(input("ingrese el sueldo: "))
    if(bool(maximo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        maximo=sueldo#toma el primer valor que tenga sueldo
    if(bool(minimo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        minimo=sueldo#toma el primer valor que tenga sueldo
    #maximo sueldo    
    if(maximo<=sueldo):
        maximo=sueldo
        aguinaldo=maximo/2#el aguinaldo es la mitad del sueldo mas alto del periodo
        mes_alto=i
    #minimo sueldo
    if(minimo>=sueldo):
        minimo=sueldo
        sueldo_minimo=sueldo
        #mes que recibio el sueldo mas bajo
        mes_bajo=i

    acumulador_sueldo=acumulador_sueldo+sueldo#acumulador de todos los sueldos igresados
    promedio=acumulador_sueldo/6#promedio de los sueldos
#imprimo resultados
print("aguinaldo: ",aguinaldo)
print("el mes que recibio el sueldo mas bajo:",mes_bajo)
print("el total del sueldo es:",acumulador_sueldo)
print("el promedio es:",promedio)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO       ENTRADA                         SALIDA  
 **********************************************************************************************************
 *     1     * ingrese el sueldo: 1000    *      aguinaldo:  3000.0                                                                                 
 *           * ingrese el sueldo: 2000    *      el mes que recibio el sueldo mas bajo: 1                                   
 *           * ingrese el sueldo: 3000    *      el total del sueldo es: 21000
 *           * ingrese el sueldo: 4000    *      el promedio es: 3500.0
 *           * ingrese el sueldo: 5000    *
 *           * ingrese el sueldo: 6000    *                            
 * ********************************************************************************************************                                                                                               
 *"""
