""" /*
 * Reto #2
 * LA SUCESIÓN DE FIBONACCI
 * Fecha publicación enunciado: 10/01/22
 * Fecha publicación resolución: 17/01/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
 */ """
import math
#  1, 2, 3, 5, 7, 12, 19, 

def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)

var1 = 0
var2 = 1

for x in range(1,51):
    #print("Fibo ",x,"Es", fibonacci(x))
    print("Fibo ",x,"Es", var1)

    """ fib = var1
    var1 = var2 + fib
    var2 = fib  """

    fib = var1 + var2
    var1 = var2
    var2 = fib 

    