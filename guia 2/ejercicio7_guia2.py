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
while(cantidad_espectadores!=0):
    cantidad_espectadores=int(input("ingrese la cantidad de spectadores: "))
    descuento=(input("¿agrega descuento?"))
    if(descuento=='S') or (descuento=='s'):
        print("tiene descuento")
        entrada_descuento=cantidad_espectadores*50
        acumulador_descuento=acumulador_descuento+entrada_descuento
        contador_descuento=contador_descuento+1
    if(descuento=='N') or (descuento=='n'):
        print("no tiene descuento")
        entrada_sin_descuento=cantidad_espectadores*75
        acumulador_sin_descuento=acumulador_sin_descuento+entrada_sin_descuento
    contador=contador+1
total_funciones=acumulador_descuento+acumulador_sin_descuento
porcentaje_funciones=((contador_descuento*total_funciones)/100)
print("la recaudacion total es de:",total_funciones)
print("funciones con descuento: ",contador_descuento)
print("promedio del total de funciones:",porcentaje_funciones)
