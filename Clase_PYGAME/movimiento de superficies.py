#Introducción
#Pygame es Pygame es un contenedor de Python para la biblioteca SDL, que significa Simple DirectMedia Layer.
#SDL brinda acceso multiplataforma a los componentes de hardware multimedia subyacentes de su sistema, como sonido, video, mouse, teclado y joystick. 

#Esta librería te permite:
#Levantar imágenes en formato PNG, BMP,  JPG, entre otros.
#Usar sistemas de sonido con audio en formato WAV, OGG, MP3.
#Realizar operaciones relacionadas con el gestor de ventanas.
#Manejar eventos de la aplicación.
#Manejo de dispositivos de entrada tales como mouse y teclado.
#Crear temporizadores para realizar acciones.
#Manejar colisiones entre objetos.
#Manejar un sistema de Sprites para elementos del juego.

#Ciclo de vida -> Es como una pelicula que se reproduce constantemente en mi programa, cada fotograma es una actualizacion al estado del juego que queremos hacer
#Para generar mi ciclo de vida generar un bucle infinito while que se encarga de actualizar constantemente lo que ocurre en pantalla, para poder interactuar con eso.

#1.Inicializacion

import pygame
import random
from Constantes import *

#Inicializar pygame
pygame.init()

#Configuraciones básicas
#Nombre del proyecto
pygame.display.set_caption("TEST JUEGO")
#Icono
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

#Generamos nuestra primer superficie

#Superficie sin imagen
# mi_superficie = pygame.Surface((100,100))
# #A mi superficie vacia le doy un color
# mi_superficie.fill(COLOR_VIOLETA)

#Superficie con imagen
mi_superficie = pygame.image.load("homero.png")
mi_superficie = pygame.transform.scale(mi_superficie,(150,200))
#Rectangulo
mi_rectangulo = mi_superficie.get_rect()
mi_rectangulo.x = 200
mi_rectangulo.y = 250 
#Pared
pared = pygame.Surface((40,200))
pared.fill(COLOR_AZUL)
rectangulo_pared = pared.get_rect()
rectangulo_pared.x = 40
rectangulo_pared.y = mi_rectangulo.y



#Configurar la pantalla
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
contador = 0

#Texto 
fuente = pygame.font.SysFont("Arial",25)
texto = fuente.render(f"PUNTUACION: {contador}",True,COLOR_NEGRO)

#SONIDOS
sonido_click = pygame.mixer.Sound("click.mp3")
sonido_click.set_volume(1)

#MUSICA

pygame.mixer.init() #Inicializo mixer para manipular la musica
pygame.mixer.music.load("musica.mp3") #Cargo musica de fondo
pygame.mixer.music.set_volume(0.0)
pygame.mixer.music.play()#Se ejecuta una vez
pygame.mixer.music.play(-1)#Se ejecuta constatemente

#Creo un reloj
clock = pygame.time.Clock()

#Eventos personalizados -> puedo especificar que ocurra lo que yo quiera cuando pasa un determinado tiempo
evento_tiempo_1_segundo = pygame.USEREVENT #Constante que guarda un numero
pygame.time.set_timer(evento_tiempo_1_segundo,1000)

evento_tiempo_5_segundos = pygame.USEREVENT + 1
pygame.time.set_timer(evento_tiempo_5_segundos,5000)
contador_tiempo = 30


#2.Bucle principal -> Es el bucle que se ejecuta cuando el juego esta activo
while corriendo:
    #3.Definir el tiempo en el que las imagenes se van a actualizar (FPS)
    clock.tick(FPS)
    contador +=1
    #4. Gestionar eventos:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            print("SALIENDO")
            corriendo = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            print(f"X = {evento.pos[0]} Y = {evento.pos[1]}")
            print("HIZO CLICK")

            if rectangulo_pared.collidepoint(evento.pos):
                # pared.fill(COLOR_VIOLETA)
                #Color random
                pared.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
                #Desaparecer la pared
                # rectangulo_pared.x = -100
                # rectangulo_pared.y = -100
                print("LE HICE CLICK A LA PARED")
            
            #Mover la imagen.png
            # mi_rectangulo.x = evento.pos[0]
            # mi_rectangulo.y = evento.pos[1]
            sonido_click.play()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                # print("SE TOCÓ FLECHA IZQUIERDA")
                if mi_rectangulo.left > 10:
                    mi_rectangulo.x -= 1
            elif evento.key == pygame.K_RIGHT:
                if mi_rectangulo.right < 345:
                    mi_rectangulo.x += 1
                # print("SE TOCÓ FLECHA DERECHA")

        if evento.type == evento_tiempo_1_segundo:
            contador_tiempo -= 1
            # print("PASÓ UN SEGUNDO")
        if evento.type == evento_tiempo_5_segundos:
            pass
            # print("PASÓ 5 SEGUNDOS")
    teclas = pygame.key.get_pressed()
    
    
    if teclas[pygame.K_LEFT]:
        if mi_rectangulo.colliderect(rectangulo_pared):
            # print("CHOCÓ")
            mi_rectangulo.right += 10
        else:
            if mi_rectangulo.left > 10:
                mi_rectangulo.x -= 1
                

    elif teclas[pygame.K_RIGHT]:
        if mi_rectangulo.colliderect(rectangulo_pared):
            mi_rectangulo.left += 10
            # print("CHOCÓ")
        else:
            if mi_rectangulo.right < 500:
                mi_rectangulo.x += 1

    # if contador_tiempo == 0:
    #     corriendo = False
    
    #5. Actualizar el juego: 
    texto = fuente.render(f"TIEMPO: {contador_tiempo}",True,COLOR_VIOLETA)
    
    #6.Dibujar pantalla y las otras superficies
    pantalla.fill(COLOR_BLANCO)
    #Dibujo la hitbox de homero
    # pygame.draw.rect(pantalla,COLOR_ROJO,mi_rectangulo,2)
    # pygame.draw.rect(pantalla,COLOR_ROJO,rectangulo_pared,2)
    
    
    #Muestro mi propia superficie
    pantalla.blit(mi_superficie,(mi_rectangulo.x,mi_rectangulo.y))
    pantalla.blit(texto,(10,10))
    pantalla.blit(pared,(rectangulo_pared.x,rectangulo_pared.y))
    #7.Actualiza la pantalla
    pygame.display.flip()
pygame.quit()