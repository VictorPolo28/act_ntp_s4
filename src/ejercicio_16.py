#Crea una función que simule un inventario de productos.
#  Usa un diccionario para almacenar producto:cantidad y un ciclo while para mostrar un menú que permita agregar, actualizar, eliminar productos y mostrar el inventario completo.

def inventario_de_productos():
    inventario = {}
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Actualizar cantidad")
        print("3. Eliminar producto")
        print("4. Mostrar inventario")
        print("5. Salir")

        try:
            opcion = int(input("Selecione un opcion"))
        except ValueError:
            print("Debe ingresar un numero valido")
            continue
        if opcion == 1:
            producto = input("Ingrese el nombre del producto: ").strip().lower()
            if producto in inventario:
                print("El producto ya existe")
            else:
                try:
                    cantidad = int(input("Ingrese  la cantidad: "))
                    inventario[producto] = cantidad
                    print(f"Producto {producto} agregado")
                except ValueError:
                  print("Cantidad invalida.")

        elif opcion == 2:
            producto = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
            if producto in inventario:
                try:
                    cantidad = int(input("Ingrese la nueva cantidad"))
                    inventario[producto] = cantidad
                    print(f"Cantidad de {producto} actualizada")
                except ValueError:
                    print("CAntidad invalida")
            else:
                print("El producto no existe en  el inventario")
        elif opcion == 3:
            producto = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
            if producto in inventario:
                del inventario[producto]
                print(f"Producto {producto} eliminado")
            else:
                print("Ese producto no esta enel inventario")
        elif opcion == 4:
            if not inventario:
             print("El inventario esta vacio")
            else:
                print("\n--- Inventario actual ---")
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")
        elif opcion == 5:
            print("Saliendo del sistema de inventario.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

        
