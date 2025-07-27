#Implementa una función que reciba una lista de números con duplicados y use un ciclo for para crear un conjunto con números únicos. Luego compara el tamaño original vs el conjunto para mostrar cuántos duplicados había.

def validar_duplicados(lista):
    numeros_unicos = set()

    for numeros  in lista:
        numeros_unicos.add(numeros)
    
    
    cantidad_total = len(lista)
    cantidad_sin_duplicados = len(numeros_unicos)
    cantidad_duplicados = cantidad_total - cantidad_sin_duplicados

    return f"La cantidad de números duplicados era: {cantidad_duplicados}"

numeros_con_duplicados = [1, 5, 2, 8, 3, 5, 9, 2, 1, 7, 4, 6, 8, 0, 3]

numeros_repetidos = validar_duplicados(numeros_con_duplicados)
print(numeros_repetidos)
