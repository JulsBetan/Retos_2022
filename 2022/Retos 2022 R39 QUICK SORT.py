# /*
#  * Reto #39
#  * TOP ALGORITMOS: QUICK SORT
#  * Fecha publicación enunciado: 27/09/22
#  * Fecha publicación resolución: 03/10/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
#  * creado por C.A.R. Hoare.
#  * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a
#  *   mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
#  *   no únicamente a copiar su implementación.
#  * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
#  *   los más famosos de la historia.
#  */

def quick_sort(list):

    if len(list) < 2:
        return list

    mitad = len(list) // 2
    pivote = list[mitad]

    print("lista:",list)
    print("pivote:",pivote)
    if len(list) == 2:
        if list[0] > list[1]:
            list[0], list[1] = list[1], list[0]
        return list
    
    izq = []
    der = []

    for index, element in enumerate(list):
        if index != mitad:
            if element < pivote:
                izq.append(element)
            else:
                der.append(element) 

    print("Izq:", izq)
    print("Der:", der)
    return quick_sort(izq) + [pivote] + quick_sort(der)


list = [10,102,4,23,2,40,3,53,1,23,34,232,12]
print("La lista ordenada:",quick_sort(list))