def mostrar_matriz(matriz:list)->None:
    '''
    
    '''
    if type(matriz) == list:
        for fil in range(len(matriz)):
        # For para las columnas
        # Cantidad columnas:
            for col in range(len(matriz[fil])):
                print(matriz[fil][col], end=" ")
            print("")
    else:
        print("No se ingresaron listas")
matriz_alumnos = [
    ["Mariano", 22222,5],
    ["Ezequiel", 33333,3],
    ["Maria", 44444,1],
    ["Jazmin", 55555,9],
    ["Pablo", 11111,7]
]


#En que columna se encuentra la nota?

I_NOTA = 2

print("Antes de ordenar: ")
mostrar_matriz(matriz_alumnos)
print("")

#Ordeno de mayor a menor

for fil_izq in range(len(matriz_alumnos)-1):
    for fil_der in range(fil_izq + 1, len(matriz_alumnos)):
        if matriz_alumnos[fil_izq][I_NOTA] < matriz_alumnos[fil_der][I_NOTA]:
            #Cuando hay un intercambio, lo que va a ocurrir es que se va a intercambiar el alumno COMPLETO
            aux = matriz_alumnos[fil_izq]

            matriz_alumnos[fil_izq] = matriz_alumnos[fil_der]
            matriz_alumnos[fil_der] = aux
