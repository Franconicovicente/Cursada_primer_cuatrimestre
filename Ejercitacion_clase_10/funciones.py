import random
import os
I_NOMBRE = 0
I_APELLIDO = 1
I_DNI = 2
I_GENERO = 3
I_NOTA_FINAL = 4

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    '''
    Pedir un numero para el menu.
    '''
    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))

    return numero

def mostrar_matriz(matriz:list)->None:
    for fil in range(len(matriz)):#PARA LAS FILAS,largo de la lista es la cantidad de filas
        for colum in range(len(matriz[fil])):#PARA LAS COLUMNAS,va iterando cada valor en cada fila
            print(matriz[fil][colum], end=" ")
        print(" ")

def inicializar_matriz(cant_filas:int, cant_columnas:int,valor_inicial)->list:
    matriz = []
    for _ in range(cant_filas):
        fila =[valor_inicial] * cant_columnas
        matriz += [fila]
    return matriz

matriz_alumnos = inicializar_matriz(2, 5, 0)

def cargar_nombre_apellido(mensaje, mensaje_error):
    nombre = input(mensaje)
    while len(mensaje) < 3:
        nombre = input(mensaje_error)
    return nombre

def cargar_entero(mensaje, mensaje_error, min, max):
    numero = int(input(mensaje))
    while numero < min or numero > max:
        numero = int(input(mensaje_error))
    return numero


def cargar_alumnos(matriz_alumnos):
    '''
    Pide los datos del alumno y los carga a la lista matriz_alumnos.
    '''
    for i in range(len(matriz_alumnos)):
        nombre = cargar_nombre_apellido("Ingrese el nombre del alumno: ", "El nombre debe tener mas de 3 caracteres. Reingrese el nombre del alumno: ")

        apellido = cargar_nombre_apellido("Ingrese el apellido del alumno: ", "El apellido debe tener mas de 3 caracteres. Reingrese el nombre del alumno: ")

        dni = cargar_entero("Ingrese el dni del alumno: ", "El DNI debe tener entre 6 y 9 caracteres. Reingrese el dni del alumno: ", 11111111, 99999999)

        genero = input("Ingrese el genero del alumno: ")
        while genero != "M" and genero != "F" and genero != "NB":
            genero = input("Genero no valido. Reingrese el genero del alumno: ")
        nota_final = cargar_entero("Ingrese el nota del alumno: ", "La nota debe ser entre 1 y 10. Reingrese el nota del alumno: ", 1, 10)
        matriz_alumnos[i][I_NOMBRE] = nombre
        matriz_alumnos[i][I_APELLIDO] = apellido
        matriz_alumnos[i][I_DNI] = dni
        matriz_alumnos[i][I_GENERO] = genero
        matriz_alumnos[i][I_NOTA_FINAL] = nota_final

def mostrar_alumno(lista: list) -> list:
    '''
    Muestra los datos del alumno en un formato mas simple para el usuario
    '''
    for fil in range(len(lista)):
        print(f"nombre: {lista[fil][I_NOMBRE]}")
        print(f"apellido: {lista[fil][I_APELLIDO]}")
        print(f"dni: {lista[fil][I_DNI]}")
        print(f"genero: {lista[fil][I_GENERO]}")
        print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")

#mostar_alumno(matriz_alumnos)

#3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
#4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
#5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
def mostrar_alumno_notas(lista: list, min: int, max: int, mensaje: str, mensaje_error: str) -> list:
    '''
    Muestra los alumnos promocionados, aprobados y desaprobados.
    '''
    print(mensaje)
    flag = False
    for fil in range(len(lista)):
        if lista[fil][I_NOTA_FINAL] >= min and lista[fil][I_NOTA_FINAL] <= max:
            print(f"nombre: {lista[fil][I_NOMBRE]}")
            print(f"apellido: {lista[fil][I_APELLIDO]}")
            print(f"dni: {lista[fil][I_DNI]}")
            print(f"genero: {lista[fil][I_GENERO]}")
            print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")
            flag = True
    
    if flag == False:
        print(mensaje_error)

#mostrar_alumno_notas(matriz_alumnos, 6, 10, "Alumnos promocionados: ", "No hay alumnos promocionados")
#mostrar_alumno_notas(matriz_alumnos, 4, 5, "Alumnos aprobados: ", "No hay alumnos aprobados.")
#mostrar_alumno_notas(matriz_alumnos, 1, 3, "Alumnos desaprobados: ", "No hay alumnos desaprobados.")

#6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.

