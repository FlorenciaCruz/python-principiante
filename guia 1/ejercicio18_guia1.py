"""Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo hace en el turno diurno cobra 35.50 pesos la hora"""
turno=int
turno=1
horas=int
total_horas=float
nocturno=float
diurno=float
print("JOURNAL DE UN OPERARIO")
print("menu de turnos")
print("1)turno diurno")
print("2)turno nocturno")
while(turno!=0):
  turno=int(input("ingrese el turno:"))
  if(turno==1):
    horas=int(input("ingrese la cantidad de horas trabajadas:"))
    diurno=horas*35.50
    print("salario diurno",diurno,"pesos")
  if(turno==2):
    horas=int(input("ingrese la cantidad de horas trabajadas"))
    nocturno=horas*40.60
    print("salario nocturno",nocturno,"pesos")
turno=int(input("ingrese el turno:"))
print("la suma de las horas trabajadas es de:")
total_horas=diurno+nocturno;
print(total_horas)
