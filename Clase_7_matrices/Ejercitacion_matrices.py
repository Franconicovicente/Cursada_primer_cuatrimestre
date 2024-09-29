from Funciones import *
'''
Ejercitación Clase 9 (Matrices)
Nota 1:Se debería realizar la función inicializar_matriz que está en la diapositiva para definir la longitud de la matriz_resultado que va a ser usada en cada una de las funciones 

Nota 2: En todas las funciones en caso de recibir por parámetro en la llamada elementos que no son de tipo lista devolver una lista vacía que me indica que algo en la función falló.

1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con la suma de las mismas.
Tanto la matriz A como la matriz B deben tener la misma cantidad de filas y columnas, validar que eso ocurra (Podemos hacer otra función que se encargue de esto) , caso contrario retornar una lista vacía en caso de que no se cumpla.
2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, la función devuelve una matriz nueva con el resultado de la multiplicación.
3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta
4. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz transpuesta (Donde las columnas y las filas se intercambian)
5. Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de filas de la matriz B , si no se cumple devolver una lista vacía.
Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B



'''
        

# 1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con la suma de las mismas.

# matriz_a = [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#             ]
# matriz_b = [
#             [1,2,3],
#             [4,5,6],
#             [7,8,9]
#             ]

# resultado = sumar_matrices(matriz_a, matriz_b)
# print("Suma de las matrices:")
# print("")
# mostrar_matriz(resultado)
# print("")

# 2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, la función devuelve una matriz nueva con el resultado de la multiplicación.

# matriz = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#         ]

# escalar = 3

# resultado = realizar_producto(matriz,escalar)
# print("Resultado de la multiplicación: ")
# mostrar_matriz(resultado)


# 3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta

# matriz = [
#         [1,2,3],
#         [4,5,6]
#             ]

# escalar = -1

# resultado = realizar_producto(matriz,escalar)
# print("El opuesto de la matriz es: ")
# mostrar_matriz(resultado)

# 4. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz transpuesta (Donde las columnas y las filas se intercambian)

# matriz = [
#         [1,2,3],
#         [4,5,6],
#         [7,8,9]
#             ]


# resultado = calcular_traspuesta(matriz)

# print("La traspuesta de la matriz es: ")
# mostrar_matriz(resultado)

# 5. Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
# Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de filas de la matriz B , si no se cumple devolver una lista vacía.
# Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B

matriz_a = [
            [5,4],
            [3,1],
            [12,7]
            ]

matriz_b = [
            [1,5,6,7],
            [1,3,5,2]            
            ]

resultado = calcular_producto(matriz_a, matriz_b)

print("El producto de las matrices es: ")

mostrar_matriz(resultado)