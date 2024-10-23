def inicializar_matriz(cant_filas:list,cant_columnas:list,valor_inicial:any)-> list:

    
    '''
    
    '''
    matriz = []
    for fil in range(cant_filas):
        fila =  [valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz


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

def validar_cantidad_filas_columnas(matriz_a:list,matriz_b:list):
    '''
    
    '''
    if len(matriz_a) == len(matriz_b) and len(matriz_a[0]) == len(matriz_b[0]):
        return True
    else:
        print("Las matrices son distintas")


# 1. Realizar una función que permita realizar la suma entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con la suma de las mismas.
# Tanto la matriz A como la matriz B deben tener la misma cantidad de filas y columnas, validar que eso ocurra (Podemos hacer otra función que se encargue de esto) , caso contrario retornar una lista vacía en caso de que no se cumpla.

# matriz_a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]    
#     ]

# matriz_b = inicializar_matriz(2,3,1)

# def sumar_matrices(matriz_a:list,matriz_b:list) -> list:
#     '''
    
#     '''
    
#     validar_cantidad_filas_columnas(matriz_a,matriz_b)
    
#     matriz_c = inicializar_matriz(len(matriz_a),len(matriz_a[0]),0)
#     for fil in range(len(matriz_a)):
#         for col in range(len(matriz_a[fil])):
#             matriz_c[fil][col] = matriz_a[fil][col] + matriz_b[fil][col]

#     return matriz_c


# resultado = sumar_matrices(matriz_a,matriz_b)
# mostrar_matriz(resultado)

# 2. Realizar una función que permita realizar el producto (multiplicación) de una matriz por un escalar (número entero) , la función deberá recibir la matriz a la que se le quiera realizar el producto, el número entero que multiplique a está matriz, la función devuelve una matriz nueva con el resultado de la multiplicación.

# matriz = inicializar_matriz(2,2,2)

# def multiplicar_matriz_y_num_entero(matriz:list):
#     '''
    
#     '''

#     numero_entero = int(input("Ingrese el numero por el que se va a multiplicar la matriz: "))

#     matriz_nueva = inicializar_matriz(2,2,0)

#     for fil in range(len(matriz)):
#         for col in range(len(matriz[fil])):
#             matriz_nueva[fil][col] = matriz[fil][col] * numero_entero
    
#     return matriz_nueva


# resultado = multiplicar_matriz_y_num_entero(matriz)

# mostrar_matriz(resultado)

# 3. Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz opuesta

# matriz = inicializar_matriz(2,2,7)

# def calcular_matriz_opuesta(matriz:list) -> list:
#     '''
    
#     '''
#     matriz_opuesta = inicializar_matriz(2,2,0)
#     for fil in range(len(matriz)):
#         for col in range(len(matriz[fil])):
#             matriz_opuesta[fil][col] = -1 * matriz[fil][col]

#     return matriz_opuesta


# resultado = calcular_matriz_opuesta(matriz)
# mostrar_matriz(resultado)

#  Realizar una función que reciba una matriz , calcule y retorne en una nueva lista su matriz traspuesta (Donde las columnas y las filas se intercambian)

# print("Matriz comun: ")
# matriz = inicializar_matriz(3,2,2)
# mostrar_matriz(matriz)
# def calcular_matriz_traspuesta(matriz:list)-> list:
#     '''
    
#     '''
#     matriz_traspuesta = inicializar_matriz(2,3,2)
#     for fil in range(len(matriz)):
#         for col in range(len(matriz[fil])):
#             matriz_traspuesta[col][fil] = matriz[fil][col]

#     return matriz_traspuesta

# print("Matriz traspuesta:")
# resultado = calcular_matriz_traspuesta(matriz)
# mostrar_matriz(resultado)

#  Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
# Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de filas de la matriz B , si no se cumple devolver una lista vacía.
# Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B

matriz_a = inicializar_matriz(2,3,2)

matriz_b = inicializar_matriz(3,2,2)


def multiplicar_matrices(matriz_a:list,matriz_b:list) -> list:
    '''
    
    '''
    matriz_resultante = inicializar_matriz(len(matriz_a),len(matriz_b[0]),0)

    if len(matriz_a[0]) == len(matriz_b):
        for fil in range(len(matriz_a)):
            for col in range(len(matriz_b[0])):
                for fil_b in range(len(matriz_b)):
                    matriz_resultante[fil][col] += matriz_a[fil][fil_b] * matriz_b[fil_b][col]

    return matriz_resultante

resultado = multiplicar_matrices(matriz_a,matriz_b)

mostrar_matriz(resultado)