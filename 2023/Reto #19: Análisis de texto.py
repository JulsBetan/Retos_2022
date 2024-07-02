# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.
#  */

def analize_text(text):
    array = text.split()
    word_count = len(array)
    phrases = len(text.split("."))
    print(f'Número palabras: {word_count}')
    length = 0
    max = 0
    max_word = ""
    for x in array:
        length += len(x)
        if len(x) > max:
            max = len(x)
            max_word = x
    print(f'Logitud media palabras: {length/word_count}')
    print(f'Número de oraciones: {phrases}')
    print(f'Palabra más larga: {max_word} mide {max}')
    


text = """Cada semana se publica un nuevo reto y se corrige en directo desde Twitch el reto de la semana pasada.
En la sección "Eventos" de nuestro servidor de Discord encontrarás el día y horario por país de los directos.
Puedes utilizar cualquier lenguaje de programación, y encontrar tanto mis correcciones como las de la comunidad en el directorio de cada reto.
¿Quieres participar? Te lo explico en la sección ¿Cómo puedo participar? en este mismo documento.
Los retos no tienen relación entre ellos. Puedes resolverlos de manera totalmente independiente. Simplemente revisa su nivel de dificultad.
Una vez se haya cumplido la semana de publicación del reto, podrás consultar mi corrección y las de la comunidad en cualquier lenguaje de programación.v"""

analize_text(text)