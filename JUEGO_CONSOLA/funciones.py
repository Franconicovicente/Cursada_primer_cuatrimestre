import random
import os
from constantes import *

def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('clear')

def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:
    numero_ingresado = int(input(mensaje))
    while numero_ingresado > maximo or numero_ingresado < minimo:
        numero_ingresado = int(input(mensaje_error))
    return numero_ingresado

def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)

def mostrar_pregunta(pregunta_juego:dict) -> None:
    print(f"PREGUNTA: {pregunta_juego["pregunta"]}")
    print(f"1 - {pregunta_juego["respuesta_1"]}")
    print(f"2 - {pregunta_juego["respuesta_2"]}")
    print(f"3 - {pregunta_juego["respuesta_3"]}")
    
def verificar_respuesta(datos_juego:dict,pregunta_actual:dict,respuesta:int) -> bool:
    if respuesta == pregunta_actual["respuesta_correcta"]:
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
    else:
        #SIN PUNTOS NEGATIVOS
        if datos_juego["puntuacion"] > PUNTUACION_ERROR:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
            
        #CON PUNTOS NEGATIVOS
        #datos_juego["puntuacion"] -= PUNTUACION_ERROR
        
        datos_juego["vidas"] -= 1
        retorno = False
    
    return retorno
    
def jugar_preguntados_consola(datos_juego:dict,lista_preguntas:list[dict]) -> None:
    indice = 0
    
    while datos_juego["vidas"] != 0:
        #Todo lo que este aca va a formar parte de la partida de mi juego
        print(f"PUNTUACION ACTUAL: {datos_juego["puntuacion"]}")
        print(f"VIDAS RESTANTES: {datos_juego["vidas"]}")
        
        #¿Qué pasa si me quedo sin preguntas?
        if indice == len(lista_preguntas):
            indice = 0
            mezclar_lista(lista_preguntas)
        
        pregunta_actual = lista_preguntas[indice]
        mostrar_pregunta(pregunta_actual)
        respuesta = pedir_numero("Su respuesta: ","Reigrese la respuesta: (Entre 1 y 3)",1,3)
        
        if verificar_respuesta(datos_juego,pregunta_actual,respuesta):
            print("RESPUESTA CORRECTA")
        else:
            print("RESPUESTA INCORRECTA")
        
        indice += 1
        limpiar_consola()
    
def reiniciar_estadisticas(datos_juego:dict):
    datos_juego["puntuacion"] = 0
    datos_juego["vidas"] = CANTIDAD_VIDAS