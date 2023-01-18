""" /*
 * Reto #13
 * FACTORIAL RECURSIVO
 * Fecha publicación enunciado: 28/03/22
 * Fecha publicación resolución: 04/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
 */ """

def factorial(number):
    if number == 1:
        return 1
    else:
        return factorial(number-1) * number

print("El factorial es",factorial(4))