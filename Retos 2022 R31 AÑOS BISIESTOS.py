# /*
#  * Reto #31
#  * AÑOS BISIESTOS
#  * Fecha publicación enunciado: 01/08/22
#  * Fecha publicación resolución: 08/08/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
#  * - Utiliza el menor número de líneas para resolver el ejercicio.
#  */

def next_bisiestos(number, begins):
    count = 1
    nextBisiesto = begins
    while count <= number:
        nextBisiesto += 1
        if nextBisiesto % 4 == 0 and (nextBisiesto %100 != 0 or nextBisiesto % 400 == 0):
            print(count, nextBisiesto)
            count += 1

next_bisiestos(30, 1899)