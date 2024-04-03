/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
 */

 let resultado_juego: [ [String] : String ] = [
    ["piedra", "papel"]: "papel",
    ["piedra", "tijera"]: "piedra",
    ["piedra", "lagarto"]: "piedra",
    ["piedra", "spock"]: "spock",
    ["papel", "piedra"]: "papel",
    ["papel", "tijera"]: "tijera",
    ["papel", "lagarto"]: "lagarto",
    ["papel", "spock"]: "papel",
    ["tijera", "piedra"]: "piedra",
    ["tijera", "papel"]: "tijera",
    ["tijera", "lagarto"]: "tijera",
    ["tijera", "spock"]: "spock",
    ["lagarto", "piedra"]: "piedra",
    ["lagarto", "papel"]: "lagarto",
    ["lagarto", "tijera"]: "tijera",
    ["lagarto", "spock"]: "lagarto",
    ["spock", "piedra"]: "spock",
    ["spock", "papel"]: "papel",
    ["spock", "tijera"]: "spock",
    ["spock", "lagarto"]: "lagarto"
]

func evalua_juego(tiradas: [[String]]) -> String {
    var p1 = 0
    var p2 = 0
    var found = 0
    for tirada in tiradas {
        let play1 = tirada[0].lowercased()
        let play2 = tirada[1].lowercased()

        var wins = ""

        found = 0
        if let result = resultado_juego[[play1, play2]]{
            wins = result
            found = 1
        }
        else if let result = resultado_juego[[play2, play1]] {   
            wins = result
            found = 1
        }

        if  found == 1 {
            if play1 == wins {
                p1 += 1
            }
            else{
                p2 += 1
            }
        }
    }

    return p1 > p2 ? "Player 1" : (p1 < p2 ? "Player 2" : "Empate")
}

print("Resultado: \(evalua_juego(tiradas: [["piedra","tijera"], ["tijera","piedra"], ["papel","tijera"]]))")
print("Resultado: \(evalua_juego(tiradas: [["spock","tijera"], ["spock","piedra"], ["papel","tijera"]]))")