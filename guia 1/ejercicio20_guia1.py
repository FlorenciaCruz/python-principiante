"Tarjeta de Bingo. Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaría la tarjeta de bingo de una persona. Una vez generado los números aleatorios solicitar al usuario que ingrese 3 números enteros, a parƟr de allí mostrar los siguientes mensajes: Si el usuario no marcó ninguno de los números, indicarlo diciendo “El jugador tiene mala suerte, no marcó ninguna casilla”. Caso contrario mostrar “El jugador marcó algún número de la tarjeta”."
from random import*
numero=randint(1,100)
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))
numero3=int(input("ingrese otro numero: "))
if(numero1==numero)or(numero2==numero)or(numero3==numero):
    print("el jugador marco algun numero en la tarjeta")
else:
    print("el jugador tiene mala suerte, no marco ningun numero en la casilla")
    
