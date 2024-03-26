    # /*
    # * Escribe un programa que muestre por consola (con un print) los
    # * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    # * cada impresión), sustituyendo los siguientes:
    # * - Múltiplos de 3 por la palabra "fizz".
    # * - Múltiplos de 5 por la palabra "buzz".
    # * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    # */

def fizzbuzz():
    for i in range(1,101):
        mult3 = i%3==0
        mult5 = i%5==0
        
        if mult3 and mult5:
            print(f"{i} FizzBuzz")
        elif mult3:
            print(f"{i} Fizz")
        elif mult5:
            print(f"{i} Buzz")

fizzbuzz()