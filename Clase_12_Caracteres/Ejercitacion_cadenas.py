'''
5. Realizar una función que me cuente la cantidad de vocales de mi cadena, la misma recibe una cadena y devuelve la cantidad de vocales que encontró.

6. Realizar una función que me cuente la cantidad de consonantes de mi cadena, la misma recibe una cadena y devuelve la cantidad de consonantes que encontró.

7. Realizar una función que me quite los espacios de mi cadena, recibe una cadena y devuelve una nueva cadena con los espacios eliminados.

8. Crear una función llamada repetir_cadena() que lo que va a hacer es replicar lo mismo que hace el operador * en cadenas pero separando las mismas por un espacio, se le pasa como parámetro la cadena que va a repetir, y un entero que me indique la cantidad de veces que la misma se va a repetir. 
Devuelve como resultado una cadena resultante.

NOTA: Resolver sin usar operador *

Ejemplo de uso:
cadena = “Hola”
cadena_repetida = repetir_cadena(cadena,5)

print(cadena_repetida) -> ‘’hola hola hola hola hola‘’ 

'''

# 5. Realizar una función que me cuente la cantidad de vocales de mi cadena, la misma recibe una cadena y devuelve la cantidad de vocales que encontró.
# cadena = input("Ingrese una cadena: ")

def contar_vocales (cadena:str)-> int:
    '''
    Cuenta las vocales que tiene la cadena ingresada
    Devuelve un contador
    '''
    contador_vocales = 0
    for caracter in cadena:
        if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u":
            contador_vocales += 1
    return contador_vocales

print(f"En su cadena hay un total de {contar_vocales(cadena)} vocales")


# 6. Realizar una función que me cuente la cantidad de consonantes de mi cadena, la misma recibe una cadena y devuelve la cantidad de consonantes que encontró.
# cadena = input("Ingrese una cadena: ")

def contar_consonantes (cadena:str)-> int:
    '''
    Recibe una cadena y cuenta las letras que no son vocales
    Devuelve cuantas consonantes hay
    '''
    contador_consonantes = 0
    for caracter in cadena:
        if caracter != "a" and caracter != "e" and caracter != "i" and caracter != "o" and caracter != "u":
            contador_consonantes += 1
    return contador_consonantes

print(f"En su cadena hay un total de {contar_consonantes(cadena)} consonantes")

# 7. Realizar una función que me quite los espacios de mi cadena, recibe una cadena y devuelve una nueva cadena con los espacios eliminados.


cadena = input("Ingrese una cadena: ")
def quitar_espacios(cadena:str)-> str:
    '''
    
    '''
    resultado = ""
    for caracter in cadena:
        if caracter != " ":
            resultado += caracter

    return resultado

print(quitar_espacios(cadena))

# 8. Crear una función llamada repetir_cadena() que lo que va a hacer es replicar lo mismo que hace el operador * en cadenas pero separando las mismas por un espacio, se le pasa como parámetro la cadena que va a repetir, y un entero que me indique la cantidad de veces que la misma se va a repetir. 
# Devuelve como resultado una cadena resultante.


# NOTA: Resolver sin usar operador *

# Ejemplo de uso:
# cadena = “Hola”
# cadena_repetida = repetir_cadena(cadena,5)

# print(cadena_repetida) -> ‘’hola hola hola hola hola‘’ 

cadena = input("Ingrese una cadena: ")

def repetir_cadena(cadena:str,veces_repetida:int):
    '''
    
    '''
    resultado = ""
    for i in range(veces_repetida):
        resultado += f"{cadena} "
    return resultado

print(repetir_cadena(cadena, 5))