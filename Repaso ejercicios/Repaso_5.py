'''
Ejercitación Clase 10 (Listas Anidadas)

Debemos realizar un programa que nos permita inscribir 10 alumnos en el sysacad.
Debemos guardar la información de estos alumnos en una matriz de 10 filas y 5 columnas.
Cada fila va a guardar la información individual de cada alumno.
Cada columna guarda un dato diferente del alumno siguiendo el siguiente orden (Nombre,Apellido,DNI,Género,Nota Final)

El sistema debe pedir:

Nombre (Validar que se ingresó un str de al menos 3 caracteres)
Apellido (Validar que se ingresó un str de al menos 3 caracteres)
DNI (Número entre 6 y 8 caracteres) 
Género (M para masculino, F para femenino, NB para No Binario)
Nota Final (Número entre 1 y 10)

El sistema debe tener un menú como el siguiente (Pueden usar de base menu.py de la Calculadura por ejemplo)

Debemos cargar todo de manera algorítmica sin usar append inicializando anteriormente la matriz de alumnos con la función vista la clase anterior.

1.Ingresar 10 alumnos:Realiza lo explicado anteriormente
2.Mostrar Todos los Alumnos:Mostrar la información de cada alumno en un formato que quede lindo para el usuario
3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.
7.La cantidad de alumnos promocionados, aprobados y desaprobados
8.El promedio de nota de todos los alumnos
9.El promedio de nota de los alumnos masculinos
10.El porcentaje de alumnos de cada género
11.Mostrar el alumno o los alumnos con mayor nota
12.Mostrar la cantidad de alumnos que superan la nota promedio
13.Salir

NOTA 1: No se puede acceder de la opción 2 a la 12 si nunca se ingresó la opción 1.
NOTA 2: Modularizar cada tarea en funciones, recordar hacerlas lo más genéricas posibles.

'''

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




# Debemos guardar la información de estos alumnos en una matriz de 10 filas y 5 columnas.
# Cada fila va a guardar la información individual de cada alumno.
# Cada columna guarda un dato diferente del alumno siguiendo el siguiente orden (Nombre,Apellido,DNI,Género,Nota Final)

# El sistema debe pedir:

# Nombre (Validar que se ingresó un str de al menos 3 caracteres)
# Apellido (Validar que se ingresó un str de al menos 3 caracteres)
# DNI (Número entre 6 y 8 caracteres) 
# Género (M para masculino, F para femenino, NB para No Binario)
# Nota Final (Número entre 1 y 10)
I_NOMBRE = 0
I_APELLIDO = 1
I_DNI = 2
I_GENERO = 3
I_NOTA = 4

# Debemos realizar un programa que nos permita inscribir 10 alumnos en el sysacad.

lista_datos_finales = inicializar_matriz(2, 5, 0)

def cargar_alumnos(lista:list):

    for i in range(2):
    
        nombre = input("Nombre del alumno: ")
        while (len(nombre)) < 3:
            nombre = input("Error, reingrese nombre del alumno: ")

        apellido = input("Apellido del alumno: ")
        while (len(apellido)) < 3:
            apellido = input("Error, reingrese apellido del alumno: ")

        dni = int(input("Ingrese DNI: "))
        while dni < 111111 or dni > 99999999:
            dni = int(input("Reingrese DNI: "))

        genero = input("Ingrese genero, M, F O NB: ") 
        while genero != "M" and genero != "F" and genero != "NB":
            genero = input("Reingrese genero, M, F O NB: ") 

        nota = int(input("Ingrese nota: "))
        while nota < 1 or nota > 10:
            nota = int(input("Reingrese nota: "))

        lista[i][I_NOMBRE] = nombre
        lista[i][I_APELLIDO] = apellido
        lista[i][I_DNI] = dni
        lista[i][I_GENERO] = genero
        lista[i][I_NOTA] = nota

    return lista
        





# 2.Mostrar Todos los Alumnos:Mostrar la información de cada alumno en un formato que quede lindo para el usuario

def mostrar_datos_alumnos():
    '''
    
    '''
    resultado = cargar_alumnos(lista_datos_finales)

    print("Datos del alumno...")
    print("")
    for resultado in lista_datos_finales:
        print(f"Nombre: {resultado[0]}")
        print(f"Apellido: {resultado[1]}")
        print(f"DNI: {resultado[2]}")
        print(f"Genero: {resultado[3]}")
        print(f"Nota: {resultado[4]}")
        print("")

mostrar_datos_alumnos()

# 3.Mostrar Alumnos Promocionados:Mostrar sólo la información de los alumnos con nota mayor a 6 , en caso de no haber informar que no hay
# 4.Mostrar Alumnos Aprobados:Mostrar sólo la información de los alumnos con nota 4,5 , en caso de no haber informar que no hay
# 5.Mostrar Alumnos Desaprobados:Mostrar sólo la información de los alumnos con nota menor a 4 , en caso de no haber informar que no hay.
# 7.La cantidad de alumnos promocionados, aprobados y desaprobados

