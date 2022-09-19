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
#inicio del programa
primer_numero=int(input("ingrese el primer numero: "))#ingreso primer numero por teclado
segundo_numero=int(input("ingrese el segundo numero: "))#ingreso segundo numero por teclado
division=primer_numero/segundo_numero;#almacena la division del primer numero por el segundo numero
cociente=primer_numero//segundo_numero;#almacena el cociente del primer numero y el segundo numero
resto=primer_numero%segundo_numero;#almacena el resto del primer y segundo numero
#imprime los resultados por pantalla
print("la division del primer numero ",primer_numero,"por el segundo numero ",segundo_numero,"es de",division)
print("el cociente del primer numero ",primer_numero,"por el segundo numero ",segundo_numero,"es de",cociente)
print("el resto del primer numero: ",primer_numero,"por el segundo numero: ",segundo_numero,"es de",resto)
"""********************************************************************************************************
                                    PRUEBA DE ESCRITORIO
 **********************************************************************************************************
  INTENTO            ENTRADA                                SALIDA
 **********************************************************************************************************
 *     1     *      ingrese el primer numero: 120   *       la division del primer numero  120 por el segundo numero  20 es de 6.0
 *           *      ingrese el segundo numero: 20   *       el cociente del primer numero  120 por el segundo numero  20 es de 6  
 *           *                                      *       el resto del primer numero:  120 por el segundo numero:  20 es de 0 
 *           *                                      *                                                                
 *           *                                      *        
 *           *                                      *          
 * ********************************************************************************************************
 *"""
