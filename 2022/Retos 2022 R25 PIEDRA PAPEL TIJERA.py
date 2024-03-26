# /*
#  * Reto #25
#  * PIEDRA, PAPEL, TIJERA
#  * Fecha publicación enunciado: 20/06/22
#  * Fecha publicación resolución: 27/06/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
#  * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
#  */
from enum import Enum

class Play(Enum):
    R = "R"
    S = "S"
    P = "P"

class Result(Enum):
    Player1 = "Player1"
    Player2 = "Player2"
    Tie = "Tie"

def analize(plays):
    win1 = 0
    win2 = 0
    for x in plays:
        #print(x[0],x[1])
        if (x[0] == Play.P and x[1] == Play.R) or (x[0] == Play.S and x[1] == Play.P) or (x[0] == Play.R and x[1] == Play.S):
            win1 += 1
        if (x[1] == Play.P and x[0] == Play.R) or (x[1] == Play.S and x[0] == Play.P) or (x[1] == Play.R and x[0] == Play.S):
            win2 += 1

    
    return Result.Tie.name if win1 == win2 else (Result.Player1.name if win1 > win2 else Result.Player2.name)
    

print ("El ganador es", analize([(Play.R,Play.P),(Play.R,Play.R)]))
print ("El ganador es", analize([(Play.R,Play.P),(Play.R,Play.S),(Play.R,Play.S)]))
print ("El ganador es", analize([(Play.R,Play.P),(Play.R,Play.S),(Play.R,Play.R),(Play.R,Play.R)]))