def mostrar_notas_promocionados_aprobados_y_desaprobados(lista:list):
    '''
    
    '''
    contador_promocionados = 0
    contador_aprobados = 0
    contador_desaprobados = 0
    for fil in range (len(lista)):
            if lista[fil][I_NOTA] > 6:
                contador_promocionados += 1
            elif lista [fil][I_NOTA] >= 4 or lista [fil][I_NOTA] <= 5:
                contador_aprobados += 1
            else:
                contador_desaprobados += 1

            if contador_promocionados >= 1:
                print(f"Datos del alumno promocionado...\nNombre: {lista[fil][I_NOMBRE]} {lista[fil][I_APELLIDO]}\nDNI: {lista[fil][I_DNI]}\nGenero: {lista[fil][I_GENERO]}")
            if contador_aprobados >= 1:
                print(f"Datos del alumno aprobado...\nNombre: {lista[fil][I_NOMBRE]} {lista[fil][I_APELLIDO]}\nDNI: {lista[fil][I_DNI]}\nGenero: {lista[fil][I_GENERO]}")
            if contador_desaprobados >= 1:
                print(f"Datos del alumno desaprobado...\nNombre: {lista[fil][I_NOMBRE]} {lista[fil][I_APELLIDO]}\nDNI: {lista[fil][I_DNI]}\nGenero: {lista[fil][I_GENERO]}")

    print("Cantidad de alumnos totales... ")
    print(f"Alumnos promocionados: {contador_promocionados}\nAlumnos aprobados: {contador_aprobados}\nAlumnos desaprobados: {contador_desaprobados}")

# mostrar_notas_promocionados_aprobados_y_desaprobados(lista_datos_finales)

# 6.Buscar Alumno por DNI:Se debe ingresar el DNI de un alumno y buscar si se encuentra o no en el sistema, mostrar su información también.

def buscar_alumno_con_dni(lista:list):
    '''
    
    '''
    bandera_dni = False
    busqueda_por_dni = int(input("Ingrese el DNI que desea buscar: "))
    for fil in range(len(lista)):
        if lista[fil][I_DNI] == busqueda_por_dni:
            print(f"Datos:\nNombre: {lista_datos_finales[fil][I_NOMBRE]}\nApellido: {lista_datos_finales[fil][I_APELLIDO]}\nNota: {lista_datos_finales[fil][I_NOTA]}\nGenero: {lista_datos_finales[fil][I_GENERO]}")
            bandera_dni = True
            break
    
    if bandera_dni == False:
        print("No se encontró el alumno...")


# buscar_alumno_con_dni(lista_datos_finales)

# 8.El promedio de nota de todos los alumnos
# 9.El promedio de nota de los alumnos masculinos
# 12.Mostrar la cantidad de alumnos que superan la nota promedio

def calcular_promedio_notas (lista:list):
    '''
    
    '''
    contador_notas = 0
    contador_notas_masculino = 0
    contador_alumnos_que_superan_promedio = 0

    acumulador_notas = 0
    acumulador_notas_masculino = 0



    for fil in range(len(lista)):
        acumulador_notas += lista[fil][I_NOTA]
        contador_notas += 1

        promedio_notas = acumulador_notas / contador_notas
        if acumulador_notas > promedio_notas:
            contador_alumnos_que_superan_promedio += 1


        if lista[fil][I_GENERO] == "M":
            acumulador_notas_masculino += lista[fil][I_NOTA]
            contador_notas_masculino += 1


    if contador_notas_masculino != 0:
        promedio_notas_masculino = acumulador_notas_masculino / contador_notas_masculino
        print(f"El promedio de nota de los masculinos es = {promedio_notas_masculino}")
    else:
        print("No se ingresaron alumnos masculinos...")

    if contador_alumnos_que_superan_promedio != 0:
        print(f"Alumnos que superan el promedio de nota = {contador_alumnos_que_superan_promedio}")
    else:
        print("Ningun alumno supera el promedio de nota")

    resultado = f"El promedio de las notas de todos los alumnos es = {promedio_notas}"

    return resultado

print(calcular_promedio_notas(lista_datos_finales))

# 10.El porcentaje de alumnos de cada género

def calcular_porcentaje_genero (Lista:list) -> float:
    '''
    
    '''
    contador_mujeres = 0
    contador_hombres = 0
    contador_no_binario = 0

    for fil in range(len(Lista)):
        if Lista[fil][I_GENERO] == "M":
            contador_hombres += 1
        elif Lista[fil][I_GENERO] == "F":
            contador_mujeres += 1
        else:
            contador_no_binario += 1
    
    if contador_hombres != 0:
        porcentaje_masculinos = (contador_hombres * 100) / len(Lista)
    else:
        porcentaje_masculinos = 0
    if contador_mujeres != 0:
        porcentaje_mujeres = (contador_mujeres * 100) / len(Lista)
    else:
        porcentaje_mujeres = 0
    if contador_no_binario != 0:
        porcentaje_no_binarios = (contador_no_binario * 100) / len(Lista)
    else:
        porcentaje_no_binarios = 0


    print(f"Datos de porcentaje por genero:\nMasculinos = {porcentaje_masculinos}%\nFemeninos = {porcentaje_mujeres}%\nNo Binarios = {porcentaje_no_binarios}%")


# calcular_porcentaje_genero(lista_datos_finales)

# 11.Mostrar el alumno o los alumnos con mayor nota

def mostrar_alumno_mayor_nota (lista:list):
    '''
    
    '''
    bandera = False
    nota_max = 0
    for fil in range(len(lista)):
        nota = lista[fil][I_NOTA]
        if nota > nota_max or bandera == False:
            nota_max = nota
            nombre_alumno_mejor_nota = lista[fil][I_NOMBRE]
            bandera = True
        
        elif nota == nota_max:
            nombre_alumno_mejor_nota += ", " + lista[fil][I_NOMBRE]
    

    return nombre_alumno_mejor_nota

print(mostrar_alumno_mayor_nota(lista_datos_finales))