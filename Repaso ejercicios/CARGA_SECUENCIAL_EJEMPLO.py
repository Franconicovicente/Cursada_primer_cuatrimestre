def inicializar_matriz(cant_filas:list,cant_columnas:list)-> list:
    '''
    
    '''
    matriz = []
    for fil in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz
matriz = inicializar_matriz(3,3)


for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        #Pido datos
        numero = int(input(f"Ingrese numero para la fila {fil} y columna {col}: "))
        #Lo asigno a dicha fila/columna
        matriz[fil][col] = numero