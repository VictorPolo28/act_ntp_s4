#Desarrolla una función que simule un sistema de registro de temperaturas por ciudad. Usa un diccionario anidado donde cada ciudad tenga un diccionario con días de la semana y temperaturas. Calcula estadísticas por ciudad y día.

temperaturas = {}

def registrar_temperatura():
    ciudad = input("Ingrese el nombre de la ciudad: ").title()
    dia = input("Ingrese el día de la semana: ").capitalize()
    
    try:
        temp = float(input("Ingrese la temperatura: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    
    if ciudad not in temperaturas:
        temperaturas[ciudad] = {}
    
    temperaturas[ciudad][dia] = temp
    print(f"Temperatura de {temp}° registrada para {ciudad} el día {dia}.")

def mostrar_temperaturas():
    if not temperaturas:
        print("No hay temperaturas registradas.")
        return
    
    for ciudad, dias in temperaturas.items():
        print(f"\n Ciudad: {ciudad}")
        for dia, temp in dias.items():
            print(f"  {dia}: {temp}°C")

def estadisticas_por_ciudad():
    ciudad = input("Ingrese la ciudad para ver estadísticas: ").title()
    
    if ciudad not in temperaturas:
        print("La ciudad no está registrada.")
        return
    
    temps = list(temperaturas[ciudad].values())
    if not temps:
        print("No hay temperaturas registradas para esta ciudad.")
        return

    print(f"\n Estadísticas para {ciudad}:")
    print(f"  Promedio: {sum(temps)/len(temps):.2f}°C")
    print(f"  Mínima: {min(temps)}°C")
    print(f"  Máxima: {max(temps)}°C")

def estadisticas_por_dia():
    dia = input("Ingrese el día de la semana: ").capitalize()
    temps = []

    for ciudad in temperaturas:
        if dia in temperaturas[ciudad]:
            temps.append(temperaturas[ciudad][dia])
    
    if not temps:
        print(f"No hay temperaturas registradas para el día {dia}.")
        return

    print(f"\n Estadísticas para el día {dia}:")
    print(f"  Promedio: {sum(temps)/len(temps):.2f}°C")
    print(f"  Mínima: {min(temps)}°C")
    print(f"  Máxima: {max(temps)}°C")

def menu():
    while True:
        print("\n--- SISTEMA DE REGISTRO DE TEMPERATURAS ---")
        print("1. Registrar temperatura")
        print("2. Mostrar temperaturas")
        print("3. Estadísticas por ciudad")
        print("4. Estadísticas por día")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            registrar_temperatura()
        elif opcion == 2:
            mostrar_temperaturas()
        elif opcion == 3:
            estadisticas_por_ciudad()
        elif opcion == 4:
            estadisticas_por_dia()
        elif opcion == 5:
            print("Saliendo del sistema. ❄️")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


menu()