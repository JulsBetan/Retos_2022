# /*
#  * Reto #22
#  * CONJUNTOS
#  * Fecha publicación enunciado: 01/06/22
#  * Fecha publicación resolución: 07/06/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
#  * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
#  * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
#  *

def common(cad1, cad2, bool):
    result = []
    if bool:
        for x in cad1:
            if x in cad2 and x not in result:
                result.append(x) 
    else:
        to_remove=[]
        for x in cad1:
            if x in cad2:
                to_remove.append(x)
                cad2.remove(x)

        for x in to_remove:
            while x in cad1:
                cad1.remove(x)
            while x in cad2:
                cad2.remove(x)
        result = cad1 + cad2
    return result

print("El resultado", common([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], True))

print("El resultado", common([1, 2, 3, 3, 4], [2, 2, 3, 3, 3, 4, 6], False))

