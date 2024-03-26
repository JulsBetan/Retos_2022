# /*
#  * Reto #30
#  * MARCO DE PALABRAS
#  * Fecha publicación enunciado: 26/07/22
#  * Fecha publicación resolución: 01/08/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
#  * un marco rectangular de asteriscos.
#  * - ¿Qué te parece el reto? Se vería así:
#  *   **********
#  *   * ¿Qué   *
#  *   * te     *
#  *   * parece *
#  *   * el     *
#  *   * reto?  *
#  *   **********
#  */

def word_square(message):
    max_len = 0
    for x in message.split():
        if (len(x) > max_len):
            max_len = len(x)

    line = "".join("*" for x in range(0, max_len+4))
    print(line)
    for x in message.split():
        print("* " + x + "".join(" " for y in range(0,max_len-len(x))) + " *")
    print(line)

word_square("Hola este es un ejercicio de programación")

word_square("Hijo de la gran puta")

word_square("No pain, no gain")