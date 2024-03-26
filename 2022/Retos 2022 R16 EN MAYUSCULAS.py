""" /*
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente."""

def uppercase (string):
    new_char = ""

    ant_espacio = 1
    for char in string:
        if ant_espacio == 1 and char != " ":
            new_char += chr(ord(char)-32)
            ant_espacio = 0
        elif char == " ":
            ant_espacio = 1
            new_char += char
        else:
            new_char += char

    return new_char


print("La cadena es:", uppercase("hola cara de perro como estas?")) 