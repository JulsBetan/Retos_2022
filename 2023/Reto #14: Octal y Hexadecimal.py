# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

hexa = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'A',
    11:'B',
    12:'C',
    13:'D',
    14:'E',
    15:'F'
}

def to_octal(number):
    if  number // 8 == 0:
        return number % 8
    
    return int(str(to_octal(number // 8)) + str(number % 8))

def to_hexadecimal(number):
    if  number // 16 == 0:
        return hexa[number % 18]
    
    return to_hexadecimal(number // 16) + hexa[number % 16]
    
number = 123
print(f"El octal de {number} es {to_octal(number)}")
print(f"El hexadecimal de {number} es {to_hexadecimal(number)}")