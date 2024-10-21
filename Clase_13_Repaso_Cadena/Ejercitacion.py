'''Ejercitación Clase 13 
(Cadenas de Caracteres Algorítmicamente)

1. Realizar una función llamada es_alfabetico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfabéticos (a-z/A-Z) -> No hace falta tener en cuenta los acentos y algún otro carácter

Tener en cuenta los caracteres ASCII imprimibles que sólo sean letras

CODIGO ASCII

2. Realizar una función llamada es_entero() que recibe una cadena y verifica si la misma tiene sólo caracteres numéricos (0-9) 

Tener en cuenta los caracteres ASCII imprimibles que sólo sean números enteros

3. Realizar una función llamada es_alfanumerico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfanuméricos (a-z/A-Z/0-9) 

Tener en cuenta los caracteres ASCII imprimibles que sólo sean números enteros y caracteres alfabéticos.
Deberia reutilizar las funciones anteriores ya que me ayudara a que mi código sea más rápido de hacer.

4. Realizar la función es_mayuscula() que me verifica que la cadena que le pase como parámetro está en mayúscula o no.
Devuelve True si esa cadena está en mayúscula.
Devuelve False en caso contrario

5. Realizar la función es_minuscula() que me verifica que la cadena que le pase como parámetro está en minúscula o no.
Devuelve True si esa cadena está en minúscula.
Devuelve False en caso contrario

6. Realizar una función que me permita convertir un carácter de mi cadena a mayúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en mayúscula. 
En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

7. Realizar una función que me permita convertir un carácter de mi cadena a minúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en minúscula. 
En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

8.Realizar una función que me permita convertir toda mi cadena a mayúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en minúscula a mayúscula.
Los otros caracteres que no sean alfabéticos simplemente los deja como está.

9.Realizar una función que me permita convertir toda mi cadena a minúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en mayúscula a minúscula.
Los otros caracteres que no sean alfabéticos simplemente los deja como está.

10.Crear una función llamada capitalizar_texto(), en la que recibe una cadena y devuelve la misma con la primer letra en mayúscula y todas las demás en minúscula.

11.Crear una función llamada generar_titulo(), en la que recibe una cadena y devuelve la misma con cada palabra con la primera letra mayúscula y todas las demás en minúscula

Ejemplo: “hOla mUNdO” —>  “Hola Mundo”


12.Crear una función llamada formatear_nombre_apellido() en la que recibe una cadena cualquiera y extrae sólo el nombre y apellido de la misma en el formato correcto: (Nombre Apellido)

Ejemplo: 

cadena = “123mAriAnO ferNanDEZ 911%@”
cadena_resultado = formatear_nombre_apellido(cadena)
print(cadena_resultado) —> “Mariano Fernandez”

PISTA: La función del punto 2 debería funcionar también para un sólo carácter.
NOTA:Deberían reutilizar varias funciones hechas anteriormente.

13. Crear una función que reciba como parámetro una cadena y suprima los caracteres repetidos consecutivos.
Ejemplo: Si recibe como parámetro la cadena “Hooola” debe devolver “Hola”. 

14. Crear una función que reciba una cadena por parámetro y suprima las vocales de la misma. 
Ejemplo: Si recibe como parámetro la cadena “Hola” debe devolver “Hl”.

15.Crear una función para contar cuántas veces aparece una subcadena dentro de una cadena. 
Ejemplo: Si recibe la cadena “El origen del gen” y la subcadena “gen” deberá retornar el valor 2.

'''

# 1. Realizar una función llamada es_alfabetico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfabéticos (a-z/A-Z) -> No hace falta tener en cuenta los acentos y algún otro carácter

# cadena = "la32A"

def es_alfabetico(cadena:str):
    '''
    Recibe una cadena y verifica si tiene caracteres alfabeticos

    '''
    retorno = True
    for i in range(len(cadena)):
        if cadena[i] != " ":
            caracter_ascii = ord(cadena[i])
            if caracter_ascii < 65 or caracter_ascii > 90 and caracter_ascii < 97 or caracter_ascii > 122:
                retorno = False
                break
            
    return retorno


# print(es_alfabetico(cadena))

# 2. Realizar una función llamada es_entero() que recibe una cadena y verifica si la misma tiene sólo caracteres numéricos (0-9) 

# Tener en cuenta los caracteres ASCII imprimibles que sólo sean números enteros

# cadena = "32 pepe"

def es_entero(cadena:str):
    '''
    Recibe una cadena y verifica si tiene caracteres numericos
    '''
    retorno = True
    for i in range(len(cadena)):
        if cadena[i] != " ":
            caracter_ascii = ord(cadena[i])
            if caracter_ascii < 48 or caracter_ascii > 57:
                retorno = False
                break
            
    return retorno

# print(es_entero(cadena))


# 3. Realizar una función llamada es_alfanumerico() que recibe una cadena y verifica si la misma tiene sólo caracteres alfanuméricos (a-z/A-Z/0-9) 
# Tener en cuenta los caracteres ASCII imprimibles que sólo sean números enteros y caracteres alfabéticos.


# cadena = "Hola por vez 999"

def es_alfanumerico(cadena:str):
    '''
    Recibe una cadena y verifica si tiene caracteres alfabeticos y numericos

    '''
    retorno = "Introdujo una cadena vacia"
    for i in range(len(cadena)):
        if cadena[i] != " ":
            caracter_ascii = ord(cadena[i])
            if (caracter_ascii > 47 and caracter_ascii < 58) or (caracter_ascii > 64 and caracter_ascii < 91) or (caracter_ascii > 96 and caracter_ascii < 123):
                retorno = True
            else:
                retorno = False
    

    return retorno

