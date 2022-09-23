"""Complejo de cines Desarrollar un programa que permita procesar funciones de un complejo de cines.
Por cada función se conoce:cantidad de espectadores y descuento(S/N).La carga termina cuando la cantidad de espectadores sea igual a 0(cero).
El programa deberá:Calcular la recaudación total del complejo,considerando que el valor de la entrada es de $50 en los días con descuento
y $75 en los días sin descuento.Determinar cuántas funciones con descuentos efectuaron y qué porcentaje representan sobre el total de funciones"""
"""entrada
____________________
cantidad de espectadores
descuento
____________________
proceso
____________________
recaudacion_total
funciones_decuento
porcentaje_funciones
entrada_descuento
entrada_sin_descuento
____________________
salida
____________________
recaudacion_total
funciones_descuento
porcentaje_funciones
____________________"""
#declaracion de variables
entrada_decuento=int
acumulador_descuento=int
acumulador_descuento=0
contador_descuento=int
contador_descuento=0
entrada_sin_descuento=int
acumulador_sin_descuento=int
acumulador_sin_descuento=0
contador=int
contador=0
total_funciones=int
porcentaje_funciones=int
cantidad_espectadores=int
cantidad_espectadores=-1
#inicio del programa
cantidad_espectadores=int(input("ingrese la cantidad de espectadores: "))#ingreso cantidad de espectadores por teclado
while(cantidad_espectadores!=0):#repite el bucle hasta que ingrese 0 en cantidad de espectadores    
    descuento=(input("¿agrega descuento?"))#ingreso descuento
    if(descuento=='S') or (descuento=='s'):#si el descuento es S o s tiene descuento
        print("tiene descuento")
        entrada_descuento=cantidad_espectadores*50#precio de entrada con descuento
        acumulador_descuento=acumulador_descuento+entrada_descuento#acumulador de entradas con descuento
        contador_descuento=contador_descuento+1#contador de entradas con descuento
    if(descuento=='N') or (descuento=='n'):#si el descuento es N o n no tiene descuento
        print("no tiene descuento")
        entrada_sin_descuento=cantidad_espectadores*75#precio sin descuento
        acumulador_sin_descuento=acumulador_sin_descuento+entrada_sin_descuento#acumulador de entradas sin descuento
    contador=contador+1#contador del bucle
    cantidad_espectadores=int(input("ingrese la cantidad de espectadores: "))
total_funciones=acumulador_descuento+acumulador_sin_descuento#total de funciones con descuento y sin descuento
porcentaje_funciones=((contador_descuento*100)/contador)#calculo porcentaje de las funciones
#imprimo resultados
print("la recaudacion total es de:",total_funciones)
print("funciones con descuento: ",contador_descuento)
print("promedio del total de funciones:",porcentaje_funciones)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA                                  SALIDA   
 **********************************************************************************************************
 *     1     *  ingrese la cantidad de espectadores:1  *  tiene descuento
 *           *    ¿agrega descuento?s                  *
 *           *                                         *
 *           *    ingrese la cantidad de espectadores:1*  no tiene descuento
 *           *    ¿agrega descuento?n                  *
 *           *                                         * 
 *           *    ingrese la cantidad de espectadores:1*  tiene descuento
 *           *    ¿agrega descuento?s                  *
 *           *                                         *
 *           *    ingrese la cantidad de espectadores:1*  no tiene descuento
 *           *    ¿agrega descuento?n                  *
 *           *                                         *
 *           *                                         *      ingrese la cantidad de espectadores: 0
 *           *                                         *      la recaudacion total es de: 250
 *           *                                         *      funciones con descuento:  2
 *                                                     *      promedio del total de funciones: 50.0                                                                                             
 *           *                                         *     
 *           *                                         *        
 * ********************************************************************************************************
 *"""
