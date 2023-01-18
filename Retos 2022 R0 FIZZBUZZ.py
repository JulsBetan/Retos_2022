""" /*
* Reto #0
* EL FAMOSO "FIZZ BUZZ"
* Fecha publicación enunciado: 27/12/21
* Fecha publicación resolución: 03/01/22
* Dificultad: FÁCIL
*
* Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
* - Múltiplos de 3 por la palabra "fizz".
* - Múltiplos de 5 por la palabra "buzz".
* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
*/ """

print("Hola Mundo")

for x in range (1,101):
    mod3 = x%3 == 0
    mod5 = x%5 == 0
    if (mod3 and mod5): 
        print("FizzBuzz") 
    elif mod3:
        print("Fizz") 
    elif mod5:
        print("Buzz")
    else:
        print(x) 
print("Una linea")
for x in range (1,101):
    mod3 = x%3 == 0
    mod5 = x%5 == 0
    print("FizzBuzz" if (mod3 and mod5) else ( "Fizz" if mod3 else ("Buzz" if mod5 else x))) 
     