# print(es_alfanumerico(cadena))

# 4. Realizar la función es_mayuscula() que me verifica que la cadena que le pase como parámetro está en mayúscula o no.
# Devuelve True si esa cadena está en mayúscula.
# Devuelve False en caso contrario

def es_mayuscula(cadena:str):
    '''
    Verifica si la cadena que tiene de parametro está toda en mayuscula o no
    '''
    retorno = "Introdujo una cadena vacia..."
    for i in range(len(cadena)):
        if cadena[i] != " ":
            caracter_ascii = ord(cadena[i])
            if caracter_ascii > 64 and caracter_ascii < 91:
                retorno = True
            else:
                retorno = False

    return retorno

# print(es_mayuscula(cadena=""))

# 5. Realizar la función es_minuscula() que me verifica que la cadena que le pase como parámetro está en minúscula o no.
# Devuelve True si esa cadena está en minúscula.
# Devuelve False en caso contrario

def es_minuscula(cadena:str):
    '''
    Verifica si la cadena que tiene de parametro está toda en minuscula o no
    '''
    retorno = "Introdujo una cadena vacia..."
    for i in range(len(cadena)):
        if cadena[i] != " ":
            caracter_ascii = ord(cadena[i])
            if caracter_ascii > 96 and caracter_ascii < 123:
                retorno = True
            else:
                retorno = False

    return retorno

# print(es_minuscula(cadena="hola"))

# 6. Realizar una función que me permita convertir un carácter de mi cadena a mayúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en mayúscula. 
# En caso de que el carácter no sea alfabético o ya se encuentre en mayúscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.


def convertir_cadena_a_mayuscula(cadena:str):
    '''
    Convierte la letra de la cadena a mayuscula
    '''
    if len(cadena) == 1:
        caracter_ascii = ord(cadena)
        caracter_ascii -= 32
        nuevo_caracter = chr(caracter_ascii)
        retorno = nuevo_caracter

        if caracter_ascii < 65 or caracter_ascii > 90 and caracter_ascii < 97 or caracter_ascii > 122:
            retorno = cadena
        
    elif len(cadena) > 1:
        return None

    return retorno

# print(convertir_cadena_a_mayuscula("9"))

# 7. Realizar una función que me permita convertir un carácter de mi cadena a minúscula, se le pasa como parámetro un str con un sólo carácter (validar que esto ocurra) y devuelve dicho carácter en minúscula. 
# En caso de que el carácter no sea alfabético o ya se encuentre en minuscula, devuelve ese mismo carácter sin cambios, en caso de que haya recibido un str con más de un carácter la función devuelve None.

def convertir_cadena_a_minuscula(cadena:str):
    '''
    Convierte la letra de la cadena a minuscula
    '''
    if len(cadena) == 1:
        caracter_ascii = ord(cadena)
        caracter_ascii += 32
        nuevo_caracter = chr(caracter_ascii)
        retorno = nuevo_caracter

        if caracter_ascii < 65 or caracter_ascii > 90 and caracter_ascii < 97 or caracter_ascii > 122:
            retorno = cadena
        
    elif len(cadena) > 1:
        return None

    return retorno

# print(convertir_cadena_a_minuscula("A"))

# 8.Realizar una función que me permita convertir toda mi cadena a mayúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en minúscula a mayúscula.
# Los otros caracteres que no sean alfabéticos simplemente los deja como está.
# cadena = "CarLiTos"


def convertir_toda_la_cadena_a_mayuscula(cadena:str):
    '''
    Recibe una cadena y la pasa toda a mayuscula
    '''
    nueva_cadena = ""
    for i in range(len(cadena)):
        caracter_ascii = ord(cadena[i])
        if cadena[i] != " ":
            if 97 <= caracter_ascii <= 122:
                caracter_ascii -= 32


        nuevo_caracter = chr(caracter_ascii)
        nueva_cadena += nuevo_caracter


    return nueva_cadena


# print(convertir_toda_la_cadena_a_mayuscula(cadena))

# 9.Realizar una función que me permita convertir toda mi cadena a minúscula, se le pasa una cadena y devuelve la misma convirtiendo cada carácter alfabético en mayúscula a minúscula.
# Los otros caracteres que no sean alfabéticos simplemente los deja como está.

def convertir_toda_la_cadena_a_minuscula(cadena:str):
    '''
    Recibe una cadena y la pasa toda a minuscula
    '''
    nueva_cadena = ""
    for i in range(len(cadena)):
        caracter_ascii = ord(cadena[i])
        if cadena[i] != " ":
            if 65 <= caracter_ascii <= 90:
                caracter_ascii += 32


        nuevo_caracter = chr(caracter_ascii)
        nueva_cadena += nuevo_caracter


    return nueva_cadena

# print(convertir_toda_la_cadena_a_minuscula(cadena="HOLA COMO VA"))


# 10.Crear una función llamada capitalizar_texto(), en la que recibe una cadena y devuelve la misma con la primer letra en mayúscula y todas las demás en minúscula.

def capitalizar_texto(cadena:str):
    '''
    
    '''
    nueva_cadena = ""
    # for i in range(len(cadena)):
    caracter_ascii = ord(cadena[0])
    if cadena[0]:
        if 97 <= caracter_ascii <= 122:
            caracter_ascii -= 32
            letra_mayuscula = chr(caracter_ascii)
        elif 65 <= caracter_ascii <= 90:
            letra_mayuscula = chr(caracter_ascii)
        
        nueva_cadena += letra_mayuscula

    return nueva_cadena

print(capitalizar_texto("hola"))