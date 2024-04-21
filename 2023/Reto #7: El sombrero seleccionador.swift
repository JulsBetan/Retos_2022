/*
 * Crea un programa que simule el comportamiento del sombrero seleccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

import Foundation

class HatQuestion{
    let question: String
    let answers: [(String, String)]
    init(question: String, answers: [(String, String)]) {
        self.question = question
        self.answers = answers
    }
}

func get_answer() -> Int {

    print("Responde 1, 2, 3 o 4: ")
    
    if let answer = readLine(), let intAnswer = Int(answer), (1...4).contains(intAnswer)  {
        return intAnswer
    } else {
        return get_answer()
    }
}

print("Hola, soy el \"Sombrero Seleccionador\"\nTendrás que responder cinco preguntas para ayudarme a descubrir tu casa de Hogwarts.\n")

let hat_questions = [HatQuestion(question: "¿Cómo te definirías?", answers: [
                            ("1. Valiente", "gryffindor"),
                            ("2. Leal", "hufflepuff"),
                            ("3. Sabio", "ravenclaw"),
                            ("4. Ambicioso", "slytherin")]),
                 HatQuestion(question: "¿Cuál es tu clase favorita?", answers: [
                            ("1. Vuelo", "gryffindor"),
                            ("2. Pociones", "ravenclaw"),
                            ("3. Defensa contra las artes oscuras", "slytherin"),
                            ("4. Animales fantásticos", "hufflepuff")]),
                 HatQuestion(question: "¿Dónde pasarías más tiempo?", answers: [
                            ("1. Invernadero", "hufflepuff"),
                            ("2. Biblioteca", "ravenclaw"),
                            ("3. En la sala común", "slytherin"),
                            ("4. Explorando", "gryffindor")]),
                 HatQuestion(question: "¿Cuál es tu color favorito?", answers: [
                            ("1. Rojo", "gryffindor"),
                            ("2. Azul", "ravenclaw"),
                            ("3. Verde", "slytherin"),
                            ("4. Amarillo", "hufflepuff")]),
                 HatQuestion(question: "¿Cuál es tu mascota?", answers: [
                            ("1. Sapo", "ravenclaw"),
                            ("2. Lechuza", "gryffindor"),
                            ("3. Gato", "hufflepuff"),
                            ("4. Serpiente", "slytherin")])]


var houses = [
    "gryffindor": 0,
    "hufflepuff": 0,
    "ravenclaw": 0,
    "slytherin": 0
]

for hat_question in hat_questions {
    print(hat_question.question)
    for (_, hat_answer) in hat_question.answers.enumerated() {
        print("\(hat_answer.0)")
    }

    let answer = get_answer()
    let house = hat_question.answers[answer - 1].1
    houses[house]! += 1

    print()
}

var selected_house: [String] = []
var max_points = 0

print(houses)

for (house, points) in houses {
    if points > max_points {
        selected_house.removeAll()
        selected_house.append(house)
        max_points = points
    } else if points == max_points {
        selected_house.append(house)
        max_points = points
    }
}

if selected_house.count == 1 {
    print("Lo tengo claro... ¡\(selected_house[0].capitalized)!")
} else {
    print("Ha estado complicado... ¡\(selected_house.randomElement()!.capitalized)!")
}