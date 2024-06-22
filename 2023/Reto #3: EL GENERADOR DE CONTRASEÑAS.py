# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */
import random
import string

def gen_password(args):
    caracters  = string.ascii_lowercase + (string.ascii_uppercase if args[1] == 1 else '') + (string.digits if args[2] == 1 else '') + (string.punctuation if args[3] == 1 else '')
    print(caracters)

    lenght = 8 if args[0] == 0 else 16

    password= ''.join(random.choice(caracters) for _ in range(lenght))

    return password

print(f"La contraseña generada es: {gen_password([1,1,1,0])}")