#Implementa una función que simule una agenda telefónica usando un diccionario. Usa un ciclo while para mostrar un menú que permita agregar contactos, buscar por nombre, mostrar todos los contactos y eliminar contactos.

def agenda ():
    contactos= {}
    while True:
        print("\nBievenido a su agenda perosnal")
        print("1. Agregar contacto")
        print("2. Buscar contacto por nombre")
        print("3. Mostrar todos los contactos")
        print("4. Eliminar contacto")
        print("5. Salir")
        try:
            opcion =  int(input("Selecione una opcion: "))
        except ValueError:
            print("Debe ingresar una opcion valida")
            continue
        if opcion == 1:
            nombre = input("Ingrese el nombre de su nuevo contacto: ").strip().lower()
            if nombre in contactos:
                print(f"El contacto {nombre} ya  existe en su agenda")
            else:
                telefono = input("Ingrese el numero de telefono de su contacto")
                contactos[nombre] = telefono
                print(f"Contacto {nombre} agregado")
        elif opcion == 2:
            nombre = input("Ingrese el no,bre del contacto que desea buscar: ").split().lower()
            if nombre in contactos:
                print(f"{nombre.title()} : {agenda[nombre]}")
            else:
                print("El contacto no existe")
        
        elif  opcion == 3:
            if not contactos:
                print("la genda no contine contactos")
            else:
                print("\n Contactos  en su agenda: ")
                for nombre,telefono in agenda.items():
                    print(f"nombres.title(): {telefono}")
        elif opcion == 4:
            nombre = input("ingrese el nombre que desea eleiminar: ")
            if nombre in contactos:
                del contactos[nombre]
                print(f"Contacto '{nombre}' eliminado.")

            else:
                print("El contacto no existe en la agenda")
        elif opcion == 5:
            print("Cerrando la agenda...")
            break
        else:
            print("Opcion no valida")

