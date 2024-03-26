# /*
#  * Reto #40
#  * TRIÁNGULO DE PASCAL
#  * Fecha publicación enunciado: 03/10/22
#  * Fecha publicación resolución: 10/10/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
#  * únicamente el tamaño del lado.
#  * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
#  *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
#  *

def pascal_triangle(size):
    #matrix = [[0] * ((size * 2) - 1) for _ in range((size * 2) - 1)]
    matrix = [[0] * size for _ in range(size)]

    for index, element in enumerate (matrix):
        for i in range (index+1):
            if index+1 == 1 or index+1 == 2: 
                element[i] = 1
            else:
                ind = i-1
                if i==0 or i==index:
                    element[i] = 1
                else:
                    element[i] = matrix[index-1][i] + matrix[index-1][i-1]

    tree = [[0] * ((size * 2) - 1) for _ in range(size)]

    posx = ((size*2)-1) // 2
    
    for index, element in enumerate (matrix):
        salta=0
        for i in range (index+1):
            tree[index][posx + salta] = element[i]
            salta+=2
        posx -= 1
    
    for element in (tree):
        print("".join( str (x) if x != 0 else ' '  for x in element ))

pascal_triangle(10)