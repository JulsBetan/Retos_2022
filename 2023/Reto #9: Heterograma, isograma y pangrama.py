# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */

from unidecode import unidecode

dictionary = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

def count_dict(text):
    for x in dictionary:
        dictionary[x] = 0
    
    text_lower = unidecode(text.lower())
    for x in text_lower:
        if x in dictionary:
            dictionary[x] += 1



def is_heterograma(text):

    count_dict(text)

    for _, value in dictionary.items():
        if value > 1:
            return False

    return True

def is_isograma(text):
    count_dict(text)

    max = 0 

    for _, value in dictionary.items():
        if max  == 0:
            max = value
        elif max != value and value != 0:     
            return False

    return True

def is_pangrama(text):
    count_dict(text)

    for _, value in dictionary.items():
        if value == 0:     
            return False

    return True

def main():
    phrase  = "mezquitas mezquitas"
    print(f"La frase {phrase} {'es' if is_heterograma(phrase) else 'no es' } heterograma, {'es' if is_isograma(phrase) else 'no es'} isograma y {'es' if is_pangrama(phrase) else 'no es' } pangrama")
    phrase  = "Heterograma"
    print(f"La frase {phrase} {'es' if is_heterograma(phrase) else 'no es' } heterograma, {'es' if is_isograma(phrase) else 'no es'} isograma y {'es' if is_pangrama(phrase) else 'no es' } pangrama")
    phrase  = "The quick brown fox jumps over the lazy dog."
    print(f"La frase {phrase} {'es' if is_heterograma(phrase) else 'no es' } heterograma, {'es' if is_isograma(phrase) else 'no es'} isograma y {'es' if is_pangrama(phrase) else 'no es' } pangrama")

if __name__ == "__main__":
    main()