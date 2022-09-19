"""Jornal de un Operario. Se necesita desarrollar un programa para el área de recursos humanos
 de una empresa que permita informar el jornal de un determinado operario. Usted deberá cargar
  por teclado el código de turno que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno)
   y la cantidad de horas trabajadas. La política de trabajo en la empresa es que los operarios de la misma pueden
    trabajar en el turno diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora,
     si lo hace en el turno diurno cobra 35.50 pesos la hora"""
#declaracion de variables
turno=int
turno=1
horas=int
total_horas=float
nocturno=float
diurno=float
#inicio del programa
print("JOURNAL DE UN OPERARIO")
print("menu de turnos")
print("1)turno diurno")
print("2)turno nocturno")
while(turno!=0):#termina cuando el turno es 0
  turno=int(input("ingrese el turno:"))#ingreso el turno por teclado
  if(turno==1):#si el turno es 1 entonces
    horas=int(input("ingrese la cantidad de horas trabajadas:"))#ingreso cantidad de horas por teclado
    diurno=horas*35.50#salario diurno
    print("salario diurno",diurno,"pesos")#imprimo los resultados
  if(turno==2):#si el turno es 2 entonces
    horas=int(input("ingrese la cantidad de horas trabajadas"))#ingreso cantidad de horas por teclado
    nocturno=horas*40.60#salario nocturno
    print("salario nocturno",nocturno,"pesos")#imprimo los resultados
turno=int(input("ingrese el turno:"))#ingreso el turno por teclado
print("la suma de las horas trabajadas es de:")
total_horas=diurno+nocturno;
print(total_horas)#imprimo las horas trabajas que son la suma de el turno diurno y nocturno
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO      ENTRADA                                        SALIDA  
 **********************************************************************************************************
 *     1     *  ingrese el turno:1                          *  
 *           *  ingrese la cantidad de horas trabajadas:80  *                                                                                                               
 *           *  ingrese el turno:2                          *   salario diurno 2840.0 pesos                                         
 *           *  ingrese el turno:0                          *  
 *           *  ingrese la cantidad de horas trabajadas70   *   salario nocturno 2842.0 pesos
 *           *                                              *   la suma de las horas trabajadas es de:
 *           *                                              *   5682.0
 * ********************************************************************************************************
 *"""
