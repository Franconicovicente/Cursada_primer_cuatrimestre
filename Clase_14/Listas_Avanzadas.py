#APPEND -> Agrega un elemento al final de la lista.

# lista_numeros = [1,3,5]

# print(f"Antes del append {lista_numeros}")
# lista_numeros.append(10)
# print(f"Después del append {lista_numeros}")

#INSERT -> Agrega un elemento en la posición que yo le indique.

# lista_numeros = [1,3,5]

# print(f"Antes del insert {lista_numeros}")

#Quiero agregar un elemento al principio de mi lista
# lista_numeros.insert(0,10)
#Quiero agregar un elemento en el medio de mi lista
#lista_numeros.insert(1,10)
#Quiero agregar un elemento al final de mi lista -> Igual al append()
# largo_lista = len(lista_numeros)
# lista_numeros.insert(3,10)
# lista_numeros.insert(largo_lista,10)
# lista_numeros.insert(9999999999,10)

# print(f"Despues del insert {lista_numeros}")

#EXTEND -> Permite unir dos listas en una.

# lista_nombres_uno = ["Mariano","German","Daniela"]
# lista_nombres_dos = ["Carlos","Pedro"]

# print(f"Lista 1 antes del extend {lista_nombres_uno}")
# print(f"Lista 2 antes del extend {lista_nombres_dos}")

# #lista_nombres_uno.extend(lista_nombres_dos)
# #lista_nombres_dos.extend(lista_nombres_uno)
# #lista_nombres_uno.extend(lista_nombres_uno)

# print(f"Lista 1 despues del extend {lista_nombres_uno}")
# print(f"Lista 2 despues del extend {lista_nombres_dos}")

#REMOVE -> Elimina la primer ocurrencia del elemento que quiera eliminar

#lista_nombres = ["Juan","Mariano","Jose","Mariano","Maria"]

#print(f"Antes del remove {lista_nombres}")
#lista_nombres.remove("Juan")
#lista_nombres.remove("Mariano")
#lista_nombres.remove("Jesus")
#print(f"Despues del remove {lista_nombres}")

#POP -> Elimina y Devuelve el elemento a eliminar

# lista_nombres = ["Mariano","Juan","Jose","Maria"]

# print(f"Antes del pop {lista_nombres}")
# elemento = lista_nombres.pop(1) #Se va a eliminar a Juan
# print(f"Elemento eliminado: {elemento}")

# respuesta = input(f"¿Estás seguro de eliminar a {elemento}? (si/no). No se puede volver atras: ")

# if respuesta == "si":
#     print("Elemento eliminado")
# else:
#     lista_nombres.insert(1,elemento)
#     print("Operacion cancelada")

# print(f"Despues del pop {lista_nombres}")

# lista_nombres = ["Mariano","Juan","Jose","Maria"]
# print(f"Antes del pop {lista_nombres}")
# elemento = lista_nombres.pop() #Se va a eliminar el último elemento
# #elemento = lista_nombres.pop(99999)#Lanza error
# print(f"Elemento eliminado: {elemento}")
# print(f"Despues del pop {lista_nombres}")

#CLEAR -> Elimina todos los elementos de mi lista, dejandola vacia

# lista_numeros = [2,5,9,11,20]
# print(f"Antes del clear {lista_numeros}")
# lista_numeros.clear()
# print(f"Despues del clear {lista_numeros}")

#INDEX -> Devuelve el indice de la primer ocurrencia del elemento especificado.

#lista_nombres = ["Mariano","Juan","Maria","Jose","Mariano"]
#indice = lista_nombres.index("Juan")#Devuelve la primer ocurrencia de Juan -> 1
#indice = lista_nombres.index("Mariano")#Devuelve la primer ocurrencia de Mariano -> 0
#indice = lista_nombres.index("Fernando")#Rompe
#indice = lista_nombres.index("Mariano",1)

#print(f"Indice {indice}")
#print(f"Elemento: {lista_nombres[indice]}")

#SORT -> El metodo sort me permite ordenar una lista

# lista_numeros = [3,1,9,5,7]

# print(f"Antes del sort: {lista_numeros}")
# #lista_numeros.sort()#Por defecto ordena de menor a mayor
# # lista_numeros.sort(reverse=True)#Cuando reverse es True, me ordena de mayor a menor
# print(f"Despues del sort: {lista_numeros}")

#REVERSE -> Invierte los elementos de mi lista

