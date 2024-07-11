# /*
#  *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  * 
#  *    *
#  *   ***
#  *  *   *
#  * *** ***
#  *
#  */

def triangle(n):
    if type(n) != int or n <= 0:
        raise ValueError("La variable deber ser entero mayor que 0.")
    height = 2*n - 1 
    base = (3 * n) + (n-1) if n  > 1 else 3
    area = [[' ' for _ in range(base)] for _ in range(height+1)]

    level = 1
    center = base // 2 
    #print(f"Centro: {center}")
    for x in range (height+1):
        #print (level)
        if x%2:
            #print("IMPAR")
            if (x == 1):
                area[x][center] = '*'
                area[x][center-1] = '*'
                area[x][center+1] = '*'
            else:
                for index, y in  enumerate (area[x-1]):
                    if y == '*':
                        area[x][index-1] = '*'
                        area[x][index] = '*'
                        if index+1 < base:
                            area[x][index+1] = '*'

            level += 1
        else:
            #print('PAR')
            if x == 0:
                area[x][center] = '*'
            else:
                for index, y in  enumerate (area[x-2]):
                    if y == '*':
                        area[x][index-2] = '*'
                        if index+2 < base:
                            area[x][index+2] = '*'

        
    for row in area:
        print(''.join(row))

n = 7
triangle(n)



#      *
#     ***
#    *   *
#   *** ***
#  *   *   *
# *** *** ***