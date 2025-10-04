import funcion_iconos
import variables

def recibir_disparo(tablero, coordenada):
    if tablero[coordenada[0], coordenada[1]] == "O":
        tablero[coordenada[0], coordenada[1]] = "X"
        print("Tocado")
        print("Te toca otra vez")
        print(funcion_iconos.lloro())
        estado_disparo = True
    elif tablero[coordenada[0], coordenada[1]] == "X":
        print("Agonia, deja de perder el tiempo, dispara a otro sitio")
        print("Te toca otra vez")
        print(funcion_iconos.nahh())
        estado_disparo = True
    else:
        tablero[coordenada[0], coordenada[1]] = "-"
        print(funcion_iconos.solo_agua())
        estado_disparo = False
    return tablero, estado_disparo