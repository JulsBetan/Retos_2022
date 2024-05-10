# /*
#  * Crea una función que sea capaz de transformar Español al lenguaje básico del universo
#  * Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *  
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */

import string
from unidecode import unidecode

aurebesh_dict = {
    'A': 'Ⰿ', 'B': 'Ⱆ', 'C': 'Ⱎ', 'D': 'Ⰻ', 'E': 'Ⰳ',
    'F': 'Ⱒ', 'G': 'Ⱋ', 'H': 'Ⱀ', 'I': 'Ⰺ', 'J': 'Ⱂ',
    'K': 'Ⱇ', 'L': 'Ⱄ', 'M': 'Ⰾ', 'N': 'Ⰽ', 'O': 'Ⰰ',
    'P': 'Ⱅ', 'Q': 'Ⱐ', 'R': 'Ⱏ', 'S': 'Ⱍ', 'T': 'Ⱌ',
    'U': 'Ⰲ', 'V': 'Ⱓ', 'W': 'ⰋⰀ', 'X': 'Ⱗ', 'Y': 'Ⱔ',
    'Z': 'ⰖⰠ'
}

aurebesh_alphabet = [
    'Ⰿ', 'Ⱆ', 'Ⱎ', 'Ⰻ', 'Ⰳ', 'Ⱒ', 'Ⱋ', 'Ⱀ', 'Ⰺ', 'Ⱂ',
    'Ⱇ', 'Ⱄ', 'Ⰾ', 'Ⰽ', 'Ⰰ', 'Ⱅ', 'Ⱐ', 'Ⱏ', 'Ⱍ', 'Ⱌ',
    'Ⰲ', 'Ⱓ', 'ⰋⰀ', 'Ⱗ', 'Ⱔ', 'ⰖⰠ'
]

opuesto_dict = {
    'Ⰿ': 'A', 'Ⱆ': 'B', 'Ⱎ': 'C', 'Ⰻ': 'D', 'Ⰳ': 'E',
    'Ⱒ': 'F', 'Ⱋ': 'G', 'Ⱀ': 'H', 'Ⰺ': 'I', 'Ⱂ': 'J',
    'Ⱇ': 'K', 'Ⱄ': 'L', 'Ⰾ': 'M', 'Ⰽ': 'N', 'Ⰰ': 'O',
    'Ⱅ': 'P', 'Ⱐ': 'Q', 'Ⱏ': 'R', 'Ⱍ': 'S', 'Ⱌ': 'T',
    'Ⰲ': 'U', 'Ⱓ': 'V', 'ⰋⰀ': 'W', 'Ⱗ': 'X', 'Ⱔ': 'Y',
    'ⰖⰠ': 'Z'
}

def to_aurebesh(text):
    return ''.join([aurebesh_dict[x] if x in string.ascii_uppercase else x for x in list(text)])

def from_aurebesh(text):
    return ''.join([opuesto_dict[x] if x in aurebesh_alphabet else x for x in list(text)])
    

text = "Hola cara de bola malparida"
print(f"El texto en Aurebesh es: {to_aurebesh(unidecode(text.upper()))}")

print(f"El texto de Aurebesh a Español: {from_aurebesh(to_aurebesh(unidecode(text.upper())))}")