from Funciones import *

def ejecutar_menu():
    cantidad_victorias_jugador = 0
    cantidad_victorias_maquina = 0
    puntaje_maximo_adivina_numero = 0
    puntaje_maximo_mayor_menor = 0
    puntaje_final_adivina_numero = 0
    puntaje_final_mayor_menor = 0

    while(True):
        print("SALA DE JUEGOS\n1.Jugar al Piedra Papel o Tijera\n2.Jugar al Adivina el Número\n3.Jugar al Mayor/Menor\n4.Jugar a penales \n5.Salir")
        
        opcion = pedir_numero("Su opcion: ","Error, ingrese números entre 1-5\nSu opcion:",1,5)
        
        if opcion == 1:
            ganador = jugar_piedra_papel_tijera()
            print(ganador)
            #Pista : Deberia notificar quien gano la partida
        elif opcion == 2:
            puntaje_final_adivina_numero = jugar_adivina_numero()
            print(puntaje_final_adivina_numero)
        elif opcion == 3:
            puntaje_final_mayor_menor = jugar_mayor_menor()
            print(puntaje_final_mayor_menor)
        elif opcion == 4:
            penales = juego_penales()
            print(penales)
        elif opcion == 5:
            print("Saliendo...")
            break
        limpiar_consola()
        
    
ejecutar_menu()
