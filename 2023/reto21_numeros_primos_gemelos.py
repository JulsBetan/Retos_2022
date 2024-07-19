# /*
#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  * 
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)
#  */

def is_primo(num):

    if num < 2:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def primos(rango):
    if rango < 5:
        raise ValueError("El numero menor aceptado para el rango es 5.")
    
    list = []
    num1 = 3
    num2 = 0
    for x in range(5, rango+1):
        if is_primo(x):
            num2 = x
            if num2 - num1 == 2:
                list.append((num1, num2))
            num1 = num2 
    
    return list

print(primos(14))
