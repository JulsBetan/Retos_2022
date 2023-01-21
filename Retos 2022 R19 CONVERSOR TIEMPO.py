""" /*
 * Reto #19
 * CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
 */ """

def milisecs(days, hours, mins, secs):
    return days*24*60*60*1000 + hours*60*60*1000 + mins*60*1000 + secs*1000

print("Milisegundos:", milisecs(1,0,0,0))