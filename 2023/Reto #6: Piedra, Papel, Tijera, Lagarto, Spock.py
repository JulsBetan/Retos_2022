# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  */

from typing import  List

resultado_juego = {
    ("piedra", "papel"): "papel",
    ("piedra", "tijera"): "piedra",
    ("piedra", "lagarto"): "piedra",
    ("piedra", "spock"): "spock",
    ("papel", "piedra"): "papel",
    ("papel", "tijera"): "tijera",
    ("papel", "lagarto"): "lagarto",
    ("papel", "Spock"): "papel",
    ("tijera", "piedra"): "piedra",
    ("tijera", "papel"): "tijera",
    ("tijera", "lagarto"): "tijera",
    ("tijera", "spock"): "spock",
    ("lagarto", "piedra"): "piedra",
    ("lagarto", "papel"): "lagarto",
    ("lagarto", "tijera"): "tijera",
    ("lagarto", "spock"): "lagarto",
    ("spock", "piedra"): "spock",
    ("spock", "papel"): "papel",
    ("spock", "tijera"): "spock",
    ("spock", "lagarto"): "lagarto"
}

def evalua_juego(tiradas: List[str]) -> str:
    p1 = 0
    p2 = 0
    found = 0
    for play1, play2 in tiradas:
        found = 0
        if (play1.lower(), play2.lower()) in resultado_juego:
            wins = resultado_juego[(play1.lower(), play2.lower())]
            found = 1
        elif (play2.lower(), play1.lower()) in resultado_juego:   
            wins = resultado_juego[(play2.lower(), play1.lower())]
            found = 1

        if  found == 1:
            if play1 == wins:
                p1 += 1
            else:
                p2 += 1
    
    return "Player 1" if p1 > p2 else ("Player 2"  if p1 < p2 else "Empate")

print(f"Resultado: {evalua_juego([('piedra','tijera'), ('tijera','piedra'), ('papel','tijera')])}")
print(f"Resultado: {evalua_juego([('spock','tijera'), ('spock','piedra'), ('papel','tijera')])}")


