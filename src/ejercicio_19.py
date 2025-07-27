#Crea una función que gestione las calificaciones de estudiantes. Usa un diccionario donde la clave sea el nombre del estudiante y el valor una lista de calificaciones. Implementa funciones para agregar estudiantes, agregar calificaciones y calcular promedios.

estudiantes = {}

def agregar_estudiantes():
    nombre = input("Ingrese el nombre del estudiante: ").title()
    if nombre in estudiantes:
        print("El estudiante ya existe")
    else:
        estudiantes[nombre] = []
        print(f"El estudiante {nombre} fue agregado.")

def agregar_calificacion():
    nombre = input("Ingrese el nombre del estudiante: ").title()
    
    if nombre in estudiantes:
        try:
            nota = float(input("Ingrese la calificación: "))
            estudiantes[nombre].append(nota)
            print(f"Calificación {nota} agregada a {nombre}.")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        print("El estudiante no existe.")

def calcular_promedio():
    nombre = input("Ingrese el nombre del estudiante: ").title()
    if nombre in estudiantes:
        if estudiantes[nombre]:
            promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
            print(f"Promedio de {nombre}: {promedio:.2f}")
        else:
            print("El estudiante no tiene calificaciones registradas.")
    else:
        print("El estudiante no existe.")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        print("\nEstudiantes y calificaciones:")
        for nombre, notas in estudiantes.items():
            notas_listado = ", ".join(str(n) for n in notas) if notas else "Sin calificaciones"
            print(f"{nombre}: {notas_listado}")

def gestionar_calificaciones():
    while True:
        print("\n--- MENÚ DE CALIFICACIONES ---")
        print("1. Agregar estudiante")
        print("2. Agregar calificación")
        print("3. Calcular promedio")
        print("4. Mostrar estudiantes")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            agregar_estudiantes()
        elif opcion == 2:
            agregar_calificacion()
        elif opcion == 3:
            calcular_promedio()
        elif opcion == 4:
            mostrar_estudiantes()
        elif opcion == 5:
            print("Saliendo del sistema de calificaciones.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


gestionar_calificaciones()