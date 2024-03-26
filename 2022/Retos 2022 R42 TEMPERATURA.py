# /*
#  * Reto #42
#  * CONVERSOR DE TEMPERATURA
#  * Fecha publicación enunciado: 17/10/22
#  * Fecha publicación resolución: 24/10/22
#  * Dificultad: FÁCIL
#  *
#  * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
#  * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
#  * - En caso contrario retornará un error.
#  * - ¿Quieres emplear lo aprendido en este reto?
#  *   Revisa el reto mensual y crea una App: https://retosdeprogramacion.com/mensuales2022
#  */

def temperatura(temp):
    list = temp.split("˚")

    if len(list) != 2 or (list[1] != "C" and list[1] != "F"): 
        return "datos incorrectos"
    
    try:
        valor = float(list[0])
    except ValueError:
        return "datos incorrectos"

    return f"{(valor * 9/5) + 32}˚F" if list[1] == "C" else f"{(valor-32) * 5/9 }˚C"

print("La temperatura es", temperatura("100˚C"))
print("La temperatura es", temperatura("212˚F"))
print("La temperatura es", temperatura("212˚f"))
print("La temperatura es", temperatura("212"))
print("La temperatura es", temperatura("FC˚C"))