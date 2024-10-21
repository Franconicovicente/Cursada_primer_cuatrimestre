def inicializar_matriz(cant_filas:int, cant_columnas:int,valor_inicial)->list:
    matriz = []
    for _ in range(cant_filas):
        fila =[valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):#PARA LAS FILAS,largo de la lista es la cantidad de filas
        for colum in range(len(matriz[fil])):#PARA LAS COLUMNAS,va iterando cada valor en cada fila
            print(matriz[fil][colum], end=" ")
        print(" ")

matriz_bailarines = [
    [0,0,0]
]
matriz_jurado = [
    [1,2,3]
                ]

# 1. Calificar Bailarines: Se realiza una carga secuencial de todas las notas que eligió
# cada jurado de cada uno de los bailarines.
def calificar_bailarines(matriz_bailarines:list,matriz_jurado:list):
    '''
    
    '''
    for fil in range(len(matriz_bailarines)):
        for col in range(len(matriz_bailarines[fil])):
            for i in range(len(matriz_jurado[0])):
                nota = int(input(f"Nota del bailarin numero en la fila {fil+1} columna {col+1} para jurado numero {i+1}: "))
                matriz_bailarines[fil][col] += nota
    
    return matriz_bailarines

resultado = calificar_bailarines(matriz_bailarines, matriz_jurado)
mostrar_matriz(resultado)

# 2. Mostrar Notas: Muestra en un lindo formato los siguientes datos:
# Nro Participante, Nota Jurado 1,Nota Jurado 2,Nota Jurado 3,Nota Promedio:
def mostrar_matriz_bailarines(matriz:list)->None:
    for i in range(len(matriz)):
        print(f"Participante numero: {i+1}")
        notas = 0
        for j in range(len(matriz[i])):
            notas += matriz[i][j]
            promedio_notas = notas / len(matriz[i])
            print(f"Nota jurado {j+1}: {matriz[i][j]}")
            print(f"Promedio del participante {i+1}: {promedio_notas}")
        print("")



mostrar_matriz_bailarines(matriz_bailarines)

# 3. Ordenar Bailarines jurado 2: Ordena a los participantes por la mejor nota que les
# puso el jurado 2.

def ordenar_bailarines(matriz_bailarines:list):
    '''
    
    '''
    for i in range(len(matriz_bailarines) - 1):
        for j in range(i+1, len(matriz_bailarines)):
            if matriz_bailarines[j][1] < matriz_bailarines[j+1][1]:
                num_aux = matriz_bailarines[j]

                matriz_bailarines[j] = matriz_bailarines[j+1]
                matriz_bailarines[j+1] = num_aux
    
    return matriz_bailarines


resultado = ordenar_bailarines (matriz_bailarines)
print("Bailarines ordenados por la mejor nota del jurado 2:")
mostrar_matriz(resultado)

# 4. Triple 7: Encontrar y mostrar a los participantes que tengan un 7 de nota en todos los
# jurados. En caso de no haber indicar que no existen.

def encontrar_participantes(matriz:list,numero_busqueda:int):
    '''
    
    '''
    for fil in range(len(matriz)):
        for col in range(len(matriz[fil])):
            numero = matriz[fil][col]
            if numero_busqueda == numero:
                print(f"Se encontró el alumno con nota 7 en el indice {fil+1} y columna {col+1}")
                return
    print("No se encontró el alumno")



encontrar_participantes(matriz_bailarines, 7)

# 5. Jurado malo: Muestra a todos los bailarines que fueron aplazados por el jurado 3
# (Aplazo seria nota menor 4)

def mostrar_aplazados(matriz:list,max:int):
    '''
    
    '''
    bandera_aplazados = False
    print("Bailarines aplazados por el jurado 3:")
    for fil in range(len(matriz)):
            if matriz[fil][2] < max:
                print(f"Participante {fil + 1}: Nota: {matriz[fil][2]}")
                bandera_aplazados = True    

                
    if bandera_aplazados == False:
        print("No hay aplazados")


mostrar_aplazados(matriz_bailarines, 4)


