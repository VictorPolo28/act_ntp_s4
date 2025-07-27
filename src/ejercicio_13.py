#Desarrolla una función que genere dos conjuntos: uno con números pares del 2 al 20 y otro con múltiplos de 3 del 3 al 30. Usa ciclos for para crear los conjuntos y muestra todas las operaciones entre ellos.

def conjuntos():
    numeros_pares = set()
    multiplos_de_3 =set()

    for numero in range(31):
        if numero %2 == 0  and numero <= 20:
            numeros_pares.add(numero)
        elif numero %3 == 0:
            multiplos_de_3.add(numero)

    
    print("Números pares del 2 al 20:", numeros_pares)
    print("Múltiplos de 3 del 3 al 30:", multiplos_de_3)

  

    print("Unión:", numeros_pares.union(multiplos_de_3))
    print("Intersección:", numeros_pares.intersection(multiplos_de_3))
    print("Diferencia (pares - múltiplos):", numeros_pares.difference(multiplos_de_3))
    print("Diferencia (múltiplos - pares):", multiplos_de_3.difference(numeros_pares))
    print("Diferencia simétrica:", numeros_pares.symmetric_difference(multiplos_de_3))


conjuntos()
    