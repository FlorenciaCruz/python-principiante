"17. Suma - División - Potencia. Se necesita desarrollar un programa que permita calcular la suma de tres números. Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales), en caso contrario elevar el resultado al cubo."
numero1=int
numero2=int
numero=int
suma=int
numero1=int(input("ingrese el numero1: "))
numero2=int(input("ingrese el numero2: "))
numero3=int(input("ingrese el numero3: "))
suma=numero1+numero2+numero3
print("la suma de todos los numeros es: ",suma)
if(suma>10):
    print("division:",round(suma/2))
else:
    print("potencia",suma*suma*suma)
