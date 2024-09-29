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

def inicializar_matriz(cant_filas:list,cant_columnas:list)-> list:

    
    '''
    
    '''
    matriz = []
    for fil in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz

def sumar_matrices(matriz_a:list,matriz_b:list)->list:
    '''
    
    '''
    retorno = []
    if type(matriz_a) == list and type(matriz_b) == list:
        if len(matriz_a) == len(matriz_b) and len(matriz_a[0]) == len(matriz_b[0]):
            matriz_c = inicializar_matriz(len(matriz_a), len(matriz_a[0]))
            for fil in range(len(matriz_a)):
                for col in range(len(matriz_a[fil])):
                    matriz_c[fil][col] = matriz_a[fil][col] + matriz_b[fil][col]
        retorno = matriz_c
    return retorno

def realizar_producto(matriz:list,escalar:int) -> list:
    '''
    '''
    retorno = []
    if type(matriz) == list and type(escalar) == int:
        matriz_resultado = inicializar_matriz(len(matriz), len(matriz[0]))
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                matriz_resultado[fil][col] = matriz[fil][col] * escalar
        retorno = matriz_resultado
    
    return retorno

def calcular_traspuesta(matriz:list) -> list:
    '''
    Calcula la traspuesta de una matriz, en caso de no haber ninguna matriz, devuelve una matriz vacia.
    '''
    retorno = []
    if type(matriz) == list:
        matriz_traspuesta = inicializar_matriz(len(matriz), len(matriz[0]))
        for fil in range(len(matriz)):
            for col in range(len(matriz[fil])):
                matriz_traspuesta[col][fil]= matriz[fil][col]
    
        return matriz_traspuesta

    return retorno


# Realizar una función que permita realizar la multiplicación entre dos matrices, recibirá una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
# Para que se pueda hacer una multiplicación entre dos matrices la cantidad de columnas de la matriz A debe ser igual a la cantidad de filas de la matriz B , si no se cumple devolver una lista vacía.
# Además el tamaño de la matriz resultante debe ser equivalente a la cantidad de filas de la matriz A y la cantidad de columnas de la matriz B

def calcular_producto(matriz_a:list,matriz_b:list)->list:
    '''
    Recibe una matriz_a y una matriz_b y devuelve una matriz resultante con el producto de las mismas.
    '''
    cant_filas = len(matriz_a)
    cant_columnas =len(matriz_b[0])
    matriz_c = inicializar_matriz(cant_filas, cant_columnas)
    retorno = []
    if type (matriz_a) == list and type (matriz_b) == list:
        if  len(matriz_a[0]) == len(matriz_b):
            for fil in range(cant_filas):#A
                for col in range(cant_columnas):#B
                    for k in range (len(matriz_b)):#FILAS DE B
                        matriz_c[fil][col] += matriz_a[fil][k] * matriz_b[k][col] 
                    
            
            retorno = matriz_c
    

    return retorno