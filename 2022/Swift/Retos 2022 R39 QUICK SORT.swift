 /*
  * Reto #39
  * TOP ALGORITMOS: QUICK SORT
  * Fecha publicación enunciado: 27/09/22
  * Fecha publicación resolución: 03/10/22
  * Dificultad: MEDIA
  *
  * Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
  * creado por C.A.R. Hoare.
  * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a
  *   mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
  *   no únicamente a copiar su implementación.
  * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
  *   los más famosos de la historia.
  */

func quick_sort(lista: [Int])->[Int]{

    if lista.count < 2
    {
        return lista
    }

    let mitad = Int((Double(lista.count) / 2).rounded())
    let pivote = lista[mitad]
    var list = lista

    print("lista:",list)
    print("pivote:",pivote)
    if lista.count == 2{
        if list[0] > list[1]{
            (list[0], list[1]) = (list[1], list[0])
        }
        return list
    }
    var izq :[Int] = []
    var der : [Int] = []

    for (index, element) in lista.enumerated(){
        if index != mitad {
            if element < pivote{
                izq.append(element)
            }
            else{
                der.append(element) 
            }
        }
    }
    print("Izq:", izq)
    print("Der:", der)
    return quick_sort(lista: izq) + [pivote] + quick_sort(lista:der)

}

var list = [10,102,4,23,2,40,3,53,1,23,34,232,12]
print("La lista ordenada:",quick_sort(lista: list))

/*
// Basado en https://www.genbeta.com/desarrollo/implementando-el-algoritmo-quicksort

func quicksort(array: Array<Int>) -> Array<Int> {
    return array.isEmpty ? array : quicksort(array: array, first: 0, last: array.count - 1)
}

func quicksort(array: Array<Int>, first: Int, last: Int) -> Array<Int> {

    var i = first
    var j = last
    var array = array
    let pivot = (array[i] + array[j]) / 2

    while (i < j) {

        while array[i] < pivot {
            i += 1
        }

        while array[j] > pivot {
            j -= 1
        }

        if i <= j {

            let x = array[j]

            array[j] = array[i]
            array[i] = x

            i += 1
            j -= 1
        }
    }

    if first < j {
        array = quicksort(array: array, first: first, last: j)
    }

    if last > i {
        array = quicksort(array: array, first: i, last: last)
    }

    return array
}

let sortedArray = quicksort(array: [3, 5, 1, 8, 9, 0])
sortedArray.forEach { element in
    print(element)
}
*/