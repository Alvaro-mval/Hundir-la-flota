# %%
import numpy as np  

def crea_tablero(lado = 10):   #funcion que crea tableros (matrices)
    tablero = np.full((lado,lado)," ")
    return tablero