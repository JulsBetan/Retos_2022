/*
#  * Reto #41
#  * LA LEY DE OHM
#  * Fecha publicación enunciado: 10/10/22
#  * Fecha publicación resolución: 17/10/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
#  * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
#  * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
#  *
*/

import Foundation

// func ohm(v: Double? = nil, r: Double? = nil, i: Double? = nil) -> String {

//     if let v, let r, i == nil {
//         return "I = \(String(format: "%.2f", v / r))"
//     } else if let v, let i, r == nil {
//         return "R = \(String(format: "%.2f", v / i))"
//     } else if let r, let i, v == nil {
//         return "V = \(String(format: "%.2f", r * i))"
//     }

//     return "Invalid values"
// }

func ley_ohm(v:Double? = nil, r:Double? = nil, i:Double? = nil)->String{
    if let v, let r, i == nil{
        return "i=\(String(format:"%.2f", v/r))"
    }else if let v, let i, r == nil{
        return "r=\(String(format:"%.2f", v/i))"
    }else if let r, let i, v == nil{
        return "v=\(String(format:"%.2f", r*i))"
    }
    return "Invalid values"
}

print("El resultado es", ley_ohm(v:10,r:20.52323))
print("El resultado es", ley_ohm(r:20.52323,i:10))

// print("El resultado es", ohm(v:10,r:20.52323))
// print("El resultado es", ohm(r:20.52323,i:10))

// print(ohm())
// print(ohm(v: 5.0))
// print(ohm(v: 5.0, r: 4.0))