from funciones import *
from preguntas import lista_preguntas

def ejecutar_menu():
    datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":""}
    while(True):
        print("PREGUNTADOS\n1.Jugar\n2.Rankings\n3.Salir")
        opcion = pedir_numero("Su opcion: ","Opcion invalida ingrese números entre 1-3\nSu opcion:",1,3)
        if opcion == 1:
            mezclar_lista(lista_preguntas)
            jugar_preguntados_consola(datos_juego,lista_preguntas)
            #mostrar_pregunta(lista_preguntas[0])
            print(f"JUEGO TERMINADO\nPUNTUACION FINAL {datos_juego["puntuacion"]} PUNTOS")
            datos_juego["nombre"] = input("Ingrese el nombre del jugador:")
            print(f"JUGADOR: {datos_juego['nombre']}")
            #Se guarden las puntuaciones (EN UN ARCHIVO)
    
            #Reiniciar las estadisticas
            reiniciar_estadisticas(datos_juego)
        elif opcion == 2:
            pass
        elif opcion == 3:
            break
        limpiar_consola()
    
ejecutar_menu()