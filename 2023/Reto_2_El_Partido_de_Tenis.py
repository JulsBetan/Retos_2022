# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por 'P1' (Player 1) o 'P2' (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son 'Love' (cero), 15, 30, 40, 'Deuce' (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */

# 0 love
# 1 15
# 2 30
# 3 40
# 4 ventaja
# 5 punto 

score = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40"
}

def tenis_match(moves) -> str:
    m1=0
    m2=0
    result=0j

    for move in moves:
        if move == "P1":
            m1 += 1
            if m1 == 4 and m2 == 4:
                m1 = 3
                m2 = 3 
            elif m1 == 4:
                print("Ventaja P1")
            if m1 == 5 or (m1 == 4 and m2 < 3):
                return "P1"
        else:
            m2 += 1
            if m2 == 4 and m1 == 4:
                m1 = 3
                m2 = 3 
            elif m2 == 4:
                print("Ventaja P2")
            if m2 == 5 or (m2 == 4 and m1 < 3):
                return "P2"

        if m1 < 3 or m2 < 3:
            print(f"{score.get(m1)} - {score.get(m2)}")
        elif m1 == 3 and m2 == 3:
            print("Deuce")


    return 'Nadie'

print(f"Ha ganado {tenis_match(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2','P2','P2'])}")