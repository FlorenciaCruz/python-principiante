"Mostrar por pantalla el promedio de los números ingresados por teclado. Se deja de pedir que el usuario agregue números una vez ingrese 0 (cero)."
promedio=int
acumulador_numeros=int
acumulador_numeros=0
contador_numeros=int
contador_numeros=-1
numeros=int
numeros=1
while(numeros!=0):
    numeros=int(input("ingrese un numero: "))
    acumulador_numeros=acumulador_numeros+numeros
    contador_numeros=contador_numeros+1
    
promedio=acumulador_numeros/contador_numeros
print("el promedio de los numeros es:",promedio)
print(contador_numeros)
