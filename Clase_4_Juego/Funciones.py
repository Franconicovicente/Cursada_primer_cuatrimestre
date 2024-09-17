import random
import os

#Constantes -> para facilitar el uso de eso números.

PIEDRA = 1
PAPEL = 2
TIJERA = 3

MAYOR = 1
MENOR = 2

CRUZ = 0
CARA = 1




def limpiar_consola():
    input("Ingrese cualquier boton para continuar...")
    os.system('cls')

#PEDIR DATOS
def pedir_numero(mensaje:str,mensaje_error:str,minimo:int,maximo:int) -> int:

    numero = int(input(mensaje))
    while numero < minimo or numero > maximo:
        numero = int(input(mensaje_error))
    
    return numero



#RANKINGS
def calcular_maximo(numero_uno:int,numero_dos:int) -> int:
    if numero_uno > numero_dos:
        return numero_uno
    else:
        return numero_dos

def calcular_porcentaje(cantidad_victorias:int,cantidad_partidas:int)->float:
    resultado = (cantidad_victorias * 100) / cantidad_partidas
    return resultado

#JUEGOS EN GENERAL
def generar_respuesta_maquina(minimo:int,maximo:int) -> int:
    resultado = random.randint(minimo, maximo)
    return resultado


#PIEDRA PAPEL O TIJERA
def verificar_ganador_ronda(respuesta_jugador:int,respuesta_maquina:int) -> str:
    if respuesta_jugador == respuesta_maquina:
        mensaje = "Empate"
    elif (respuesta_jugador == PIEDRA and respuesta_maquina == TIJERA) or (respuesta_jugador == PAPEL and respuesta_maquina == PIEDRA) or (respuesta_jugador == TIJERA and respuesta_maquina == PAPEL):
        mensaje = "Gana el jugador"
    else:
        mensaje = "Gana la maquina"
    
    return mensaje


def verificar_ganador_partida(aciertos_jugador:int,aciertos_maquina:int) -> str:
    if aciertos_jugador > aciertos_maquina:
        mensaje = "Victoria"
    else:
        mensaje = "Derrota"

    return mensaje


def verificar_estado_partida(aciertos_jugador:int,aciertos_maquina:int,ronda_actual:int) -> bool:
    retorno = True
    if ronda_actual == 2:
        if aciertos_jugador == 2 or aciertos_maquina == 2:
            retorno = False #FIN DEL JUEGO
    elif ronda_actual >= 3:
        if aciertos_jugador > aciertos_maquina or aciertos_maquina > aciertos_jugador:
            retorno = False #False == FIN DEL JUEGO
    
    return retorno

def obtener_elemento(respuesta:int) -> str:
    if respuesta == 1:
        evento = "Piedra"
    elif respuesta == 2:
        evento = "Papel"
    else:
        evento = "Tijera"

    return evento

def jugar_piedra_papel_tijera() -> str:
    aciertos_jugador = 0
    aciertos_maquina = 0
    contador_rondas = 0
    print("Bienvenido a la partida de Piedra Papel o Tijera")
    
    while verificar_estado_partida(aciertos_jugador,aciertos_maquina,contador_rondas):
        contador_rondas +=1
        print(f"Ronda: {contador_rondas}")
        #Pista: Debo pedirle al jugador que elija el elemento
        #Pista: Debo elegir el elemento de la maquina
        #Pista: Debo saber quien gano la ronda (deberia mostrarlo tambien)
        respuesta_jugador = pedir_numero("Elija una opcion\n1. PIEDRA\n2. PAPEL\n3.TIJERA \nSu opcion: ", "ERROR. Reelija una opcion\n1. PIEDRA\n2. PAPEL\n3.TIJERA: ", 1, 3)
        respuesta_maquina = generar_respuesta_maquina(1, 3)
        print(f"La maquina eligio: {obtener_elemento(respuesta_maquina)}")
        ganador_ronda = verificar_ganador_ronda(respuesta_jugador, respuesta_maquina)
        
        if ganador_ronda == "Gana el jugador":
            aciertos_jugador += 1
        elif ganador_ronda == "Gana la maquina":
            aciertos_maquina += 1
        
        
            
        
        print(f"{ganador_ronda}!")
        #NO BORRAR
        limpiar_consola()
    #Pista: Debo saber quien gano la partida


    ganador = verificar_ganador_partida(aciertos_jugador, aciertos_maquina) 
    
    #En caso del piedra papel o tijera se va a mostrar el porcentaje de victorias entre el jugador y la máquina
    if aciertos_jugador > aciertos_maquina:
        victoria_jugador = calcular_porcentaje_victorias(aciertos_jugador, aciertos_maquina, contador_rondas)
        print(victoria_jugador)
    else:
        victoria_maquina = calcular_porcentaje_victorias(aciertos_jugador, aciertos_maquina, contador_rondas)
        print(victoria_maquina)
    
    # RANKING 
    return ganador

