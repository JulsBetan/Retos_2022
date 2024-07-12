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

def piramid(n):
    for i in range(n):
        print(' '*(n-i-1) + '*'*(i+1) + '*'*i)

def triforce(n):
    for i in range(n):
        print(' '*(n-1) + ' '*(n-i) + '*'*(i+1) + '*'*i)

    for i in range(n):
        print(' '*(n-i-1) + '*'*(i+1) + '*'*i + ' '*(n-i-1) +' '*(n-i) + '*'*(i+1) + '*'*i)
        

n = 5
triangle(n)
piramid(n)
triforce(n)

#      *
#     ***
#    *   *
#   *** ***

#      *
#     ***
#    *   *
#   *** ***
#  *   *   *
# *** *** ***


#Solucion Moure
# def print_triforce(rows: int):

#     for row in range(0, rows * 2):
#         if row < rows:
#             start_space = " " * (((2 * rows) - 1) - row)
#             print_row = "*" * ((2 * (row + 1)) - 1)
#             print(f"{start_space}{print_row}")
#         else:
#             current_row = row - rows
#             start_space = " " * ((rows - current_row) - 1)
#             middle_space = " " * ((2 * (rows - current_row)) - 1)
#             print_row = "*" * ((2 * (current_row + 1)) - 1)
#             print(f"{start_space}{print_row}{middle_space}{print_row}")

# print_triforce(1)
# print_triforce(2)
# print_triforce(3)
# print_triforce(30)