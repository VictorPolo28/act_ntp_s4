#Crea una función que genere una tupla con las coordenadas (x, y) de 10 puntos aleatorios. Usa un ciclo for para calcular cuáles puntos están dentro de un círculo de radio 5 centrado en el origen.

import math
import random


def cordenadas():
    random_points = []
    for i in range(10):
        x = random.uniform(0,10)
        y = random.uniform(0,10)
        random_points.append((x,y)) #de esta manera seguarda como tupla

        into_the_circle = []
        for x ,y in random_points:
            distance = math.sqrt(x**2 + y**2)
            if distance <= 5:
                into_the_circle.append((x,y))

    print("Todos los puntos generados:")
    for p in random_points:
        print(f"{p}")

    print("\nPuntos dentro del círculo de radio 5:")
    for p in into_the_circle:
        print(f"{p}")

    return tuple(random_points)

cordenadas()