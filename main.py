import numpy as np
from numba import njit
import time


@njit
def ebrio():
    # Usamos un array en lugar de un diccionario para almacenar las coordenadas
    
    cordenadas = np.array([0, 0])
    camino_ebrio = np.array([
        [-1, 0],  # oeste
        [1, 0],   # este
        [0, 1],   # norte
        [0, -1]   # sur
    ])
    direcciones = np.floor(np.random.uniform(0, 4, 10)).astype(np.int16)
    
    for direccion in direcciones:
        cordenadas += camino_ebrio[direccion]
    
    return cordenadas

@njit
def simulacion(n_simulacion = 1000 * 500):
    n_is_far = 0
    data = np.zeros((n_simulacion, 2))
    
    for i in range(n_simulacion):
        x, y = ebrio()
        data[i, 0] = x
        data[i, 1] = y
        if abs(x) + abs(y) == 2:
            n_is_far += 1
            
    return n_is_far / n_simulacion * 100, data,n_is_far,n_simulacion
        
        
    

if __name__ == "__main__":
    probabilidad, data,n_is_far,n_simulacion = simulacion(1000000)
    print(f"Probabilidad de que el ebrio esté a 2 calles de su inicio: {probabilidad}%") 
    print("mas info".center(20,"-"))
    print(f"numero de simulaciones: {n_simulacion}")
    print(f"numero de veces que el ebrio esta a 2 calles: {n_is_far}")