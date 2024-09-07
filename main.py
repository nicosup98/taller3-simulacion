import numpy as np
from numba import njit

@njit
def ebrio():
    # Usamos un array en lugar de un diccionario para almacenar las coordenadas
    cordenadas = np.array([0, 0])
    camino_ebrio = np.array([
        [-1, 0],  # dirección 1
        [1, 0],   # dirección 2
        [0, 1],   # dirección 3
        [0, -1]   # dirección 4
    ])
    
    for _ in range(10):
        direccion = np.random.randint(0, 4)  
        cordenadas += camino_ebrio[direccion]
    
    return cordenadas

@njit
def simulacion():
    n_simulacion = 1000* 500
    n_is_far = 0
    data = np.zeros((n_simulacion, 2))
    
    for i in range(n_simulacion):
        x, y = ebrio()
        data[i, 0] = x
        data[i, 1] = y
        if abs(x) >= 2 or abs(y) >= 2:
            n_is_far += 1
            
    return n_is_far / n_simulacion * 100, data

if __name__ == "__main__":
    probabilidad, _ = simulacion()
    print(f"Probabilidad de que el ebrio esté a 2 calles de su inicio: {probabilidad}%") 