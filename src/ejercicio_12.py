#Implementa una función que solicite al usuario ingresar palabras usando un ciclo while hasta que escriba 'salir'. Almacena las palabras en un conjunto y muestra cuántas palabras únicas se ingresaron y cuáles se repitieron.

def registrar_palabras():
    palabras_ingresadas = []
    palabras_unicas = set()
    palabras_repetidas = set()

    while True:
        palabra = input("Ingresa una palabra (o 'salir' para finalizar): ").lower()
        if palabra == 'salir':
            break

        if palabra in palabras_unicas:
            palabras_repetidas.add(palabra)
        else:
            palabras_unicas.add(palabra)

        palabras_ingresadas.append(palabra)

    print("\nResumen:")
    print(f"Total de palabras únicas: {len(palabras_unicas)}")
    print("Palabras únicas:", palabras_unicas)
    print("Palabras repetidas:", palabras_repetidas)

registrar_palabras()