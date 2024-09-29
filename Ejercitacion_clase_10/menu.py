from funciones import *


def ejecutar_menu():


    while(True):
        print("ALUMNOS SYSACAD\n1.Ingresar 10 alumnos\n2.Mostrar Todos los Alumnos\n3.Mostrar Alumnos Promocionados\n4.Jugar a penales \n5.Salir")
        
        opcion = pedir_numero("Su opcion: ","Error, ingrese números entre 1-12\nSu opcion:",1,12)
        
        if opcion == 1:
            alumnos_a_ingresar = cargar_alumnos(matriz_alumnos)
            print(alumnos_a_ingresar)
        elif opcion == 2:
            # mostrar_alumnos_ingresados = mostrar_alumno
            # print(mostrar_alumnos_ingresados)
            pass
        limpiar_consola()
        
    
ejecutar_menu()