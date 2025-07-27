#Crea una función que reciba dos listas y use ciclos for para convertirlas en conjuntos. Luego calcula y muestra la unión, intersección, diferencia y diferencia simétrica entre ambos conjuntos.

def conjuntos(lista1,lista2):
    conjunto1 =set()
    conjunto2 = set()
    
    for   item in lista1:
        conjunto1.add(item)
    for item in lista2:
        conjunto2.add(item)

    union = conjunto1.union(conjunto2)
    print("Unión:", union)
    intersection_set = conjunto1.intersection(conjunto2)
    print("Intersección:", intersection_set)
    difference_set = conjunto1.difference(conjunto2)
    print("Diferencias:",difference_set) 
    symmetric_difference_set = conjunto1.symmetric_difference(conjunto2)
    print("Diferencias simetricas: ",symmetric_difference_set) 

lista1 = [1, 2, "hola", True, 3.14, "python", False, "mundo", 10]
lista2 = [2, "hola", False, 3.14, "java", 20, True, "python", 99]

conjuntos(lista1,lista2)