# lista_nombres = ["Mariano","Juan","Maria","Jose","Daniela"]

# print(f"Antes del reverse {lista_nombres}")
# lista_nombres.reverse()
# print(f"Despues del reverse {lista_nombres}")

# SHUFFLE -> Funcion de random que me ordena aleatoriamente una lista.
# import random

# lista_nombres = ["Mariano","Juan","Maria","Jose","Daniela"]

# print(f"Antes del shuffle {lista_nombres}")
# random.shuffle(lista_nombres)
# print(f"Despues del shuffle {lista_nombres}")

#DEL -> Palabra reservada que me permite eliminar un objeto en memoria.

# lista_nombres = ["Mariano","Juan","Maria","Jose","Daniela"]

# print(f"Antes de DEL {lista_nombres}")
# del lista_nombres #DEJA DE EXISTIR LA LISTA, SI LUEGO LA QUIERO ACCEDER COMO NO EXISTE MAS NO SE PUEDE ACCEDER
# #del lista_nombres[0] #Elimino el elemento del indice 0
# #del lista_nombres[2] #Elimino el elemento del indice 2
# #del lista_nombres[1:4]#Elimino el elemento del indice 1,2 y 3
# print(f"Despues de DEL {lista_nombres}")

#COPIAR LISTAS - SHALLOW COPY (COPIA SUPERFICIAL) -> Crea una nueva lista, con los elementos de la lista original.

#lista_numeros = [1,5,7]
# # lista_numeros_dos = lista_numeros#Yo no puedo copiar listas de esta manera
# lista_numeros_dos = lista_numeros.copy()

# print(f"Lista 1 id: {id(lista_numeros)}")
# print(f"Lista 2 id: {id(lista_numeros_dos)}")

# print(f"Lista 1 antes del append{lista_numeros}")
# print(f"Lista 2 antes del append{lista_numeros_dos}")

# lista_numeros_dos.append(10)

# print(f"Lista 1 despues del append{lista_numeros}")
# print(f"Lista 2 despues del append{lista_numeros_dos}")

#COPIAR LISTAS -> DEEP COPY Aparte de copiar los elementos de la lista en una nueva, copia los subelementos en esa nueva lista.

# import copy

# matriz_numeros = [[2,4,6],[1,5,9]]
# #matriz_numeros_dos = matriz_numeros.copy()#Shallow copy -> Solo crea un nuevo id para la matriz
# matriz_numeros_dos = copy.deepcopy(matriz_numeros)
# #Deep copy -> Crea un id nuevo para la matriz y para cada una de sus filas

# print(f"Matriz 1 id: {id(matriz_numeros)}")
# print(f"Matriz 2 id: {id(matriz_numeros_dos)}")

# print(f"Matriz 1 Fila 1 id: {id(matriz_numeros[0])}")
# print(f"Matriz 1 Fila 2 id: {id(matriz_numeros[1])}")
# print(f"Matriz 2 Fila 1 id: {id(matriz_numeros_dos[0])}")
# print(f"Matriz 2 Fila 2 id: {id(matriz_numeros_dos[1])}")


# print(f"Matriz 1 antes{matriz_numeros}")
# print(f"Matriz 2 antes{matriz_numeros_dos}")

# matriz_numeros_dos[0][0] = 0 
# matriz_numeros_dos[1][0] = 0 
# matriz_numeros_dos[1][1] = 0

# #[[0,4,6],[0,0,9]]

# print(f"Matriz 1 despues{matriz_numeros}")
# print(f"Matriz 2 despues{matriz_numeros_dos}")

#ENUMARATE -> Alternativa para recorrer la lista, guardanos el indice y el elemento.

# lista_nombres = ["Mariano","Juan","Maria","Jose","Daniela"]

# for indice, nombre in enumerate(lista_nombres):
#     print(f"Indice: {indice} Elemento: {nombre}")

#Enumerate hace lo mismo que esto
# for i in range(len(lista_nombres)):
#     print(f"Indice: {i} Elemento: {lista_nombres[i]}")

#ZIP -> Permite iterar varias listas a la vez

# lista_nombres = ["Mariano","Gonzalo","Maria","Juan","Pablo"]
# lista_apellidos = ["Fernandez","Perez","Gomez"]
# lista_edades = [20,30,40]

# for nombre,apellido,edad in zip(lista_nombres,lista_apellidos,lista_edades):
#     print(f"{nombre} {apellido} {edad} años")


