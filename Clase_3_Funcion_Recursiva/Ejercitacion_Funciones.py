'''
Ejercitación Clase 5 (Funciones Avanzado)

'''


# 1. Desarrollar una función que verifique el DNI de una persona, la misma recibirá un str (se asume que solamente contiene caracteres numéricos). Si la cantidad de caracteres es menor a 6 o mayor a 8, retornara False. Si la cantidad de caracteres está comprendida entre 6 y 8 devolverá True

# Para saber la cantidad de elementos de un str usamos la función len()


def verificar_dni (numero_dni:int) -> int:
    cantidad_caracteres = len(str(numero_dni))
    if cantidad_caracteres >= 6 and cantidad_caracteres <= 8:
        return True
    else:
        return False
    
numero_dni_usuario = int(input("Ingrese su DNI: "))
print(verificar_dni(numero_dni_usuario)) 


# 2. Desarrollar una función que complete el número de DNI de una persona. Recibirá un str (se asume que solamente contiene caracteres numéricos), deberá medirla (len) y completar con ceros a la izquierda hasta llegar a un total de 8 caracteres, y devolviendo la cadena resultante. 
# En caso de que el dni sea invalido (que no tiene entre 6 y 8 caracteres) devolvera una cadena que dice : “DNI INVALIDO”

# Ej: Se ingresa “12345”, y devolverá “DNI INVALIDO”.
# Ej: Se ingresa “123456”, y devolverá “00123456”.
# Ej: Se ingresa “1234567”, y devolverá “01234567”.
# Ej: Se ingresa “12345678”, y devolverá “12345678”.
# Ej: Se ingresa “123456789”, y devolverá “DNI INVALIDO”.

# Nota: Reutilizar la función del ejercicio 1 para validar si el dni es válido

def verificar_dni (numero_dni:int) -> int:
    cantidad_caracteres = len(str(numero_dni))
    if cantidad_caracteres < 6:
        return "Su DNI es invalido, debe tener mas de 6 digitos"
    elif cantidad_caracteres == 6 or cantidad_caracteres == 7:
        dni = '{:0>8}'.format(numero_dni) #Se usa .format() para formatear cadenas de texto, permitiéndote insertar valores de una manera controlada y flexible.
                #{:0>8} Indica que deben haber al menos 8 caracteres, si no los hay, completa con 0 a la izquierda o derecha, depende el < >.
        return f"El DNI con 8 digitos seria {dni}"
    elif cantidad_caracteres == 8:
        return f"Su DNI es {numero_dni}"
    else:
        return "DNI Invalido, no ingrese mas de 8 digitos"
    

numero_dni_usuario = int(input("Ingrese su DNI: "))
print(verificar_dni(numero_dni_usuario)) 
