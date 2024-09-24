# Como se muestra:
def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):
    # For para las columnas
    # Cantidad columnas:
        for col in range(len(matriz[fil])):
            print(matriz[fil][col], end=" ")
        print("")

# Un array bidimensional es una estructura de datos que contiene elementos dispuestos en filas y columnas
# formando una tabla que se conoce como matriz

# Estas matrices se las representa en python mediante listas anidadas
# Como se declaran:
matriz_a = [
            [1,5],
            [-3,6],
            [2,-1]
            ]

matriz_b = [
            [4,3,9],
            [-1,2,-5]
            ]

matriz_c = [
            [4,7,1],
            [-2,5,9],
            [5,4,-4]
            ]


# Como se accede: 

# Accedo a la primer fila de mi matriz (0)
# print(matriz_c[0])

# Accedo a la segunda fila de mi matriz (1)
# print(matriz_c[1]) 

# Accedo a la tercer fila de mi matriz (2)
# print(matriz_c[2]) 

# Accedo al elemento de la fila 1 en la columna 1:
# print(matriz_c[0][0])   # Cuando quiero acceder a un solo elemento de la matriz, 
                        # tengo que especificar no solo la fila si no la columna [Fila][Columna]


# Accedo a un elemento de la fila 3
# print(matriz_c[2][0])
# print(matriz_c[-1][0]) # --> Solo funciona en python


# Modificar matriz:

print("Matriz antes:")
mostrar_matriz(matriz_c)
print("")

matriz_c[0][0] = 5 # Cambio el elemento de la fila 1 columna 1. Antes era un 4, lo cambié por un 5
matriz_c[0][1] = 4 # Cambio el elemento de la fila 1 columna 2. Antes era un 7, lo cambié por un 4
matriz_c[1][0] = 3 # Cambio el elemento de la fila 2 columna 1. Antes era un -2, lo cambié por un 3
matriz_c[2][2] = -2 # Cambio el elemento de la fila 3 columna 3. Antes era un -4, lo cambié por un -2




print("Matriz despues:")
mostrar_matriz(matriz_c)
print("")