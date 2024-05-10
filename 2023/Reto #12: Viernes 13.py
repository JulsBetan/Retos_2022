# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */
import datetime

def isthereFriday13(month, year):

    first_day = datetime.date(year, month, 13)

    day_week = first_day.weekday()

    print(first_day, day_week)

    return "Tiene viernes trece!!" if day_week ==  4 else "No tiene viernes 13"


month = 4
year = 2012

print(f"El mes y año {str(month)+'/'+str(year)}: {isthereFriday13(month, year)}" ) 

