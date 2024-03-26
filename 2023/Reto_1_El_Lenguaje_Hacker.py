# /*
# * Escribe un programa que reciba un texto y transforme lenguaje natural a
# * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
# *  se caracteriza por sustituir caracteres alfanuméricos.
# * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
# *   con el alfabeto y los números en "leet".
# *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
# */

leet_dict = {
    'a': '4',
    'b': '8',
    'c': '<',
    'd': '|)',
    'e': '3',
    'f': '|=',
    'g': '9',
    'h': '|-|',
    'i': '1',
    'j': '_|',
    'k': '|<',
    'l': '|_',
    'm': '|\/|',
    'n': '|\\|',
    'o': '0',
    'p': '|>',
    'q': '(,)',
    'r': '|2',
    's': '5',
    't': '7',
    'u': '|_|',
    'v': '\/',
    'w': '\^/',
    'x': '><',
    'y': '`/',
    'z': '2'
}

def str_to_leet(cadena: str) ->str:
    text = input("Ingresa texto:  ")
    return "".join(leet_dict.get(char.lower(), char) for char  in text)

print (str_to_leet("leet"))