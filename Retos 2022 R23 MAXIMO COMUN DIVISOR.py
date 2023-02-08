# /*
#  * Reto #23
#  * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
#  * Fecha publicación enunciado: 07/06/22
#  * Fecha publicación resolución: 13/06/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
#  * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.

    # Divide el número más grande por el número más pequeño.
    # Si el residuo es cero, el más pequeño es el MCD.
    # Si el residuo no es cero, divide el número más pequeño por el residuo y repite los pasos 2 y 3 hasta que el residuo sea cero.
    # Entonces, el último número no nulo que se ha obtenido será el MCD.

    # Para calcular el MCD de 40 y 15 utilizando el algoritmo de Euclides:

    # Dividimos 40 entre 15 y el resultado es 2 con un residuo 10.
    # Luego, dividimos 15 entre 10 y el resultado es 1 con un residuo 5.
    # Ya que el residuo es 0, el MCD es 5.
    # Por lo tanto, el MCD de 40 y 15 es 5.
#  */

def MCD(num1, num2):
    while (num1%num2) > 0:
        num1, num2 = num2, (num1%num2)
    return num2

def MCM(num1, num2):
    return num1*num2/MCD(num1,num2)

print("El MCD es", MCD(54, 24))
print("El MCD es", MCD(40, 30))
print("El MCD es", MCD(40, 15))
print("El MCM es", MCM(40, 15))