def calcular_porcentaje_victorias (aciertos_jugador:int, aciertos_maquina:int, contador_rondas:int) -> int:
    if aciertos_jugador > aciertos_maquina:
        porcentaje_jugador = round((aciertos_jugador * 100) / contador_rondas, 2)
        return f"El porcentaje de victoria del jugador es de un {porcentaje_jugador}%"
    else:
        porcentaje_maquina = round((aciertos_maquina * 100) / contador_rondas, 2)
        return f"El porcentaje de victoria de la maquina es de un {porcentaje_maquina}%"




#ADIVINA EL NUMERO

def mostrar_mensaje_final(puntaje_final:int)->None:
# En caso de no acertar ni una sola vez : 
# “Se ve que no eres bueno adivinando, más suerte la próxima”
# En caso de acertar entre 1 y 3 veces:
# “Buen trabajo adivinando”
# En caso de acertar entre 4 y 5 veces:
# “Excelente eres muy bueno adivinando”
# En caso de acertar más de 5 veces:
# “WOW, Usted es psiquico”
    if puntaje_final == 0:
        mensaje = "Se ve que no eres bueno adivinando, más suerte la próxima"
    elif puntaje_final > 0 or puntaje_final < 4:
        mensaje = "Buen trabajo adivinando"
    elif puntaje_final > 4 or puntaje_final < 6:
        mensaje = "Excelente eres muy bueno adivinando"
    else:
        mensaje = "WOW, usted es psiquico"

    return mensaje


def jugar_adivina_numero() -> int:
    contador_intentos = 3
    puntaje_final = 0
    bandera_puntaje_maximo = True
    puntaje_maximo = 0
    
    while(contador_intentos != 0):
        #Pista debo reutilizar funciones anteriores que use en el de piedra papel tijera no hacer todo de cero.
        numero_random_jugador = pedir_numero("Diga un número random entre 1 y 9: ", "Error, reingrese numero entre 1 y 9... : ", 1, 9)
        numero_random_maquina = generar_respuesta_maquina(1, 9)

        if numero_random_jugador != numero_random_maquina: 
            contador_intentos -= 1 
            print(f"Intentos restantes: {contador_intentos}")
        else:
            puntaje_final += 1
        

        if bandera_puntaje_maximo == True or puntaje_maximo < puntaje_final:
            puntaje_maximo = puntaje_final
            bandera_puntaje_maximo = False
        #NO BORRAR
        limpiar_consola()

    
    puntaje = mostrar_mensaje_final(puntaje_final)
    return puntaje  




#MAYOR MENOR

def verificar_cartas(carta:int, carta_posterior:int,eleccion_jugador:int) -> str:    

    # MAYOR = 1
    # MENOR = 2       
    carta = generar_respuesta_maquina(1, 12)
    print(f"El valor de la carta es {carta}")


    carta_posterior = generar_respuesta_maquina (1, 12)    
    # print(carta_posterior)
    eleccion_jugador = pedir_numero(f"Adivine el numero de la carta posterior a {carta} entre el 1 = MAYOR y el 2 = MENOR: ", "Error, REINGRESE número entre 1 y 2: ", 1, 2)

    if eleccion_jugador == 1:
        if carta_posterior > carta:
            mensaje = "Tuvo razón"
        else:
            mensaje = "No tuvo razón"
    else:
        if carta_posterior > carta:
            mensaje = "No tuvo razón"
        else:
            mensaje = "Tuvo razón"
    
    return mensaje



        
def jugar_mayor_menor():
    puntuaje_final = 0 
    

    #Pista : Debo generar primero la carta random antes de jugar
    while(True):
        carta = generar_respuesta_maquina(1, 12)
        print(f"El número de la carta es {carta}")
        carta_posterior = generar_respuesta_maquina(1, 12)
        eleccion_jugador = pedir_numero(f"La siguiente carta es mayor a {carta}? El 1 = MAYOR y el 2 = MENOR: ", "Error, REINGRESE número entre 1 y 2: ", 1, 2)
        if eleccion_jugador == 1:
            if carta_posterior > carta:
                puntuaje_final += 1
            else:
                break
        elif eleccion_jugador == 2:
            if carta_posterior > carta:
                break
            else:
                puntuaje_final += 1
        #Pista : Cuando pierdo debo salir del while
        #NO BORRAR
        limpiar_consola()
    mensaje = f"Tuviste un total de {puntuaje_final} aciertos!"

    return mensaje


