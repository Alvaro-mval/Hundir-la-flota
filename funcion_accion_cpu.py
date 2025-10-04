import variables
from funcion_recibir_disparo import recibir_disparo   #empezamos jugando e importamos la función de disparar.
from funcion_saber_donde_disparos import saber_disparo
import random
import time

def accion_cpu():

#La CPU dispara

    fila = random.randint(1, 10)    #la maquina elige numero aleatorio de 1 a 10
    columna = random.randint(1, 10) 
    
    print("Fallaste! Me toca!!, soy el hundiflaitor 3000 y las coordenadas que elijo son:", fila,",", columna)

    coordenadas_disparo =[(columna-1), (fila-1)]                     #creamos el disparo
    
    while variables.tablero_cpu_ataque[(columna-1), (fila-1)] == "*":     #comprobamos que el disparo no se ha hecho antes en el mismo sitio
        fila = random.randint(1, 10)    #si las coordenadas son repetida, volvemos a elegir
        columna = random.randint(1, 10)
        coordenadas_disparo =[(columna-1), (fila-1)]

    time.sleep(1)                                                   # Esperamos 1 segundo
    variables.tablero_usuario_defensa_init, estado_disparo_cpu = recibir_disparo(variables.tablero_usuario_defensa_init, coordenadas_disparo)  #llamamos a la funcion disparo y se actualiza el tablero
    #print(variables.tablero_usuario_defensa_init)
    #print()

#apuntamos donde la CPU ha disparado

    variables.tablero_cpu_ataque = saber_disparo(variables.tablero_cpu_ataque, coordenadas_disparo)  #llamamos a la para saber donde hemos disparado y despues de cada tiro que nos lo muestre.
    #print(variables.tablero_cpu_ataque)
    #print()

    return estado_disparo_cpu               #retornamos el valor del disparo (acertado o no) que hemos calculado en la funcion recibir_disparo