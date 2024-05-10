# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */
import random
from unidecode import unidecode

def get_list():
    file_name = "words.txt"
    try:
        with open(file_name, 'r') as file:
            word_list = file.read().splitlines()
        return word_list
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no se encontró.")
        return []
    
def get_word(list):
    word = list[random.randint(0, len(list)-1)]
    return unidecode(word.lower())

def get_masked(word):
    len_ = len(word)
    cont = len_ * 60 // 100

    positions = []

    while cont > 0:
        index = random.randint(0, len_-1)
        if  index not in positions:
            positions.append(index)
            cont -= 1
        
    array = list(word)

    for x in positions:
        array[x] = '_'
    return "".join(array), positions

def solved(array):
    if '_' not in array:
        return True
    else:
        return False

def start_game():
    word_list = get_list()
    word = get_word(word_list) 
    masked_word, index_array = get_masked(word)

    masked_array = list(masked_word)
    word_array = list(word)

    print(f"La palabra a adivinar es: {masked_word}")

    attempts = len(index_array)

    while attempts > 0:
       answer = input(f"Ingresa un caracter ({attempts} oportunidaded restantes): ") 
       answer = unidecode(answer.lower())

       if answer == word:
           return True

       attempts -= 1
       
       for index in index_array:    
            if answer == word_array[index]:
                masked_array[index] = answer

       print(f"Resultado: {''.join(masked_array)}") 

       if solved(masked_array) == True:
            return True

    print(f"Era: {word}")
    return False


def main():
    print("Haz adivinado!!" if start_game() else "Perdiste.")

if __name__ == "__main__":
    main() 