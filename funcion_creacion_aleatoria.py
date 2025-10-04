from funcion_coloca_barcos import coloca_barco
from funcion_proposicion_barco import proposicion_barco
import variables

def creacion_aleatoria():
    #creacion de los barcos de usuario
    tablero = variables.tablero_usuario_defensa    #proponemos un barco aleatorio y dentro de la funcion, llamamos a la funcion coloca_barco para ver si es posible.
    for tamaño in [4,3,3,2,2,2]:
        tablero = proposicion_barco(tablero, tamaño)
    variables.tablero_usuario_defensa_init = tablero
    print(variables.tablero_usuario_defensa_init)
    print()

    #Creación aleatoria de los barcos de la CPU
    tablero = variables.tablero_cpu_defensa    #proponemos un barco aleatorio y dentro de la funcion, llamamos a la funcion coloca_barco para ver si es posible.
    for tamaño in [4,3,3,2,2,2]:
        tablero = proposicion_barco(tablero, tamaño)
    variables.tablero_cpu_defensa_init = tablero
    print(variables.tablero_cpu_defensa_init)