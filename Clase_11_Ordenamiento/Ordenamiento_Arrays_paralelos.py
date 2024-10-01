# No recomendado... Muy tedioso

array_nombres = [["Mariano","Jazmin","Ezequiel"]] 

array_legajos = [[22222,33333,44444]]

array_notas = [[5,9,1]]

print("Antes de ordenar: ")
for i in range(len(array_nombres)):
    print(f"Nombre: {array_nombres[i]}")
    print(f"Legajo: {array_legajos[i]}")
    print(f"Notas: {array_notas[i]}")

for i in range(len(array_nombres)-1):
    for j in range(i+1,len(array_nombres)):
        if array_notas[i] < array_notas[j]:
            aux_nota = array_notas[i]
            array_notas[i] = array_notas[j]
            array_notas[j] = aux_nota

            aux_nombre = array_nombres[i]
            array_nombres[i] = array_nombres[j]
            array_nombres[j] = aux_nombre

            aux_legajo = array_legajos[i]
            array_legajos[i] = array_legajos[j]
            array_legajos[j] = aux_legajo


# Ordenar arrays paralelos es ineficiente y no se puede modularizar en funciones
