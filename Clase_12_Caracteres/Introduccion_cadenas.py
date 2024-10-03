#Cadenas de caracteres
#Una cadena de manera algoritmica es como una lista de caracteres (En lenguajes como C lo expresamos en un array de caracteres) que guardar un conjunto de caracteres

#palabra = "Hola"
#De manera algoritmica la variable palabra se expresaria de manera similar a esto
#lista_palabra = ['H','o','l','a']

#Indexacion

cadena = "Hola Mundo"
largo_cadena = len(cadena)
print(f"La cadena tiene {largo_cadena} caracteres")

# #Accedo al primer caracter de mi cadena
# print(cadena[0])
# #Accedo al segundo caracter de mi cadena
# print(cadena[1])
# #Accedo al ultimo caracter de mi cadena
# #print(cadena[-1])#SOLO FUNCIONA EN PYTHON
# #print(cadena[9])
# print(cadena[largo_cadena - 1])

#Si paso de rango sucede lo mismo que en las lista, me tira una excepcion
#print(cadena[10])

#INMUTABILIDAD

# #Quiero cambiar la H por una A
# cadena[9] = "A"#No se puede por la inmutabilidad
# print(cadena)

#Que pasa si quiero modificar un caracter de mi cadena

#Alternativa 1: Creo una cadena nueva con la modificacion que queria hacer

#Si puedo asignarle a la variable cadena una nueva cadena
# cadena = "Aola Mundo"#No se puede por la inmutabilidad
# print(cadena)

#Alternativa 2: Convierto la cadena a una lista la modifico y la vuelvo a convertir en cadena

# lista_cadena = list(cadena)
# lista_cadena[0] = "A" #Modifico el primer elemento por una A
# cadena = ""

# #Concatenamos 
# for caracter in lista_cadena:
#     cadena += caracter

# print(cadena)

#SLICING

#Tengo la cadena Hola Mundo puedo separar Hola y Mundo con un Slincing
# print(cadena[0:4])#Hola
# print(cadena[5:10])#Mundo

# lista_numeros = [1,3,5,7,9]

# print(lista_numeros[1:4])

#CONCATENACION

# cadena = "Hola"
# # cadena_dos = "Hola"

# print(id(cadena))

# cadena +=" Mundo"
# print(id(cadena))

# print(id(cadena_dos))

#COMPARACION

nombre = "Mariano"
nombre_dos = "Jose"

print(nombre == nombre_dos)
print(nombre != nombre_dos)
print(nombre > nombre_dos)
print(nombre < nombre_dos)

# cadena = "Hola Mundo "

# print(cadena * 5)

# cadena = "Hola a todos"

# contador_letras_o = 0

# #For in range
# for i in range(len(cadena)):
#     if cadena[i] == "o":
#         contador_letras_o +=1
#     # print(f"{cadena[i]}")
    

# #Foreach
# for caracter in cadena:
#     if caracter == "o":
#         contador_letras_o +=1
    
# print(f"La cadena tiene {contador_letras_o} letras o")
