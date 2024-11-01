import random
#Una lista de alumnos -> (Nombre, Apellido, Edad, Nota Final)

def cargar_alumno(lista_alumnos:list) -> bool:
    print("CARGO ALUMNO\n")
    nombre_aux = input("Ingrese nombre: ")
    apellido_aux = input("Ingrese apellido: ")
    edad_aux = int(input("Ingrese la edad: "))
    nota_final_aux = random.randint(1,10)
    respuesta = input("¿Desea cargar al alumno? (si/no)")
    
    if respuesta == "si":
        mi_alumno = {
        "nombre":nombre_aux,
        "apellido":apellido_aux,
        "edad":edad_aux,
        "nota_final":nota_final_aux
        }
        
        lista_alumnos.append(mi_alumno)
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

lista_alumnos = []

while(True):
    print("1.Cargar Alumno\n2.Mostrar Alumnos\n3.Salir")
    opcion = int(input("\nIngrese una opcion: "))
    if opcion == 1:
        if cargar_alumno(lista_alumnos):
            print("Alumno cargado con exito")
        else:
            print("Operacion cancelada")
    elif opcion == 2:
        if mostrar_lista_diccionarios(lista_alumnos) == False:
            print("No hay alumnos cargados")