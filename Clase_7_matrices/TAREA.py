import random
# TAREA:

# Dada una matriz 3x3 (inicializada en todos ceros) Realizar un tateti en el que el jugador pueda jugar una partida contra la máquina, primero se le pedirá al jugador cara o cruz, si el jugador acierta comienza jugando sino comienza la máquina.
# Cuando el usuario juega debe elegir en que posición de la matriz cargar su jugada , cuando el jugador elija se llenará con una “X” esa posición.
# Cuando la máquina juegue elegirá una posición aleatoria de la matriz que no haya sido asignada y la llenará con una “O”.


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

matriz_tarea = inicializar_matriz(3,3)

CARA = 1
CRUZ = 2

respuesta_cara_cruz = random.randint(1,1)
respuesta_jugador = int(input("Elija un numero entre 1, (Cara) y 2, (Cruz): "))

for i in range(3):

    if respuesta_jugador == respuesta_cara_cruz:
        posicion_fila_jugador = int(input("Ingrese en que fila quiere hacer una X: "))
        while posicion_fila_jugador > 3 or posicion_fila_jugador < 1:
            posicion_fila_jugador = int(input("Error, ingrese una fila valida: "))

        posicion_columna_jugador = int(input("Ingrese en que columna quiere hacer una X: "))
        while posicion_columna_jugador > 3 or posicion_columna_jugador < 1:
            posicion_columna_jugador = int(input("Error, ingrese una columna valida: "))
        matriz_tarea[posicion_fila_jugador - 1][posicion_columna_jugador - 1] = "X"

    mostrar_matriz(matriz_tarea)

    posicion_fila_maquina = random.randint(1,3)
    while posicion_fila_maquina == posicion_fila_jugador:
        posicion_fila_maquina = random.randint(1,3)
    posicion_columna_maquina = random.randint(1,3)
    while posicion_columna_maquina == posicion_columna_jugador:
        posicion_columna_maquina = random.randint(1,3)

    matriz_tarea[posicion_fila_maquina - 1][posicion_columna_maquina - 1] = "O"

    mostrar_matriz(matriz_tarea)