# Juego nro 4 -> Tanda de Penales
# Agregar un juego que me permita patear penales en los siguientes lugares.
# A la izquierda
# Al medio
# A la derecha
# Gana la partida el mejor de cinco intentos, en caso de empate aplican las mismas reglas que en el piedra papel o tijera.
# Nota mostrar mensajes descriptivos de cada penal pateado, por ejemplo.
# Si el jugador elige el número 2 y la máquina el número 3 debería mostrar.
# “El jugador pateó al medio. La máquina se tiró a la derecha. El jugador convierte Gol” -> Pueden usar el mensaje que quieran pero que explique cada circunstancia de la tanda de penales.
def verificar_estado_partida_futbol(aciertos_jugador:int,aciertos_maquina:int,contador_rondas:int) -> bool:
    retorno = True
    if contador_rondas == 4:
        if aciertos_jugador == 3 or aciertos_maquina == 3:
            retorno = False #FIN DEL JUEGO
    elif contador_rondas >= 4:
        if aciertos_jugador > aciertos_maquina or aciertos_maquina > aciertos_jugador:
            retorno = False #False == FIN DEL JUEGO

    return retorno

def verificar_estado_ronda_futbol_patear (patear_numero:int, maquina_penales:int) -> int:
    if patear_numero == 1 and (maquina_penales == 2 or maquina_penales == 3) or patear_numero == 2 and(maquina_penales == 1 or maquina_penales == 3) or patear_numero == 3 and (maquina_penales == 1 or maquina_penales == 2):
        mensaje = "El jugador patea a la izquierda, la maquina no llega! GOL!"  
    else:
        mensaje = "Atajó la maquina"
    return mensaje

def verificar_estado_ronda_futbol_atajar (atajar_numero:int, maquina_penales:int) -> int:
    if atajar_numero == 1 and (maquina_penales == 2 or maquina_penales == 3) or atajar_numero == 2 and (maquina_penales == 1 or maquina_penales == 3) or atajar_numero == 3 and (maquina_penales == 1 or maquina_penales == 2):
        mensaje = "Gol de la maquina"
    else:
        mensaje = "Buena atajada"

    return mensaje

def juego_penales (): 
        aciertos_jugador = 0
        aciertos_maquina = 0
        contador_rondas = 0
        patear_numero = 0
    # Se le pedirá al jugador cara o cruz, si acierta empieza pateando el jugador, sino empieza pateando la máquina.    
        respuesta = pedir_numero("Elija cara o cruz, CARA = 1, CRUZ = 0 : ", "ERROR : ", 0, 1)
        cara_o_cruz_random = generar_respuesta_maquina(0, 1)

        while verificar_estado_partida_futbol (aciertos_jugador,aciertos_maquina,contador_rondas):
            contador_rondas += 1
            print(f"Contador rondas = {contador_rondas}")
            maquina_penales = generar_respuesta_maquina(1, 3)
            

            if respuesta == cara_o_cruz_random:
                # Cuando al jugador le toque patear el penal también tiene que elegir un número del 1 al 3 en este caso debe elegir un número distinto a la máquina de lo contrario la misma le atajara el penal
                patear_numero = pedir_numero("Elija un numero, que será donde patea el penal: 1, 2 o 3: ", "ERROR: ", 1, 3)
                ganador_ronda_pateo = verificar_estado_ronda_futbol_patear(patear_numero, maquina_penales)
                print(f"El numero que eligió la maquina es = {maquina_penales}")
                print(ganador_ronda_pateo)
                limpiar_consola()

                if ganador_ronda_pateo == "Atajó la maquina":
                    aciertos_maquina += 1
                else:
                    aciertos_jugador += 1
                
            else:
                atajar_numero = pedir_numero("Elija un numero, que será donde va a atajar el penal: 1, 2 o 3: ", "ERROR: ", 1, 3)
                ganador_ronda_atajada = verificar_estado_ronda_futbol_atajar(atajar_numero, maquina_penales)
                print(f"El numero que eligió la maquina es = {maquina_penales}")
                print(ganador_ronda_atajada)
                limpiar_consola()
                
                if ganador_ronda_atajada == "Gol de la maquina":
                    aciertos_maquina += 1
                else:
                    aciertos_jugador += 1
        
        if aciertos_jugador > aciertos_maquina:
            mensaje = "Ganó el jugador!"
        elif aciertos_jugador < aciertos_maquina:
            mensaje = "Ganó la maquina"
        else:
            mensaje = "Salieron empatados"

        return mensaje


