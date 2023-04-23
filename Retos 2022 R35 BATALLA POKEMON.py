# /*
#  * Reto #35
#  * BATALLA POKÉMON
#  * Fecha publicación enunciado: 29/08/22
#  * Fecha publicación resolución: 06/09/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
#  * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
#  * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
#  * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
#  * - El programa recibe los siguientes parámetros:
#  *  - Tipo del Pokémon atacante.
#  *  - Tipo del Pokémon defensor.
#  *  - Ataque: Entre 1 y 100.
#  *  - Defensa: Entre 1 y 100.
#  */

from enum import Enum

class PokemonType(Enum):
    water = "Agua"
    fire = "Fuego"
    grass = "Planta"
    electric = "Electrico" 

class PokemonChart:
    def __init__(self, effective: PokemonType, notEffective: PokemonType):
        self.effective = effective
        self.notEffective = notEffective

def battle(attacker, defender, attack, defense):

    typeChart = {
    PokemonType.water: PokemonChart(effective=PokemonType.fire, notEffective=PokemonType.grass),
    PokemonType.fire: PokemonChart(effective=PokemonType.grass, notEffective=PokemonType.water),
    PokemonType.grass: PokemonChart(effective=PokemonType.water, notEffective=PokemonType.fire),
    PokemonType.electric: PokemonChart(effective=PokemonType.water, notEffective=PokemonType.grass)
    }

    effectivity = 1.0

    if attacker == defender or typeChart[attacker].notEffective  == defender:
        effectivity = 0.5
        print("No es muy efectivo")
    elif typeChart[attacker].effective  == defender:
        effectivity = 2.0
        print("Es súper efectivo")
    else:
        print("Es neutro")
    

    return 50 * attack / defense * effectivity

print(battle( PokemonType.water, PokemonType.fire, 50, 30))
print(battle( PokemonType.water, PokemonType.fire, 101, -10))
print(battle( PokemonType.fire, PokemonType.water, 50, 30))
print(battle( PokemonType.fire, PokemonType.fire, 50, 30))
print(battle( PokemonType.grass, PokemonType.electric, 30, 50))