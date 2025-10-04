#Creacion tableros
from funcion_creacion_aleatoria import creacion_aleatoria
from funcion_crear_tablero import crea_tablero
import numpy as np
import variables
import time
import pygame

variables.tablero_cpu_defensa_init = np.full((10,10), " ")
variables.tablero_usuario_defensa_init = np.full((10,10), " ")
variables.tablero_usuario_defensa = np.full((10,10), " ")
variables.tablero_cpu_defensa = np.full((10,10), " ")
variables.tablero_usuario_ataque = np.full((10,10), " ")
variables.tablero_cpu_ataque = np.full((10,10), " ")

tablero_usuario_ataque = crea_tablero()       #MI tablero donde yo pongo veo los ataques que le hago a la CPU.
tablero_usuario_defensa = crea_tablero()      #MI tablero donde yo pongo mis barcos.
tablero_cpu_ataque = crea_tablero()           # tablero de la CPU donde la CPU ve los ataques que me hace.
tablero_cpu_defensa = crea_tablero()          # tablero de la CPU donde la CPU pone sus barcos.
print()
print()
print()
print()
print("¡BIENVENIDO A HUNDIR LA FLOTA!")
print()
print("       __/___")
print(" _____/______|")
print(" \              < < <       |")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()

while True:             #lanzamos el juego y preguntamos hasta que el usuario diga si o no
    respuesta = input("Hola grumete humano, estás hablando con el Super hundiflator 3000. ¿Quieres que te hunda todos los ciberbarcos de tu tablero? ").lower()

    if "si" in respuesta:       #si dice si, lanzamos el juego
        print(f"Has dicho '{respuesta}'. ¡let's go!!!")
        print()                
        pygame.mixer.init()   # Reproducir un archivo de música
        pygame.mixer.music.load("letsgo.mp3")
        pygame.mixer.music.play()
        
#creación aleatoria de barcos DE USUARIO

        print("Esta es tu configuración de tablero")
        print()
        creacion_aleatoria()
        
        print("Los cañones estan listos y los barcos en su sitio, tu juegas!")

        from funcion_iconos import boom  
        print(boom())
        from funcion_iconos import super_ordenador
        from funcion_iconos import humano_feliz  
        
        
        #turno del USUARIO
        from funcion_accion_usuario import accion_usuario   #esta variable bool nos dice si acertamos o fallamos para seguir jugando
        from funcion_accion_cpu import accion_cpu

        
        while True:  #bucle while siempre activo hasta que gane uno de los dos
            # Turno del jugador
            estado_disparo_usuario = True   #condcion inicial True para que se active el bucle while
            while estado_disparo_usuario:   #bucle while siempre activo mientras usuario acierte
                estado_disparo_usuario = accion_usuario()  #llamada para qeu se actualice la variable en cada iteracion while
                if "O" not in variables.tablero_cpu_defensa_init:
                    print("Me has ganado, enhorabuena!")
                    pygame.mixer.init()   # Reproducir un archivo de música
                    pygame.mixer.music.load("youwin.mp3")
                    pygame.mixer.music.play()
                    print(humano_feliz())
                    break                           #salimos del bucle si ganamos, pero tenemos que salir del otro bucle tambien
            if "O" not in variables.tablero_cpu_defensa_init: 
                break                               #salimos del segundo bucle tambien

            # Turno de la CPU
            estado_disparo_cpu = True               #condcion inicial True para que se active el bucle while
            while estado_disparo_cpu:               #bucle while siempre activo mientras usuario acierte
                time.sleep(1)                       # Esperamos 1 segundo
                estado_disparo_cpu = accion_cpu()   #llamada para qeu se actualice la variable en cada iteracion while
                if "O" not in variables.tablero_usuario_defensa_init:
                    print("JAJAJA, he ganado, soy invencible!")
                    pygame.mixer.init()   # Reproducir un archivo de música
                    pygame.mixer.music.load("youlose.mp3")
                    pygame.mixer.music.play() 
                    print(super_ordenador())
                    break                               #salimos del bucle si perdemos 
            if "O" not in variables.tablero_usuario_defensa_init:
                break                                   #salimos del segundo bucle si perdemos
        break

    elif "no" in respuesta:     #si dice no, salimos del juego
        print(f"Has dicho '{respuesta}'. ¡Veo que eres una persona sensata!!!")
        break

    else:                   #si dice otra cosa diferente, volvemos a preguntar
        print("No he entendido tu respuesta, dime 'si' o 'no', por favor.")