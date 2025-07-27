#Implementa una función que cree una tupla con los primeros 20 números de la secuencia de Fibonacci. Usa un ciclo while para generar la secuencia y luego un ciclo for para mostrar solo los números impares.

def fibonacci ():
    number1, number2 = 0,1
    fibonacci_tupla =[]
    odd_numbers = []
    while True:
        number1,number2 = number2, number1 + number2
        fibonacci_tupla.append(number1)
        if len(fibonacci_tupla) >= 20:
            break
    for numbers  in fibonacci_tupla:
        if numbers %2 != 0:
            odd_numbers.append(numbers)

    tuple(fibonacci_tupla)
    print(fibonacci_tupla)
    print(odd_numbers)
    
fibonacci ()