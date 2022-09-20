"""Ciclistas: La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
a) Determinar y mostrar el nombre del ganador de la carrera.
b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
c) Calcular y mostrar el tiempo promedio entre todos los ciclistas."""

"""entrada
__________________________
numero_competidores
__________________________
proceso
__________________________
nombre
tiempo_carrera
__________________________
salida
__________________________
nombre_ganador
tiempo_record
tiempo promedio
__________________________"""
#declaracion de variables
numero_competidores=int
numero_competidores=1
contador=int
contador=1
nombre=int
tiempo_record=float
tiempo_recod=0
nombre_maximo=int
nombre_minimo=int
acumulador=int
acumulador=0
maximo=float
minimo=float
maximo=None
minimo=None
tiempo_carrera=float
nombre_ganador=float
tiempo_record=float
tiempo_promedio=float

#inicio del programa
numero_competidores=int(input("ingrese el numero de competidores: "))#ingreso los competidores por teclado
while(contador<=numero_competidores):#se termina el bucle hasta la cantidad de competidores ingresados
    nombre=(input("ingrese el nombre: "))#ingreso nombre del competidor
    tiempo_carrera=int(input("tiempo de carrera: "))#ingreso el tiempo del competidor
    if(bool(maximo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        maximo=tiempo_carrera#toma el primer valor que tenga sueldo
    if(bool(minimo)==False):#compruebo si la variable esta vacia(false si no tiene nada)
        minimo=tiempo_carrera#toma el primer valor que tenga sueldo
    if(minimo>tiempo_carrera):
        minimo=tiempo_carrera;
        nombre_minimo=nombre#guardo el nombre del que hizo menos tiempo
    acumulador=acumulador+tiempo_carrera;
    contador=contador+1;#contador del bucle
#imprimo los resultados por pantalla
print("el ganador de la carrera es:", nombre_minimo)
tiempo_record=int(input("ingrese el tiempo record: "))
#si el tiempo minino de la carrera es mayor al tiempo record, se imprime solo el promedio
if(minimo>tiempo_record):
    tiempo_promedio=acumulador/numero_competidores;
    print("el promedio entre todos los cicistas es de: ",tiempo_promedio)
#si el tiempo minimo es menor al tiempo record, se establece un nuevo tiempo record y imprimo los resultados    
if(minimo<tiempo_record):
    print("el tiempo de la carrera es menor al tiempo recod")
    print("el nuevo record es de",nombre_minimo,"con",minimo,"tiempo")    
    tiempo_promedio=acumulador/numero_competidores;
    print("el promedio entre todos los cicistas es de: ",tiempo_promedio)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO       ENTRADA                                 SALIDA  
 **********************************************************************************************************
 *     1     *   ingrese el numero de competidores: 2 * el nuevo record es de romina con 2 tiempo
 *           *   ingrese el nombre: sofia             * el promedio entre todos los cicistas es de:  3.0
 *           *   tiempo de carrera: 4                 *
 *           *   ingrese el nombre: romina            *
 *           *   tiempo de carrera: 2                 *
 *           *   ingrese el tiempo record: 3          *                                                                  
 *           *                                        *
 *           *                                        *     
 * ********************************************************************************************************
 *     2     *  ingrese el numero de competidores: 2  *  el ganador de la carrera es: romina
 *           *    ingrese el nombre: sofia            *  el promedio entre todos los cicistas es de:  5.0
 *           *    tiempo de carrera: 8                *
 *           *    ingrese el nombre: romina           *
 *           *    tiempo de carrera: 2                *               
 *           *    ingrese el tiempo record: 1         *

 *"""



