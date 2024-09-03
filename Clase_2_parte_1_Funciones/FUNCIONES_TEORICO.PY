# CODIGO DE BLOQUE ESPECIFICO QUE REALIZA UNA TAREA.


# SIRVE PARA DESCOMPONER UNA TAREA ESPECIFICA, QUE SE PUEDE LLAMAR VARIAS VECES EN CUALQUIER PARTE DEL PROGRAMA
# PERMITE QUE SEA MODULAR, LEGIBLE Y FACIL DE ENTENDER.
# SIRVE PARA MINIMIZAR, DEPURAR Y MODIFICAR FACILMENTE CADA MODULO
# REUTILIZAR CODIGO, CADA FUNCION ES INDEPENDIENTE, POR ENDE SE OBTIENE UNA AUTONOMIA.


# parametros = Datos de entrada del usuario


#Definicion de una funcion

#> Crea la funcion
#|
#|                              #PARAMETROS FORMALES
def calcular_precio_con_iva (importe_sin_iva : float, iva:float=21) -> float:
    '''
    Se encarga de calcular el precio con iva, recibe un importe sin iva y también el iva (opcional)
    que por defecto es 21%.
    Retorna el precio iva
    '''
    importe_con_iva = importe_sin_iva * (1 + (iva / 100))
    return importe_con_iva

def sumar_enteros (numero_a:int, numero_b:int) -> int:
    '''
    Se encarga de sumar dos numeros enteros que ingrese el usuario, retorna la suma de ambos.
    '''
    suma = numero_a + numero_b
    return suma

importe = float(input("Ingrese su importe:"))
resultado = calcular_precio_con_iva(importe)
print(f"Su importe con un valor de {importe} tiene como valor final con un iva del 21% {resultado}")

#PARAMETROS ACTUALES
# numero_uno = int(input("Ingrese numero 1:"))
# numero_dos = int(input("Ingrese numero 2:"))
# resultado = sumar_enteros(numero_uno, numero_dos)
# print (f"El resultado de la suma entre {numero_uno} y {numero_dos} es {resultado}")





