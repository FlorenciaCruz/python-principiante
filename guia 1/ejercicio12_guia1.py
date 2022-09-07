"Escribir un programa que pida dos números y muestre como resultado su división, cociente y resto."
"""entrada
_________________
primer_numero
segundo_numero
_________________
proceso
_________________
division=primer_numero/segundo_numero
cociente=primer_numero//segundo_numero
resto=primer_numero%segundo_numero
_________________
salida
_________________
primer_numero
segundo_numero
division
cociente
resto
_________________"""

primer_numero=int(input("ingrese el primer numero: "))
segundo_numero=int(input("ingrese el segundo numero: "))
division=primer_numero/segundo_numero;
cociente=primer_numero//segundo_numero;
resto=primer_numero%segundo_numero;
print("la division del primer numero ",primer_numero,"por el segundo numero ",segundo_numero,"es de",division)
print("el cociente del primer numero ",primer_numero,"por el segundo numero ",segundo_numero,"es de",cociente)
print("el resto del primer numero: ",primer_numero,"por el segundo numero: ",segundo_numero,"es de",resto)