def mostrar_alumno_dni(lista:list):
    '''
    Se ingresa el DNI y si se encuentra muestra todos los datos del alumno.
    En caso de no encontrarse devuelve que no se encontró
    '''
    dni = cargar_entero("Ingrese el dni del alumno: ", "El DNI debe tener entre 6 y 9 caracteres. Reingrese el dni del alumno: ", 11111111, 99999999)
    flag = False
    for fil in range(len(lista)):
        if lista[fil][I_DNI] == dni:
            print(f"nombre: {lista[fil][I_NOMBRE]}")
            print(f"apellido: {lista[fil][I_APELLIDO]}")
            print(f"dni: {lista[fil][I_DNI]}")
            print(f"genero: {lista[fil][I_GENERO]}")
            print(f"nota final: {lista[fil][I_NOTA_FINAL]}\n")
            flag = True
    if flag == False:
        print('No se encuentra en el sistema...')
    
#7.La cantidad de alumnos promocionados, aprobados y desaprobados

def contar_alumnos_por_nota(lista: list, min: int, max: int) ->list:
    '''
    Cuenta los alumnos promocionados, aprobados y desaprobados
    '''
    contador_alumnos = 0
    for fil in range(len(lista)):
        if lista[fil][I_NOTA_FINAL] >= min and lista[fil][I_NOTA_FINAL] <= max:
            contador_alumnos += 1

    return contador_alumnos

def mostrar_alumnos():
    '''
    Muestra los alumnos que promocionaron, aprobaron y desaprobaron.
    '''
    print(f"La cantidad de alumnos promocionados: {contar_alumnos_por_nota(matriz_alumnos, 6, 10)}")
    print(f"La cantidad de alumnos aprobados: {contar_alumnos_por_nota(matriz_alumnos, 4, 5)}")
    print(f"La cantidad de alumnos desaprobados: {contar_alumnos_por_nota(matriz_alumnos, 1, 3)}")

def calcular_promedio_notas(lista:list)->float:
    '''
    Calcula el promedio de las notas de todos los alumnos
    '''
    nota = 0
    contador_notas = 0
    contador_alumnos_superan_promedio = 0
    for fil in range(len(lista)):
        nota += lista[fil][I_NOTA_FINAL] 
        contador_notas += 1 
        promedio_notas = nota / contador_notas
        if nota > promedio_notas:
            contador_alumnos_superan_promedio += 1

    print(f"El promedio de notas de los estudiantes es de: {promedio_notas}")

    return contador_alumnos_superan_promedio

def calcular_promedio_notas_masculinos(lista:list)->float:
    '''
    Se calcula el promedio de nota de SOLO los alumnos masculinos.
    En caso de no ingresarse, devuelve que no hubieron masculinos ingresados.
    '''
    nota = 0
    contador_notas = 0
    bandera = True
    for fil in range(len(lista)):
        if lista[fil][I_GENERO] == "M":
            nota += lista[fil][I_NOTA_FINAL] 
            contador_notas += 1 
            promedio_notas = nota / contador_notas
            bandera = False

    if bandera == True:
        print("No hay estudiantes masculinos, no se pudo calcular la nota...")
    else:
        print(f"El promedio de notas de los estudiantes masculinos es de: {promedio_notas}")

#10.El porcentaje de alumnos de cada género
def contar_alumnos(lista:list)->float:
    '''
    Cuenta los alumnos por genero y devuelve un porcentaje de cuantos hay de cada uno
    '''
    contador_masculinos = 0
    contador_femeninos = 0
    contador_no_binarios = 0
    contador_alumnos = 0
    for fil in range(len(lista)):
        if lista[fil][I_GENERO] == "M":
            contador_masculinos += 1
        elif lista[fil][I_GENERO] == "F":
            contador_femeninos += 1
        else:
            contador_no_binarios += 1     
        
        contador_alumnos += 1

    
    porcentaje_masculinos = round((contador_masculinos * 100) / contador_alumnos, 2)
    porcentaje_femeninos = round((contador_femeninos * 100) / contador_alumnos, 2)
    porcentaje_no_binarios= round((contador_no_binarios * 100) / contador_alumnos, 2)

    mensaje = f"El porcentaje de masculinos es de {porcentaje_masculinos}%\nEl porcentaje de femeninos es de {porcentaje_femeninos}%\nEl porcentaje de no binarios es de {porcentaje_no_binarios} "

    return mensaje

# 11.Mostrar el alumno o los alumnos con mayor nota

def calcular_mayor_nota(lista:list)->str:
    '''
    Calcula la nota maxima y muestra el nombre del alumno
    '''
    nota_maxima = lista[0][4]
    mejor_alumno = lista[0][0]

    for fil in range(len(lista)):
        nota_alumno = lista[fil][4]
        if nota_alumno > nota_maxima:
            nota_maxima = nota_alumno
            mejor_alumno = lista[fil][0]

    retorno = f"El alumno con mayor nota es {mejor_alumno}"
    return retorno

# 12.Mostrar la cantidad de alumnos que superan la nota promedio

def mostrar_alumnos_nota_promedio(lista:list)->str:
    '''
    Muestra los alumnos que superan la nota promedio.
    '''
    print(f"La cantidad de alumnos que superan el promedio es de {calcular_promedio_notas(matriz_alumnos)}")

