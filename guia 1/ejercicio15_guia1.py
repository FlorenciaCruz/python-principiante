"Crear un conversor de pies y pulgadas a centímetros."
"""entrada
_________________
pies
pulgadas
_________________
proceso
_________________
pies_centimetros
pulgadas_centimetros
_________________
salida
_________________
pies_centimetros
pulgadas_centimetros

_________________"""
print("conversor de pies a centimetros")
pies=float(input("escriba los pies a convertir a centimetros: "))#ingreso por teclado los pies
pies_centimentros=0
pies_centimetros=(pies/30.48)#conversion de pies a centimentros
print(pies,"pies ______________",pies_centimentros,"centimetros")#imprimo los resultados
print("conversor de pulgadas a centimetros")
pulgadas=float(input("escriba las pulgadas a convertir a centimetros: "))
pulgadas_centimetros=0
pulgadas_centimetros=(pulgadas/2.54)#conversion de pulgadas a centimetros
print(pulgadas,"pulgadas _____________",pulgadas_centimetros,"centimetros")#imprimo resultados
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO   ENTRADA SALIDA        
 **********************************************************************************************************
 *  1   *   escriba los pies a convertir a centimetros: 100 *   100.0 pies ______________3,2808398950131233595800524934383 centimetros
 *      *   escriba las pulgadas a convertir a centimetros: 100 * 100.0 pulgadas _____________ 39.37007874015748 centimetros  
 * ********************************************************************************************************
 *"""
