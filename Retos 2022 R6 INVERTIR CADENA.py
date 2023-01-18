""" /*
 * Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 14/02/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 * """

def invertString(string):
    return "".join([string[x-1] for x in range (len(string), 0, -1)])

print(invertString("Hola mundo"))


def invertRecursive(string):
    if len(string) == 0:
        return string
    else:
        return invertRecursive(string[1:]) + string[0] 

print(invertRecursive("Hola mundo"))
