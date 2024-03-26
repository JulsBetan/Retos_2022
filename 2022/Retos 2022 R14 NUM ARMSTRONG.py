""" /*
 * Reto #14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Fecha publicación enunciado: 04/04/22
 * Fecha publicación resolución: 11/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
 */ """

def isArmtrong(number):
    string = str(number)
    count = 0
    for digit in string:
        count += pow(int(digit),3)
    return count == number

print("Es número de Armstrong" if isArmtrong(372) else "NO es número de Armstrong") 