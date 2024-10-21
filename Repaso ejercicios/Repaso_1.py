# 1. Realizar una función recursiva que calcule la suma de los primeros números naturales:

# def sumar_naturales (numero:int) -> int:
#     '''
    
#     '''
#     if numero > 0:
#         resultado = numero + sumar_naturales(numero - 1)
        
#     else:
#         resultado = 0
    
#     return resultado
# # 5 + 4 + 3 + 2 + 1 = 15

# # numero_uno = int(input("Ingrese el numero: "))

# # print(sumar_naturales(numero_uno))


# # 2. Realizar una función recursiva que calcule la potencia de un número:

# def calcular_potencia (numero:int,potencia:int) -> int:
#     '''
    
#     '''
#     if numero == 0:
#         resultado = 0
#     elif numero != 0 and potencia == 0:
#         resultado = 1
#     else:
#         resultado = numero * calcular_potencia(numero, potencia - 1)

#     return resultado

# numero = int(input("Ingrese el numero que quiere calcular la potencia: "))

# numero_potencia = int(input("Ingrese la potencia: "))

# print(calcular_potencia(numero,numero_potencia))

# 1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

# Para saber la cantidad de elementos de un str usamos la función len()


# def verificar_dni (dni:str) -> bool:

#     '''
    
#     '''
#     if len(dni) < 6 or len(dni) > 8:
#         return False
#     else:
#         return True

# dni = input("Ingrese su NRO de DNI: ")
# print(verificar_dni(dni))
# 2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos), deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
# En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”

# Ej: Se ingresa “12345”, y devolverá “DNI INVALIDO”.
# Ej: Se ingresa “123456”, y devolverá “00123456”.
# Ej: Se ingresa “1234567”, y devolverá “01234567”.
# Ej: Se ingresa “12345678”, y devolverá “12345678”.
# Ej: Se ingresa “123456789”, y devolverá “DNI INVALIDO”.

# Nota: Reutilizar la función del ejercicio 1 para validar si el dni es válido

def completar_dni (dni:str) -> str:
    '''
    
    '''
    if len(dni) < 6 or len(dni) > 8:
        return "DNI INVALIDO"
    elif len(dni) == 6 or len(dni) == 7:
        num_dni = '{:0>8}'.format(dni)
        return f"El dni con 8 digitos seria {num_dni}"
    elif dni == 8:
        return f"El dni es {dni}"
    

dni = input("Ingrese su NRO de DNI: ")
print(completar_dni(dni))
