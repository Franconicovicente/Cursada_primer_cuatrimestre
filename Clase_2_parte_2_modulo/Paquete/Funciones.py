#EN ESTE MODULO SOLO FUNCIONES QUE VAMOS A USAR.

from .Validaciones import *


def saludar():
    print("Hola Mundo!")


def sumar(numero_a:int, numero_b:int) -> int:
    resultado = numero_a + numero_b
    return resultado


def informar_num_positivo(numero:float) -> None:
    if (verificar_positividad(numero)):
        print(f"El numero es {numero} positivo")
    
    else:
        print(f"El numero {numero} es negativo")



    

