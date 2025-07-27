#Crea una función que reciba dos listas de igual tamaño y use un ciclo for para combinarlas elemento por elemento en una nueva lista. Ejemplo: [1,2,3] + ['a','b','c'] = [1,'a',2,'b',3,'c'].


def list_combination(lista1, lista2):
   
    if len(lista1) != len(lista2):
        print("Las listas no tienen el mismo tamaño.")
        return []

    combination = []
    for posicion in range(len(lista1)):
        combination.append(lista1[posicion])
        combination.append(lista2[posicion])
    
    return combination


l1 = [1, 2,3]
l2 = ['a', 'b', 'c']
result = list_combination(l1, l2)
print(result) 