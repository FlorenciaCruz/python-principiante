"""Crear un conversor de dólares a pesos y pesos a dólares, donde se ingrese por teclado el valor del peso actual.
entrada
________________
pesos
________________
proceso
________________
pesos_conversion=(pesos/295)
dolares_conversion
________________
salida
________________
pesos
conversion
________________"""
conversion=float
valor_pesos=float
dolares_conversion=float
valor_pesos=float(input("ingrese el valor de pesos: "))
pesos=float(input("ingrese los pesos a convertir a dolar: "))
pesos_conversion=(pesos/valor_pesos)
print("pesos:",pesos,"son",round(pesos_conversion),"dolares")
valor_dolares=float(input("ingrese el valor del dolar: "))
dolares=float(input("ingrese los dolares a convertir a pesos: "))
dolares_conversion=(dolares*pesos)
print("dolares:",dolares,"son",round(dolares_conversion),"pesos")
