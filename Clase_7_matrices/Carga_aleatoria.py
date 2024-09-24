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

#Carga aleatoria

seguir = "S"

while seguir == "S":
    #Pedimos los indices de la fila y columna
    fila = int(input("Ingrese numero de fila: "))
    #VALIDAR RANGO
    columna = int(input("Ingrese numero de columna: "))
    #VALIDAR RANGO




    
    dato = int(input("Ingrese el numero que quiere ingresar: "))
    #Guardo el numero
    matriz[fila][columna] = dato
    seguir = input("Desea seguir cargando datos? S/N: ")

print("DESPUES DE LA CARGA")
mostrar_matriz(matriz)
print("")