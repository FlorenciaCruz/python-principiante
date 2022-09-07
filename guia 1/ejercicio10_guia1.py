"""Ingresar la cantidad de números de la sucesión de Fibonacci a mostrar.
entrada
____________________________
numero
____________________________
proceso
____________________________
contador
suma
____________________________
salida
____________________________
suma
____________________________"""
"declaracion de variables"
numero=int
contador=int
primer_numero=int
segundo_numero=int
suma=int
numero=int(input("ingrese un numero:"))
primer_numero=0
segundo_numero=1
suma=0
contador=1
while(contador<=numero):
    print(suma)
    contador=contador+1;
    primer_numero=segundo_numero
    segundo_numero=suma
    suma=primer_numero+segundo_numero;
