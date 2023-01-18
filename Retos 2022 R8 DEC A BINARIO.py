""" /*
 * Reto #8
 * DECIMAL A BINARIO
 * Fecha publicación enunciado: 18/02/22
 * Fecha publicación resolución: 02/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */ """

def des_to_bin(decimal):
    x = decimal
    binario = ""
    while x > 0:
        bin = x % 2 
        x = int(x / 2) 
        binario = str(bin) + binario
    print(binario)

des_to_bin(13)

def recur_dec_bin (decimal):
    if decimal == 0:
        return ""
    else:
        return recur_dec_bin(int(decimal/2)) + str(decimal%2) 

print(recur_dec_bin(130))