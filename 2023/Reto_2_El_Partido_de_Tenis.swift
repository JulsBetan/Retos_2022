/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

 let score: [Int: String] = [
    0: "Love",
    1: "15",
    2: "30",
    3: "40"
 ]

func tenis_match(moves: [String]) -> String{
    var m1=0
    var m2=0

    for move in moves{
        if move == "P1" {
            m1 += 1
            if m1 == 4 && m2 == 4 {
                m1 = 3
                m2 = 3 
            } else if m1 == 4{
                print("Ventaja P1")
            }   
            if m1 == 5 || (m1 == 4 && m2 < 3){
                return "P1"
            }   
        }
        else{
            m2 += 1
            if m2 == 4 && m1 == 4{
                m1 = 3
                m2 = 3 
            }else if m2 == 4{
                print("Ventaja P2")
            }
            if m2 == 5 || (m2 == 4 && m1 < 3){
                return "P2"
            }
        }
        if m1 < 3 || m2 < 3{
            print("\(score[m1]!) - \(score[m2]!)")
        }else if m1 == 3 && m2 == 3{
            print("Deuce")
        }

    }
    return "Nadie"
}


print("Ha ganado \(tenis_match(moves: ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2","P2","P2"]))")