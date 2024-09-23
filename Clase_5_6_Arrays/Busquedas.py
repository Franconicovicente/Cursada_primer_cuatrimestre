nombre_ingresado = input("Ingrese un nombre: ")


lista_nombres = ["Franco", "Lucia", "Sandra", "Pedro"]
bandera_encontro_nombre = True

for i in range (len(lista_nombres)):
    if lista_nombres[i] == nombre_ingresado:
        bandera_encontro_nombre = False
        break

if bandera_encontro_nombre == False:
    print("Encontró el nombre")
else:
    print("El nombre no fue encontrado")

lista_profes = ["Mariano", "Renato", "German", "David"]
lista_alumnos = ["Jose", "Juan", "Renato", "Miguel"]

for nombre_profe in lista_profes:
    for nombre_alumno in lista_alumnos:
        if nombre_profe == nombre_alumno:
            print(f"El profe {nombre_profe} también fue alumno")
