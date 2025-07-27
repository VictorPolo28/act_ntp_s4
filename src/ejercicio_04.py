#Desarrolla una función que simule un carrito de compras. Usa una lista para almacenar productos y un ciclo while para mostrar un menú que permita agregar, eliminar, mostrar productos y calcular el total.

def car_shop_menu():
    print("\nCar shop:")
    print("\n1.Agregar producto")
    print("\n2.Consultar productos")
    print("\n3.Eliminar producto")
    print("\n4.Calcular Total")
    print("\n5.Salir")


def car_shop():
    products =[]
    prices = []
 
   
    while True:
        car_shop_menu()
        try:
            option = int(input("Seleccione una opción: "))
            if option < 1 or option > 5:
                print("ingrese una opcion valida")
                continue
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        if option == 1:
            item = input("Ingrese el nombre del producto que  desea agregar: ")
            
            try:
                cost = float(input("Ingrese el valor del producto: "))
                products.append(item)
                prices.append(cost)
            except ValueError:
                print("El precio ingresado no  es numero")
        elif option == 2:
            if not products:
                print("El carrito esta vacio")
            else:
                print("\n Sus  productos son: ")

                for i in range(len(products)):
                    print(f"{i+1}.{products[i]} -${prices[i]}")
        elif option == 3:
            if not products:
                print("No hay productos para eliminar.")
            else:
                print("\nProductos actuales:")
                for i, producto in enumerate(products, start=1):
                    print(f"{i}. {producto} - ${prices[i-1]:.2f}")
                try:
                    delete = int(input("Ingrese el número del producto a eliminar: "))
                    if 1 <= delete <= len(products):
                        eliminado = products.pop(delete - 1)
                        prices.pop(delete - 1)
                        print(f"Producto '{eliminado}' eliminado del carrito.")
                    else:
                        print("Número fuera de rango.")
                except ValueError:
                    print("Debe ingresar un número válido.")
        elif  option == 4:
            if not prices:
                print(" No hay productos para calcular el total.")
            else:
                total = 0
                for n in prices:
                    total += n
                print("El totla es : ", total)
          
        else:
            break

car_shop()

