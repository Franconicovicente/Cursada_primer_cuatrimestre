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


def mostrar_datos():
    '''
    
    '''
    # resultado = cargar_alumnos(lista_datos_finales)

    print("Datos del alumno...")
    print("")
    # for resultado in lista_datos_finales:
        # print(f"Nombre: {resultado[0]}")
        # print(f"Apellido: {resultado[1]}")
        # print(f"DNI: {resultado[2]}")
        # print(f"Genero: {resultado[3]}")
        # print(f"Nota: {resultado[4]}")
        # print("")

mostrar_datos()