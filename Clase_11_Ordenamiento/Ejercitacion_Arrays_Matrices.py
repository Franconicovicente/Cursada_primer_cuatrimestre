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
'''
6. Crear una función para ordenar por apellido una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un   parámetro que se le envíe.

7. Crear una función para ordenar por nombre una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un parámetro que se le envíe.

8. Vamos a guardar la información de un jugador de fútbol en una matriz con las siguientes columnas (nombre,apellido, partidos,goles,asistencias) 
debemos:

1-Mostrar tabla de goleadores
2-Mostrar tabla de asistencias
3-Los 5 jugadores con más partidos.
4-Mostrar top 3 jugadores con más goles 
5-Mostrar top 3 jugadores con menos asisten
'''

# 6. Crear una función para ordenar por apellido una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un   parámetro que se le envíe.

# matriz_apellidos = [
#     ["Pedro", "Pascal"],
#     ["Franco", "Vicente"]
# ]

# I_APELLIDO = 1

# parametro = int(input("Ingrese numero 1 para ordenar de Z-A.\nIngrese numero 2 para ordenar de A-Z.\nSu respuesta: "))
# def ordenar_apellido(lista_anidada:list,parametro:int) ->list:
#     '''
    
#     '''
#     for fil_izq in range(len(lista_anidada)-1):
#         for fil_der in range(fil_izq + 1, len(lista_anidada)):
#             if parametro == 1:
#                 if lista_anidada[fil_izq][I_APELLIDO] < lista_anidada[fil_der][I_APELLIDO]:
#                     #Cuando hay un intercambio, lo que va a ocurrir es que se va a intercambiar el alumno COMPLETO
#                     aux = lista_anidada[fil_izq]
#                     lista_anidada[fil_izq] = lista_anidada[fil_der]
#                     lista_anidada[fil_der] = aux
#             elif parametro == 2:
#                 if lista_anidada[fil_izq][I_APELLIDO] > lista_anidada[fil_der][I_APELLIDO]:
#                 #Cuando hay un intercambio, lo que va a ocurrir es que se va a intercambiar el alumno COMPLETO
#                     aux = lista_anidada[fil_izq]
#                     lista_anidada[fil_izq] = lista_anidada[fil_der]
#                     lista_anidada[fil_der] = aux
    
#     return lista_anidada

# ordenar_apellido(matriz_apellidos,parametro)

# mostrar_matriz(matriz_apellidos)

# # 7. Crear una función para ordenar por nombre una matriz que tenga dos columnas (nombre-apellido) de la A-Z o viceversa dependiendo de un parámetro que se le envíe.

# matriz_nombres = [
#     ["Pedro", "Pascal"],
#     ["Franco", "Vicente"],
#     ["Bob", "Byron"]
# ]

# I_NOMBRE = 0

# parametro = int(input("Ingrese numero 1 para ordenar de Z-A.\nIngrese numero 2 para ordenar de A-Z.\nSu respuesta: "))
# def ordenar_nombre(lista_anidada:list,parametro:int) ->list:
#     '''
    
#     '''
#     for fil_izq in range(len(lista_anidada)-1):
#         for fil_der in range(fil_izq + 1, len(lista_anidada)):
#             if parametro == 1:
#                 if lista_anidada[fil_izq][I_NOMBRE] < lista_anidada[fil_der][I_NOMBRE]:
#                     #Cuando hay un intercambio, lo que va a ocurrir es que se va a intercambiar el alumno COMPLETO
#                     aux = lista_anidada[fil_izq]
#                     lista_anidada[fil_izq] = lista_anidada[fil_der]
#                     lista_anidada[fil_der] = aux
#             elif parametro == 2:
#                 if lista_anidada[fil_izq][I_NOMBRE] > lista_anidada[fil_der][I_NOMBRE]:
#                 #Cuando hay un intercambio, lo que va a ocurrir es que se va a intercambiar el alumno COMPLETO
#                     aux = lista_anidada[fil_izq]
#                     lista_anidada[fil_izq] = lista_anidada[fil_der]
#                     lista_anidada[fil_der] = aux
    
#     return lista_anidada

# ordenar_nombre(matriz_nombres,parametro)

# mostrar_matriz(matriz_nombres)

# 8. Vamos a guardar la información de un jugador de fútbol en una matriz con las siguientes columnas (nombre,apellido, partidos,goles,asistencias) 
# debemos:

# 1-Mostrar tabla de goleadores
# 2-Mostrar tabla de asistencias
# 3-Los 5 jugadores con más partidos.
# 4-Mostrar top 3 jugadores con más goles 
# 5-Mostrar top 3 jugadores con menos asisten
# '''

matriz_jugadores = [
    ["Lionel", "Messi", 10, 30, 5],
    ["Cristiano", "Ronaldo", 5, 3, 2],
    ["Ronaldinho", "Gaucho", 30, 20, 10],
    ["Sergio", "Aguero", 50, 5, 30],
    ["Angel", "Di Maria", 20, 30, 5]
]
I_GOLES = 3
I_ASISTENCIAS = 4
I_PARTIDOS = 2

# 1-Mostrar tabla de goleadores, 2-Mostrar tabla de asistencias, 3-Los 5 jugadores con más partidos.
def mostrar_goleadores_y_asistencias(lista:list,parametro:int)->list:
    '''
    
    '''
    if parametro == 1:
        for jugador in lista:
            print(f"{jugador[0]:<5} {jugador[1]} {jugador[2]} {jugador[I_GOLES]}")
    elif parametro == 2:
        for asistencias in lista:
            print(f"{asistencias[0]:<5} {asistencias[1]} {asistencias[2]} {asistencias[I_ASISTENCIAS]}")
    elif parametro == 3:
        for goles in lista:
            print(f"{goles[0]:<5} {goles[1]} {goles[2]} {goles[I_GOLES]}")

# def mostrar_goleadores(lista:list):
#     '''
    
#     '''
#     top_goleadores = []
#     for i in range(3):
#         max_goles = -1  
#         mejor_goleador = ""
#         indice_mejor = -1
#         for i, jugador in enumerate(lista):
#             if jugador[I_GOLES] > max_goles:
#                 max_goles = jugador[I_GOLES]
#                 mejor_goleador = jugador
#                 indice_mejor = i
#         if mejor_goleador:
#             top_goleadores.append(mejor_goleador)
#             lista[indice_mejor][I_GOLES] = -1
            

#     for jugador in top_goleadores:
#         print(f"{jugador[0]} {jugador[1]} {jugador[2]} {jugador[I_GOLES]}")


# mostrar_goleadores(matriz_jugadores)