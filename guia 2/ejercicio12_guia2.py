"""Números pares e impares Se pide desarrollar un programa que permita leer una serie de números.
 La nalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
  Los requerimientos funcionales del programa son: La sumatoria de solo los números que estén comprendidos entre 50 y 100.
   Cantidad de valores pares ingresados. Cantidad de valores impares ingresados.
    Informar si en la carga de números se ingreso al menos un número 0.
     Informar si la serie contiene solo números pares e impares alternados."""
# numeros=int
numeros=1
#sumatoria_numeros=int
sumatoria_numeros=0
#valores_pares=int
valores_pares=0
#valores_impares=int
valores_impares=0
#valores_cero=int
valores_cero=0
#alternados=int
alternados=0
contador=0
anterior=0
alternar=0
print("la  carga de los numeros finaliza con un numero negativo")
while(numeros>-1):
    numeros=int(input("ingrese un numero:"))
    if(numeros>50) and (numeros<100):
        sumatoria_numeros=sumatoria_numeros+1
    if(numeros%2==0):
        valores_pares=valores_pares+1;
    if(numeros&2!=0):
        valores_impares=valores_impares+1
    if(numeros==0):
        valores_cero=valores_cero+1
    contador=contador+1
    if(numeros<0) and (numeros<=contador):
        anterior=numeros
    if anterior%2==0 and numeros%2!=0 or anterior%2!=0 and numeros%2==0:
        alternar=alternar+1
#if(((numeros%2==0) and (numeros&2!=0)) or ((numeros%2=!0) and (numeros%2==0))):
#    alternados=alternados+1
print("numero de veces alternados:",alternar)
print("contador:",contador)
print("numeros entre 50 y 100:",sumatoria_numeros)
print("valores pares ingresados:",valores_pares)
print("valores impares ingresados:",valores_impares)
print("valores iguales a cero:",valores_cero)
#print("valores alternados:",alternados)