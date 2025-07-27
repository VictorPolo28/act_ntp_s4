#Desarrolla una función que reciba dos tuplas de igual longitud y use un ciclo for para crear una nueva tupla con la suma de elementos correspondientes. Ejemplo: (1,2,3) + (4,5,6) = (5,7,9).

def tuple_sum(tupla1,tupla2):
    suma = ()
    for i in range(len(tupla1)):
        suma += (tupla1[i] + tupla2[i],)
    return tuple(suma)

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
print(tuple_sum(tupla1, tupla2))