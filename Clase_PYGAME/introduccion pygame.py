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
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()#Se ejecuta una vez
pygame.mixer.music.play(-1)#Se ejecuta constatemente

#Creo un reloj
clock = pygame.time.Clock()

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
            sonido_click.play()
    
    #5. Actualizar el juego: 
    texto = fuente.render(f"PUNTUACION: {contador}",True,COLOR_VERDE)
    
    #6.Dibujar pantalla y las otras superficies
    pantalla.fill(COLOR_BLANCO)
    
    #Agregar un circulo rojo en el medio de la pantalla
    pygame.draw.circle(pantalla,COLOR_ROJO,(250,250),50)
    #Agregar un rectangulo negro en la pos x = 100, y = 100
    pygame.draw.rect(pantalla,COLOR_NEGRO,(100,100,100,50))
    
    #Muestro mi propia superficie
    pantalla.blit(mi_superficie,(350,350))
    pantalla.blit(texto,(10,10))
    
    #7.Actualiza la pantalla
    pygame.display.flip()
pygame.quit()