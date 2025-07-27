#Implementa una función que solicite al usuario ingresar calificaciones usando un ciclo while hasta que escriba 'fin'. Almacena las calificaciones en una lista y calcula el promedio, la nota más alta y más baja.


def check_scores():
    scores = []

    while True:
        score = input("Ingrese su puntuacion o 'fin' para finalizar:").replace(" ", "")

        if score.lower() != "fin" :
            try:

                score = float(score)
                scores.append(score)

            except ValueError:
                print("La calificacion debe ser un numero  EJ 5.0")
        else:
            break
    if scores:
        print("\nResultados:")
        print(f"- Promedio: {sum(scores) / len(scores):.2f}")
        print(f"- Nota más alta: {max(scores)}")
        print(f"- Nota más baja: {min(scores)}")
    else:
        print("No se registro ninguna calificacion")

check_scores()
