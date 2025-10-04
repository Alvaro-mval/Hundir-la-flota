import variables
from funcion_recibir_disparo import recibir_disparo   #empezamos jugando e importamos la función de disparar.
from funcion_saber_donde_disparos import saber_disparo

def accion_usuario():
    disparo_x = int(input("Dime la cordenada X, por favor:"))   #pedimos la coordenada x
    disparo_y = int(input("Muy bien, ahora dime la cordenada y, por favor:"))   #pedimos la coordenada y
    print("Muy bien. Has dicho:", disparo_x,",", disparo_y)

    coordenadas_disparo =[(disparo_y-1), (disparo_x-1)]                     #creamos el disparo
    while variables.tablero_usuario_ataque[(disparo_y-1), (disparo_x-1)]  == "*":     #comprobamos que el disparo no se ha hecho antes en el mismo sitio
        print("ya has disparado ahí, elige otras cordenadas")
        disparo_x = int(input("Dime la coordenada X, por favor: "))
        disparo_y = int(input("Muy bien, ahora dime la coordenada Y, por favor: "))
        coordenadas_disparo =[(disparo_y-1), (disparo_x-1)]


    variables.tablero_cpu_defensa_init, estado_disparo_usuario = recibir_disparo(variables.tablero_cpu_defensa_init, coordenadas_disparo)  #llamamos a la funcion disparo y se actualiza el tablero
    #print(variables.tablero_cpu_defensa_init)
    #print()
        
#apuntamos donde hemos disparado

    variables.tablero_usuario_ataque = saber_disparo(variables.tablero_usuario_ataque, coordenadas_disparo)  #llamamos a la para saber donde hemos disparado y despues de cada tiro que nos lo muestre.
    print("Como me has caido bien, para ayudarte te muestro donde han ido todos tus disparos")
    print()
    print(variables.tablero_usuario_ataque)
    print()

    return estado_disparo_usuario    #retornamos el valor del disparo (acertado o no) que hemos calculado en la funcion recibir_disparo
    