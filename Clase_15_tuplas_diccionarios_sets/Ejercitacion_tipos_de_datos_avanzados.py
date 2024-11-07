import random
import copy
'''
Ejercitación tipos de datos avanzados 

Necesitamos un sistema para organizar a los empleados de nuestra empresa.
Para eso debemos guardar en una lista de diccionarios los datos de cada empleado

Un empleado tiene la siguiente información



Se debe resolver lo siguiente:


1.Cargar empleados : Se agrega a la lista de empleados un nuevo empleado, deben permitir cancelar la acción
2.Mostrar empleados : Se muestra la información del empleado en un formato amigable para el usuario.
3.Ordenar empleados por sueldo: Crea una copia (DEEP COPY) de la lista original, la ordena y la muestra.
4.Mostrar empleados más viejos:Muestra los 5 empleados más viejos
5.Mostrar empleados con mayor antigüedad:Muestra los 5 empleados con mayor antigüedad en años
6.Mostrar apellidos:Muestra una lista de todos los apellidos de todos los empleados de la empresa, sin repetir uno a los otros , ordenados alfabéticamente (Usar set)
7.Mostrar empleados usd:Muestra a los empleados pero en vez de mostrar su salario en pesos lo muestra en USD. 
Tomar de referencia el valor actual del dólar blue: Valor dolar
8.Buscar empleado: Se debe buscar y mostrar a un empleado por dni, en caso de no encontrarlo tirar error
9.Eliminar empleado: Se debe eliminar un empleado de la lista, buscando por dni, preguntarle al usuario si está seguro de eliminarlo ya que no hay vuelta atrás.
'''
lista_empleados = []
def cargar_datos_empleado(lista_empleados:list) -> bool:
    '''
    
    '''
    
    print("CARGO EMPLEADO...\n")

    dni = int(input("Ingrese DNI: "))
    while dni < 1111111 or dni > 99999999:
        dni = int(input("Error, ingrese un DNI valido: "))

    apellido = input("Ingrese apellido: ")
    bandera = apellido.isalpha()
    while bandera == False:
        apellido = input("Error, ingrese un apellido valido: ")
        bandera = apellido.isalpha()

    nombre = input("Ingrese nombre: ")
    bandera = nombre.isalpha()
    while bandera == False:
        nombre = input("Error, ingrese un nombre valido: ")
        bandera = nombre.isalpha()

    edad = int(input("Ingrese la edad: "))
    while edad < 18 or edad > 65:
        edad = int(input("Error, ingrese una edad valida: "))
    
    antiguedad = int(input("Ingrese años de antiguedad: "))
    while antiguedad < 1:
        antiguedad = int(input("Error, ingrese un año de antiguedad valido: "))
    
    rol = input("Ingrese su rol (Administrativo, Gerencia, Atención al cliente o Limpieza): ")
    while rol != "Administrativo" and rol != "Gerencia" and rol != "Atención al cliente" and rol != "Limpieza":
        rol = input("Ingrese una opción valida...\nAdministrativo, Gerencia, Atención al cliente o Limpieza: ")
    
    sueldo = random.randint(600000, 30000000)
    print(f"Sueldo generado automaticamente: ${sueldo:,} ARS.")

    respuesta = input("¿Desea cargar al empleado? (si/no)")
    
    if respuesta == "si":
        mi_empleado = {
        "dni":dni,
        "apellido":apellido,
        "nombre":nombre,
        "edad":edad,
        "antiguedad":antiguedad,
        "rol":rol,
        "sueldo":sueldo
        }
        
        lista_empleados.append(mi_empleado)
        retorno = True
    else:
        retorno = False
    
    return retorno

def mostrar_lista_diccionarios(lista_diccionarios:list) -> bool:
    retorno = False
    for elemento in lista_diccionarios:
        retorno = True
        for clave,valor in elemento.items():
            print(f"{clave.replace("_"," ").title()} : {valor}")
        print("")
    return retorno


while(True):
    print("MENU\n1.Cargar datos del empleado.\n2.Mostrar datos del empleado.\n3.Ordenar empleados por sueldo.\n")
    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        if cargar_datos_empleado(lista_empleados):
            print("Empleado cargado con exito...")
        else:
            print("Empleado cancelado... ")

    elif opcion == 2:
        if mostrar_lista_diccionarios(lista_empleados) == False:
            print("No se ingresaron empleados...")
    
    elif opcion == 3:
        lista_empleados_copia = copy.deepcopy(lista_empleados)
        lista_empleados_copia.sort(reverse=True)
        mostrar_lista_diccionarios(lista_empleados_copia)


#3.Ordenar empleados por sueldo: Crea una copia (DEEP COPY) de la lista original, la ordena y la muestra.