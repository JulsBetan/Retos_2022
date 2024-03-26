/*
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

let leet_dict: [Character:  String] = [
    "a": "4",
    "b": "8",
    "c": "<",
    "d": "|)",
    "e": "3",
    "f": "|=",
    "g": "9",
    "h": "|-|",
    "i": "1",
    "j": "_|",
    "k": "|<",
    "l": "|_",
    "m": "|\\/|",
    "n": "|\\|",
    "o": "0",
    "p": "|>",
    "q": "(,)",
    "r": "|2",
    "s": "5",
    "t": "7",
    "u": "|_|",
    "v": "\\/",
    "w": "\\^/",
    "x": "><",
    "y": "`/",
    "z": "2"
]

func str_to_leet(cadena: String) -> String{
    var textoleet = ""

    for caracter in cadena.lowercased(){
        if let leetCaracter = leet_dict[caracter]{
            textoleet.append(leetCaracter)
        } else {
            textoleet.append(caracter)
        }
    }
    return textoleet
}


print("Ingresa texto: ")
if let text = readLine(){
print ("Resultado: \(str_to_leet(cadena: text))")
} else{
    print("No se ingreso  ningun texto")
}