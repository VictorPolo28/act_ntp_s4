#Desarrolla una función que reciba una frase y use un ciclo for para crear un diccionario que cuente la frecuencia de cada palabra. Ignora mayúsculas/minúsculas y muestra las palabras ordenadas por frecuencia.

def frecuencia_de_palabras(oracion):
    oracion = oracion.lower()
    palabras = oracion.split()
    frecuencia = {}

    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1


    frecuencia_ordenada = dict(sorted(frecuencia.items(), key=lambda item: item[1], reverse=True))

    print("\nFrecuencia de palabras:")
    for palabra, conteo in frecuencia_ordenada.items():
        print(f"{palabra}: {conteo}")


frase = "En el bosque, el viento soplaba fuerte. El bosque crujía con cada soplo del viento. Los árboles del bosque se movían al ritmo del viento, y las hojas caían una tras otra. El silencio del bosque solo era interrumpido por el susurro del viento."
frecuencia_de_palabras(frase)