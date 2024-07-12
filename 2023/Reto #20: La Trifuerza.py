# /*
#  *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  * 
#  *    *
#  *   ***
#  *  *   *
#  * *** ***
#  *
#  */

def triforce(n):
    base = (n * 2) - 1
    for i in range(n):
        print(' '*n + ' '*(n-i) + '*'*(i+1) + '*'*i)

    for i in range(n):
        print(' '*(n-i) + '*'*(i+1) + '*'*i + ' '*(n-i-1) +' '*(n-i) + '*'*(i+1) + '*'*i)
        
n = 10
triforce(n)
