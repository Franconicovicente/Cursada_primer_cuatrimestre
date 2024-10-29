cadena = "HOLA MUNDO" # hola mundo
nueva_cadena = "" # hola mundo

for i in range(len(cadena)):
    if cadena[i] != " ":
        caracter = cadena[i]
        caracter_ascii = ord(caracter)
        caracter_ascii += 32 
        nuevo_caracter = chr(caracter_ascii)
        nueva_cadena += nuevo_caracter
    else:
        nueva_cadena += cadena[i]
    
print(nueva_cadena)