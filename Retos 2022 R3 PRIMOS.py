""" /*
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Fecha publicación resolución: 24/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */ """

def isPrimo(num):
    if num < 3:
        return False
    for x in range (2, num):
         if (num % x == 0):
             return False
    return True

print(isPrimo(5))

for x in range (1,101):
    print(x, "Es primo" if isPrimo(x) else "No es primo")