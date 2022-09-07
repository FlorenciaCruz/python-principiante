"""Multiplicación. Ingresar un número cualquiera por teclado y que muestre su respectiva tabla del 1 al 10.
entrada
___________________
numero
___________________
proceso
___________________
contador=contador+1
tabla=contador*numero
___________________
salida
___________________
contador
numero
tabla
___________________"""
contador=int
contador=0
numero=(int(input("ingrese un numero y se mostrata su tabla de multiplicar hasta el 10")))
while(contador<=10):
    contador=contador+1;
    tabla=contador*numero;
    print(contador,"x",numero,"=",tabla)
