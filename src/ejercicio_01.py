#Crea una función que reciba una lista de números y use un ciclo for para devolver una nueva lista con solo los números pares. Prueba la función con la lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

def even_numbers(listas):
    even_number =[]
    for  number in listas :
        
        if number %2 == 0:
            even_number.append(number)
    return even_number


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_numbers(list1)
print("The pears numbers are: ", result)