"""Conversión de medidas.
Desarrolle un programa para convertir
una medida dada en pies a sus equivalentes en: yardas pulgadas cenơmetros metros
Sabiendo que: 1 pie = 12 pulgadas 1 yarda = 3 pies 1 pulgada = 2.54 centímetros 1 metro =1000
___________________________________________________________
entrada
___________________________________________________________
pies

___________________________________________________________
proceso
___________________________________________________________
pulgadas=pies*12
pulgada=pulgadas*2.54
yarda=pies*3
metro=pulgada/1000

___________________________________________________________
salida
___________________________________________________________
proceso
pulgadas
pulgada
yarda
metro
___________________________________________________________"""
"declaracion de variables"
pies=float
pulgadas=float
pulgada=float
yarda=float
metro=float
"inicializacion del programa"
pies=float(input("ingrese la cantidad de pies: "))#ingreso la cantidad de pies por teclado
pulgadas=pies*12;#formula de pies a pulgadas
pulgada=pulgadas*2.54;#formula de pulgada
yarda=pies*3;#formula de pies a yarda
metro=pulgada/100;#formula de metro
#muestro por pantalla las conversiones
print("la conversion de pies a:")
print("pulgadas",pulgadas)
print("pulgada",pulgada)
print("yarda",yarda)
print("metro",metro)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO     ENTRADA      SALIDA
 **********************************************************************************************************
 *     1     *  ingrese la cantidad de pies: 2  * la conversion de pies a:
                                                *  pulgadas 24.0
                                                *  pulgada 60.96
                                                *  yarda 6.0
                                                *  metro 0.6096                                                                                                                                  
 * ********************************************************************************************************
 *     2     *  ingrese la cantidad de pies: 132 * la conversion de pies a:
                                                 *   pulgadas 1584.0
                                                 *   pulgada 4023.36
                                                 *   yarda 396.0
                                                 *   metro 40.2336                                                                                                                                                
 * ********************************************************************************************************
 *"""