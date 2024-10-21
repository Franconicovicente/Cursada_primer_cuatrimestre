#Acceso

cadena = "Hola Mundo"
largo_cadena = len(cadena)

#Accedo al primer caracter
print(cadena[0])
#Accedo al segundo caracter
print(cadena[1])

#Accedo al último caracter
print(cadena[9])
#print(cadena[-1]) # SOLO FUNCIONA EN PYTHON
#print(cadena[10]) -> ERROR
print(cadena[largo_cadena - 1])

for i in range(len(cadena)):
    print(cadena[i],end="")
print("")

for caracter in cadena:
    print(caracter,end="")
print("")

#Modificacion

cadena[0] = "A"
lista_cadena = list(cadena)
lista_cadena[0] = "A"

cadena_dos = ""

for i in range(len(lista_cadena)):
    cadena_dos += lista_cadena[i]

print(lista_cadena)
print(cadena_dos)

cadena_dos = ""

for i in range(len(cadena)):
    if i == 0:
        cadena_dos += "A"
    else:
        cadena_dos += cadena[i]
        
print(cadena_dos)

#Slicing

cadena = "Hola Mundo"

# #Mostrar la palabra Hola [0:4]

print(cadena[0:4])

# #Mostrar la palabra Mundo [5:10]

print(cadena[5:10])

#Concatenacion

cadena = "Hola "
#cadena += "Mundo"
cadena = cadena + "Mundo"

print(cadena)

#Repeticion

cadena = "Hola" 
print(cadena * 5)

#Comparación

cadena_uno = "Mariano"
cadena_dos = "Daniela"

print(cadena_uno == cadena_dos)
print(cadena_uno != cadena_dos)
print(cadena_uno > cadena_dos)
print(cadena_uno < cadena_dos)

#CODIGO ASCII

cadena = "Mariano"
caracter = cadena[0]

print(ord(caracter))

letra_o = 111
caracter = chr(letra_o)
print(caracter)

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

def verificar_igualdad(cadena_uno:str,cadena_dos:str) -> bool:
    largo_cadena_uno = len(cadena_uno)
    largo_cadena_dos = len(cadena_dos)
    retorno = True
    
    if largo_cadena_uno != largo_cadena_dos:
        retorno = False
    else:
        for i in range(largo_cadena_uno):
            caracter_cadena_uno = cadena_uno[i]
            caracter_cadena_dos = cadena_dos[i]
            caracter_ascii_uno = ord(caracter_cadena_uno)
            caracter_ascii_dos = ord(caracter_cadena_dos)
            
            if caracter_ascii_uno != caracter_ascii_dos:
                retorno = False
                break
    return retorno
            
        
    
        
cadena = "mariano fernandez"
cadena_dos = "El origen del gen"

print(cadena.capitalize())
print(cadena.title())
print(cadena_dos.count("gen"))