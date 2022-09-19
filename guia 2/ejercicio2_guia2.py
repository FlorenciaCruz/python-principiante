"Secuencia de impares. Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos, en forma ascendente y descendente."
"""entrada
____________________
____________________
proceso
____________________
____________________
salida
____________________
____________________"""
resto=int
i=int
numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese otro numero: "))
for i in range(numero1,numero2+1):
    if(i%2!=0):
       print(i)
for i in range (numero1, numero2, -1):
    resto = i % 2
    if resto != 0:
        print(i)