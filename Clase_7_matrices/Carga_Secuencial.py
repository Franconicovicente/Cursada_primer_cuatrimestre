def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):
    # For para las columnas
    # Cantidad columnas:
        for col in range(len(matriz[fil])):
            print(matriz[fil][col], end=" ")
        print("")

def inicializar_matriz(cant_filas:list,cant_columnas:list)-> list:
    '''
    
    '''
    matriz = []
    for fil in range(cant_filas):
        fila = [0] * cant_columnas
        matriz += [fila]
    return matriz


matriz = inicializar_matriz(3,3) # Creo una matriz de 3x3

print("ANTES DE LA CARGA")
mostrar_matriz(matriz)
print("")

#Carga secuencial

for fil in range(len(matriz)):
    for col in range(len(matriz[fil])):
        #Pido datos
        numero = int(input(f"Ingrese numero para la fila {fil} y columna {col}: "))
        #Lo asigno a dicha fila/columna
        matriz[fil][col] = numero


print("DESPUES DE LA CARGA")
mostrar_matriz(matriz)
print("")