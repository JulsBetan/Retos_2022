# /*
#  * Reto #26
#  * CUADRADO Y TRIÁNGULO 2D
#  * Fecha publicación enunciado: 27/06/22
#  * Fecha publicación resolución: 07/07/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
#  * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
#  * - EXTRA: ¿Eres capaz de dibujar más figuras?
#  */

def square (side):
    vertical = "".join("* " for x in range (0,side))
    horizontal = "*" + "".join(" " for x in range (0,side*2-3)) + "*"
    print(vertical)
    for x in range(side-2):
        print(horizontal)        
    print(vertical)   

def triangle(side):
    for x in range (1,side):
        print("".join(("* " if (y==0 or y == x-1) else "  " ) for y in range (x)))
    print("".join("* " for x in range (0,side)))

def triangle2(side):
    for x in range (1,side+1):
        print("".join(("* " if (y==0 or y == x-1) else "  " ) for y in range (x)))
    for x in range (side+1, 0, -1):
        print("".join(("* " if (y==0 or y == x-1) else "  " ) for y in range (x)))
    #print("".join("* " for x in range (0,side)))
    
# square(15)
# triangle(15)
triangle2(15)
