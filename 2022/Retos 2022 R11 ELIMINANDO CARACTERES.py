""" /*
 * Reto #11
 * ELIMINANDO CARACTERES
 * Fecha publicación enunciado: 14/03/22
 * Fecha publicación resolución: 21/03/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
 */ """

def eliminate(string1, string2):
    out1 = ""
    out2 = ""
    
    for x in string1:
        if x not in string2:
            out1 += x

    for x in string2:
        if x not in string1:
            out2 += x

    return out1, out2

result1, result2 =  eliminate("Hola mundo","Hola motherfucker")

print("Cadena 1", result1)
print("Cadena 2", result2)