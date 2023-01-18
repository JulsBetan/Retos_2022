""" /*
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 */ """

def isAnagram(palabra1, palabra2):
    if palabra1==palabra2:
        return False
    
    return True if ''.join(sorted(palabra1, key=str.lower)) == ''.join(sorted(palabra2, key=str.lower)) else False


print("Es anagrama" if isAnagram("2Ho121laa","1aHo221la") else "No es anagrama")