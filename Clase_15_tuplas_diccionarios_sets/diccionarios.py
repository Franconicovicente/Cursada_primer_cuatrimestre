#Diccionarios -> Nos permite estructurar de una forma más amigable un conjunto de información.

#Declaración

# mi_diccionario = dict([
#     ("nombre","Mariano"),
#     ("edad",40),
#     ("dni",22222222)
# ])

# mi_diccionario = {
#     "nombre":"Mariano",
#     "edad":40,
#     "dni":22222222
# }

# mi_diccionario = {}
# mi_diccionario["nombre"] = "Mariano"
# mi_diccionario["edad"] = 40
# mi_diccionario["dni"] = 22222222

#Acceso
#Todos los elementos
#print(mi_diccionario)

#Uno por uno
#Nombre
# print(mi_diccionario["nombre"])
#Edad
# print(mi_diccionario["edad"])
#DNI
#print(mi_diccionario["dni"])

# for clave in mi_diccionario:
#     print(f"{clave.capitalize()} : {mi_diccionario[clave]}")

#KEYS()

# mi_diccionario = {
#     "nombre":"Mariano",
#     "edad":40,
#     "dni":22222222
# }

# claves = mi_diccionario.keys()
# print(type(claves))
# print(claves)

# for clave in mi_diccionario.keys():
#     print(clave)

#Equivalente a lo visto anteriormente
# for clave in mi_diccionario:
#     print(f"{clave.capitalize()} : {mi_diccionario[clave]}")

#Útil para verificar si una clave específica existe en el diccionario.  
#print("nombre" in mi_diccionario.keys()) -> True
#print("jose" in mi_diccionario.keys()) -> False

#Pese a su implementación, el metodo keys es equivalente a recorrer el diccionario.
#print("nombre" in mi_diccionario)

#VALUES() -> Extrae solo los valores de mi diccionario al recorrerlos

# mi_diccionario = {
#     "nombre":"Mariano",
#     "edad":40,
#     "dni":22222222
# }

# for clave in mi_diccionario:
#     print(clave)

# for valor in mi_diccionario.values():
#     print(valor)
    
#print("Mariano" in mi_diccionario.values())

#ITEMS() -> Me permite recorrer la clave y el valor de mi diccionario, ideal para mostrar más fácil mis datos

mi_diccionario = {
    "nombre":"Mariano",
    "edad":40,
    "dni":22222222
}

#Si al metodo items lo convertimos en lista me genera una matriz de tuplas con la información del diccionario.
# items = list(mi_diccionario.items())
# for fil in range(len(items)):
#     items[fil] = list(items[fil])
# print(items)

# for clave,valor in mi_diccionario.items():
#     print(f"{clave} : {valor}")