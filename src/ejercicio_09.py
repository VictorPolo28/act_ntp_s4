#Crea una función que simule un sistema de coordenadas. Recibe una tupla de puntos (x, y) y usa ciclos para calcular la distancia total recorrida si se visitan todos los puntos en orden.

import math


def coordinates(points):
  total_distance = 0
  for index in range (len(points) -1):
    x1,y1 = points[index]
    x2 , y2 = points[index-1]
    distance =  math.sqrt((x2-x1)**2 + (y2-y1)**2)
    total_distance += distance
    return total_distance
  




puntos = (
    (0, 0),
    (2, 3),
    (5, 5),
    (6, 1),
    (4, -2),
    (0, -3),
    (-3, -1),
    (-4, 2),
    (-2, 5),
    (1, 4)
)
total= coordinates(puntos)
print("la distancia total es :", total)