#CONJUNTOS -> Al igual que los conjuntos que vimos en matematica, el tipo de dato set me permite representarlos en mi código.

# mi_conjunto = {"Matias",9,2,14.98,1,"Jose",14,33,-12,"Mariano",1,1,14,"Mariano",9,3.14,9,3.14,5}
# print(mi_conjunto)

# set_datos = {3,5,9,5,3,4,3}
# print(type(set_datos))
# print(set_datos)

#add() 

# mi_tupla = (1,9,5,9,9)
# set_datos = {3,5,9,5,3,4,3}
# set_datos = set() # Instancia un set vacio
# set_datos = set(mi_tupla) #Tambien me permite convertir una tupla o lista en un set.

# print(f"Antes del add: {set_datos}")

# #set_datos.add(9)
# # set_datos.add(10)
# # set_datos.add(33)
# # set_datos.add("Mariano")

# print(f"Despues del add: {set_datos}")

#REMOVE 

# set_datos = {3,5,9,5,3,4,3}
# print(f"Antes del remove: {set_datos}")
# set_datos.remove(9)
# #set_datos.remove(14) -> DA ERROR
# print(f"Despues del remove: {set_datos}")

#DISCARD

# set_datos = {3,5,9,5,3,4,3}
# print(f"Antes del discard: {set_datos}")
# #set_datos.discard(9)
# #set_datos.discard(14) #-> NO DA ERROR
# print(f"Despues del discard: {set_datos}")

#POP -> Elimina un elemento aleatorio (Normalmente el primero) y lo devuelve

# set_datos = {"Matias",9,2,14.98,1,"Jose",14,33,-12,"Mariano",1,1,14,"Mariano",9,3.14,9,3.14,5}

# print(f"Antes del pop: {set_datos}")
# elemento = set_datos.pop()
# print(f"Elemento: {elemento}")
# print(f"Despues del pop: {set_datos}")

#CLEAR

# set_datos = {3,5,9,5,3,4,3}

# print(f"Antes del clear: {set_datos}")
# set_datos.clear()
# print(f"Despues del clear: {set_datos}")

#UNION -> Realiza la union entre dos conjuntos

# conjunto_uno = {1,2,3}
# conjunto_dos = {3,4,5}

# print(conjunto_uno)
# print(conjunto_dos)

# conjunto_resultado = conjunto_uno.union(conjunto_dos)
# print(conjunto_resultado)

#INTERSECTION -> Realiza la intercepción entre dos conjuntos

# conjunto_uno = {1,2,3}
# conjunto_dos = {3,4,5}

# print(conjunto_uno)
# print(conjunto_dos)

# conjunto_resultado = conjunto_uno.intersection(conjunto_dos)
# print(conjunto_resultado)

#UPDATE

# set_datos = {1,2,3}
# set_datos_dos = {8,9,10}

# lista = [2,5,9]
# tupla = (5,9,11)

# print(f"Antes del update {set_datos}")
# set_datos.update(set_datos_dos)
# set_datos.update(lista)
# set_datos.update(tupla)
# print(f"Despues del update {set_datos}")

# lista_nombres = ["Mariano","Jose","Juan","Mariano","Juan","Maria"]
# print(f"Antes de la conversión: {lista_nombres}")
# set_nombres = set(lista_nombres)
# lista_nombres = list(set_nombres)
# print(f"Despues de la conversión: {lista_nombres}")



