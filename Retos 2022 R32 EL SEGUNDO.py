# /*
#  * Reto #32
#  * EL SEGUNDO
#  * Fecha publicación enunciado: 08/08/22
#  * Fecha publicación resolución: 15/08/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
#  */

def second_bigger(list):
    bigger = list[0]
    big = bigger

    for x in list:
        if x > big:
            big = bigger
            bigger = x 

    return big

print("El segundo más grande es ", second_bigger([10,22,33,233,2424,223,4,5000]))