from random import randint, seed
from time import time_ns
from operator import itemgetter

def ebrio():
    seed(time_ns())
    cordenadas = {"x": 0, "y": 0}
    camino_ebrio = {
        1: (-1, 0),
        2: (1, 0),
        3: (0, 1),
        4: (0, -1)
    }
    for _ in range(9):
        direccion = randint(1, 4)
        camino_x, camino_y = camino_ebrio[direccion]
        cordenadas["x"] += camino_x
        cordenadas["y"] += camino_y
    return cordenadas


def simulacion():
    n_simulacion = 100 * 100
    n_is_far = 0
    data = []
    for _ in range(1,n_simulacion):
        x,y = itemgetter("x","y")(ebrio())
        data.append((x,y))
        if x >= 2 or y >= 2:
            n_is_far +=1
            
    return {"probabilidad": n_is_far / n_simulacion * 100, "data":data}


if __name__ == "__main__":
    print(f"probabilidad de que el ebrio este a 2 calles de su inicio: {simulacion()["probabilidad"]}") # ilegalisimo
