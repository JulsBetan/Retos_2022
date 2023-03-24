# /*
#  * Reto #29
#  * ORDENA LA LISTA
#  * Fecha publicación enunciado: 18/07/22
#  * Fecha publicación resolución: 26/07/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que ordene y retorne una matriz de números.
#  * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
#  *   "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
#  * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
#  */

def sort_list(list, opt):
    sorted_list = []
    menor=0
    
    if not list:
        return "lista vacía"
    else:
        for x in list:
            menor = 0
            if sorted_list:
                for index, y in enumerate(sorted_list):
                    if opt == "Asc":
                        if x <= y:
                            menor = 1
                            sorted_list.insert(index, x)
                            break
                    else:
                        if x > y:
                            menor = 1
                            sorted_list.insert(index, x)
                            break
                if menor == 0:
                    sorted_list.append(x)
            else:
                sorted_list.append(x) 

        return sorted_list

print ("La lista ordenada es: ", sort_list([1978,3,5,10,23,45,29,4,3,140,300],"Asc"))

print ("La lista ordenada es: ", sort_list([1978,3,5,10,23,45,29,4,3,140,300],"Desc"))

print ("La lista ordenada es: ", sort_list([],"Asc"))

#45,29,23,10,5,4,3