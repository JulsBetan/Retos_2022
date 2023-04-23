# /*
#  * Reto #33
#  * CICLO SEXAGENARIO CHINO
#  * Fecha publicación enunciado: 15/08/22
#  * Fecha publicación resolución: 22/08/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
#  * en el ciclo sexagenario del zodíaco chino.
#  * - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
#  * - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
#  *   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
#  *   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
#  * - Cada elemento se repite dos años seguidos.
#  * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
#  */

element = ["madera", "madera", "fuego", "fuego", "tierra", "tierra", "metal", "metal", "agua", "agua"]

animal = ["rata", "buey", "tigre", "conejo", "dragon", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]

def getChineseYear(year):
    diff = year - 1984
    pos = True
    if diff >= 0:
        pos = True
        diff += 1
    else:
        pos = False
        diff = abs(diff)
        rev_element = list(reversed(element))
        rev_animal = list(reversed(animal))
    
    print ("La diferecia es ", diff)

    indE = 0
    indA = 0

    for x in range (1, diff+1):
        
        if x == diff:
            if pos:
                print("El año chino de", year, "es",animal[indA].capitalize(),"de",element[indE].capitalize())
            else:
                print("El año chino de", year, "es",rev_animal[indA].capitalize(),"de",rev_element[indE].capitalize())
        indE = indE+1 if indE+1 < 10 else 0
        indA = indA+1 if indA+1 < 12 else 0

getChineseYear(3000)
getChineseYear(1978)
getChineseYear(1990)
