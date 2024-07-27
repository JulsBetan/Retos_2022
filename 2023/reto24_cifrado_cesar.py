# /*
#  * Crea un programa que realize el cifrado César de un texto y lo imprima.
#  * También debe ser capaz de descifrarlo cuando así se lo indiquemos.
#  *
#  * Te recomiendo que busques información para conocer en profundidad cómo
#  * realizar el cifrado. Esto también forma parte del reto.
#  */

import string

def cesar_cipher(string1, alpha):
    characters = string.ascii_uppercase
    result = ""
    for x in string1:
        for index, value in enumerate(characters):
            if value == x:
                result += characters[index + alpha if index+alpha < 26 else index+alpha-26  ]
    return result

def cesar_uncipher(string1, alpha):
    characters = string.ascii_uppercase
    result = ""
    for x in string1:
        for index, value in enumerate(characters):
            if value == x:
                result += characters[index - alpha if index-alpha >= 0 else 26 - (alpha-index)]
    return result

print(f"La palabra cifrada es {cesar_cipher("ZORRA", 3)}")

print(f"La palabra descifrada es {cesar_uncipher(cesar_cipher("ZORRA", 3), 3)}")