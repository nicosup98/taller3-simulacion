from random import randint, seed
from time import time_ns
from operator import itemgetter

def ebrio():
    seed(time_ns())
    cordenadas = {"x": 0, "y": 0}
    camino_ebrio = [
        (-1, 0),
        (1, 0),
        (0, 1),
        (0, -1)
    ]
    for _ in range(10):
        direccion = randint(0,3)
        camino_x, camino_y = camino_ebrio[direccion]
        cordenadas["x"] += camino_x
        cordenadas["y"] += camino_y
    return cordenadas


def simulacion(n_simulacion = 1000 * 500):
    n_is_far = 0
    data = []
    for _ in range(1,n_simulacion):
        x,y = itemgetter("x","y")(ebrio())
        data.append((x,y))
        if abs(x) + abs(y) == 2:
            n_is_far +=1
            
    return n_is_far / n_simulacion * 100, data, n_is_far, n_simulacion


if __name__ == "__main__":
    probabilidad,data,n_is_far,n_simulacion = simulacion()
    print(f"probabilidad de que el ebrio este a 2 calles de su inicio: {probabilidad}")
    print("mas info".center(20,"-"))
    print(f"numero de simulaciones: {n_simulacion}")
    print(f"numero de veces que el ebrio esta a 2: {n_is_far}")
