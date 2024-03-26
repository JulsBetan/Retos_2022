""" /*
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 */ """

from datetime import datetime, timedelta

def difference(date1, date2):
    fec1 = datetime.strptime(date1, "%d/%m/%Y")
    fec2=datetime.strptime(date2, "%d/%m/%Y")
    return (fec2-fec1).days

print("La diferencia en días es:",difference("28/12/1978","28/12/2022"))