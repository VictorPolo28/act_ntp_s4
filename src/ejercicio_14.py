#Crea una función que simule un sistema de votación. Usa un conjunto para almacenar los votos únicos y un ciclo while para permitir que múltiples usuarios voten. Al final, muestra los candidatos que recibieron votos.
def votaciones():
    votos = set()
    votantes = []

    while True:
        print("\n1. Votar")
        print("2. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            try:
                votante = int(input("Ingrese su número de cédula: "))
                if votante in votantes:
                    print("Usted ya dio su voto.")
                else:
                    votantes.append(votante)
                    candidato = input("Ingrese el nombre de su candidato: ")
                    votos.add(candidato)
                    print(f"Voto registrado para: {candidato}")
            except ValueError:
                print("El número de documento no es válido.")
        elif opcion == 2:
            print("\nVotación finalizada.")
            print("Candidatos que recibieron votos:", votos)
            print("Cantidad de votantes:", len(votantes))
            break
        else:
            print("Opción no válida. Intente de nuevo.")

votaciones()