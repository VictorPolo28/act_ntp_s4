#Implementa una función que reciba una lista de palabras y use ciclos anidados para encontrar y devolver todas las palabras que contienen una letra específica ingresada por el usuario.

# def  find_word(lista):
#     palabras_encontradas = []
#     find_letter= input("Ingrese la letras que desea que contengan sus palabras: ")
#     for palabra  in lista:
#         palabra_ajustada = palabra.lower()
#         for letras  in palabras:
#             if letras in palabras:
#                 palabras_encontradas.append(palabras)
#                 print(palabras_encontradas)
 
def find_word(lista):
    found_words = []
    find_leter = input("Ingrese las letras que desea que contengan sus palabras: ").lower()
    
    for word in lista:
        for char in word:
            if char.lower() == find_leter:
                found_words.append(word)
                break
    return(found_words)

palabras = [
    # Animales
    "Perro", "Gato", "Elefante", "León", "Tortuga",
    
    # Frutas
    "Manzana", "Plátano", "Naranja", "Fresa", "Mango",
    
    # Objetos cotidianos
    "Mesa", "Silla", "Libro", "Teléfono", "Vaso",
    
    # Emociones
    "Felicidad", "Tristeza", "Miedo", "Amor", "Ira",
    
    # Colores
    "Rojo", "Azul", "Verde", "Amarillo", "Negro",
    
    # Verbos comunes
    "Correr", "Saltar", "Comer", "Dormir", "Escribir"
]

found = find_word(palabras)

print("\nPalabras que contienen la letra ingresada:")
for palabra in found:
    print(palabra)