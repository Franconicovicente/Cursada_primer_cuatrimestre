from funciones import *


def ejecutar_menu():


    while(True):
        print("ALUMNOS SYSACAD\n1.Ingresar 10 alumnos\n2.Mostrar Todos los Alumnos\n3.Mostrar Alumnos Promocionados\n4.Mostrar alumnos aprobados \n5.Mostrar Alumnos Desaprobados\n6.Buscar Alumno por DNI\n7.La cantidad de alumnos promocionados, aprobados y desaprobados\n8.El promedio de nota de todos los alumnos\n9.El promedio de nota de los alumnos masculinos\n10.El porcentaje de alumnos de cada género\n11.Mostrar el alumno o los alumnos con mayor nota\n12.Mostrar la cantidad de alumnos que superan la nota promedio\n13.Salir")
        
        opcion = pedir_numero("Su opcion: ","Error, ingrese números entre 1-12\nSu opcion:",1,13)
        
        if opcion == 1:
            alumnos_a_ingresar = cargar_alumnos(matriz_alumnos)
        elif opcion == 2:
            mostrar_alumnos_ingresados = mostrar_alumno(matriz_alumnos)
        elif opcion == 3:
            alumnos_promocionados = mostrar_alumno_notas(matriz_alumnos, 6, 10, "Alumnos promocionados: ", "No hay alumnos promocionados")
        elif opcion == 4:
            alumnos_aprobados = mostrar_alumno_notas(matriz_alumnos, 4, 5, "Alumnos aprobados: ", "No hay alumnos aprobados.")
        elif opcion == 5:
            alumnos_desaprobados = mostrar_alumno_notas(matriz_alumnos, 1, 3, "Alumnos desaprobados: ", "No hay alumnos desaprobados.")
        elif opcion == 6:
            alumno_por_dni = mostrar_alumno_dni(matriz_alumnos)
        elif opcion == 7:
            cantidad_alumnos = mostrar_alumnos()
        elif opcion == 8:
            promedio_nota_alumnos = calcular_promedio_notas(matriz_alumnos)
        elif opcion == 9:
            promedio_nota_masculinos = calcular_promedio_notas_masculinos(matriz_alumnos)
        elif opcion == 10:
            porcentaje_alumnos_genero = contar_alumnos(matriz_alumnos)
        elif opcion == 11:
            alumno_mayor_nota = calcular_mayor_nota(matriz_alumnos)
        elif opcion == 12:
            alumnos_nota_promedio = mostrar_alumnos_nota_promedio(matriz_alumnos)
        else:
            print("Saliendo...")
            break

        limpiar_consola()
        
    
ejecutar_menu()