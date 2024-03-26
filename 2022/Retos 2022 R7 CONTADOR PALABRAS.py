""" /*
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 */ """
import string

def cuenta_palabras(cadena):
    traduccion = str.maketrans("","",string.punctuation)

    cadena = cadena.translate(traduccion)

    lista = cadena.split()

    word_list = {}

    for x in lista:
        x = x.lower()
        if x in word_list:
            word_list[x] += 1
        else:
            word_list[x] = 1

    for x,valor in word_list.items():
        print(x, valor)

cuenta_palabras("Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev).")
