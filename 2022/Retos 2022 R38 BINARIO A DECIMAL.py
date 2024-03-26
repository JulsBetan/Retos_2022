# /*
#  * Reto #38
#  * BINARIO A DECIMAL
#  * Fecha publicación enunciado: 19/09/22
#  * Fecha publicación resolución: 27/09/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
#  * funciones propias del lenguaje que lo hagan directamente.
#  */

def binary_to_decimal(binary):
    power = len(binary)-1
    decimal = 0
    for x in binary:
        decimal += int(x) * 2 ** power
        power -= 1
    return decimal

print("El decimal es", binary_to_decimal("00110"))
print("El decimal es", binary_to_decimal("01100"))