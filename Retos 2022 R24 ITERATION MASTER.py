# /*
#  * Reto #24
#  * ITERATION MASTER
#  * Fecha publicación enunciado: 13/06/22
#  * Fecha publicación resolución: 20/06/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno). ¿De cuántas maneras eres capaz de hacerlo? Crea el código para cada una de ellas.
#  */

for x in range (1,101):
    print (x)

x=1
while x < 101:
    print (x)
    x+=1

print("Recursivo")
def to100(num):
    if num <= 100:
        print(num)
        to100(num+1)

to100(1)