# /*
#  * Reto #34
#  * LOS NÚMEROS PERDIDOS
#  * Fecha publicación enunciado: 22/08/22
#  * Fecha publicación resolución: 29/08/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
#  * - Lanza un error si el array de entrada no es correcto.
#  */

def lost_numbers(list1):
    lost = []

    if len(list1) < 2:
        raise ValueError("La lista debe tener al menos 2 elementos.")
    
    sorted_list = sorted(list(set(list1)))

    if list1 != sorted_list:
        raise ValueError("La lista debe estar ordenada y sin duplicados.")

    min = list1[0]
    max = list1[len(list1)-1]

    for x in range (min, max):
        if x not in list1:
            lost.append(x)

    return lost

try:
    print("Los números perdidos son:", lost_numbers([2]))
    print("Los números perdidos son:", lost_numbers([2,3,4,10,20]))
    
except ValueError as e:
    print("Se ha producido un error:", e)