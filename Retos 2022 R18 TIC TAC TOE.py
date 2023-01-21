""" /*
 * Reto #18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
 */ """

def threeInline (matrix, char):
    return (matrix[0][0] == char and matrix[0][1] == char and matrix[0][2] == char ) or \
            (matrix[1][0] == char and matrix[1][1] == char and matrix[1][2] == char) or \
            (matrix[2][0] == char and matrix[2][1] == char and matrix[2][2] == char) or \
            (matrix[0][0] == char and matrix[1][0] == char and matrix[2][0] == char) or \
            (matrix[0][1] == char and matrix[1][1] == char and matrix[2][1] == char) or \
            (matrix[0][2] == char and matrix[1][2] == char and matrix[2][2] == char) or \
            (matrix[0][0] == char and matrix[1][1] == char and matrix[2][2] == char) or \
            (matrix[2][0] == char and matrix[1][1] == char and matrix[0][2] == char)  

def analize_matrix(matrix):
    result = "Empate"

    xCount = 0
    oCount = 0

    for x in range (3):
        for y in range (3):
            if matrix[x][y] == "X":
                xCount += 1
            if matrix[x][y] == "O":
                oCount += 1

    if abs(xCount-oCount) > 1:
        return "Nulo"

    if threeInline(matrix, "X") and threeInline(matrix, "O"):
        result = "Nulo"
    elif threeInline(matrix, "X"):
        result = 'X'
    elif threeInline(matrix, "O"):
        result = 'O'
        
    return result

print("El resultado es: ", analize_matrix([["O","X","O"],
                                            ["O","O","X"],
                                            ["O","X","X"]]))


#Otra Solución

from enum import Enum 

class Cell(Enum):
    X = "X"
    O = "O"
    Empty = " "

def analize(matrix):
    result = "Empate"

    xCount = 0
    oCount = 0

    flat_matrix = []

    for x in range(3):
        for y in range(3):
            flat_matrix.append(matrix[x][y])
            if matrix[x][y] == Cell.X:
                xCount += 1
            if matrix[x][y] == Cell.O:
                oCount += 1

    if abs(xCount-oCount) > 1:
        return "Nulo"

    #Draw o Win

    winOptions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[6,4,2]]

    for row in winOptions:
        if flat_matrix[row[0]] != Cell.Empty and flat_matrix[row[0]] == flat_matrix[row[1]] and flat_matrix[row[0]] == flat_matrix[row[2]]:
            winner  = flat_matrix[row[0]]

            if result != "Empate" and result != winner:
                return "Nulo"

            result = Cell.X if winner == Cell.X else Cell.O

    return result

print("El resultado es: ", analize([[Cell.O,Cell.X,Cell.O],
                                    [Cell.O,Cell.O,Cell.X],
                                    [Cell.O,Cell.X,Cell.X]]))

#0 1 2
#3 4 5
#6 7 8