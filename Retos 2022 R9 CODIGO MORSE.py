""" /*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
 */ """

naturalDict = {"A":".—", "N":"—.", "0":"—————",
                "B":"—...", "Ñ":"——.——", "1":".————",
                "C":"—.—.", "O":"———", "2":"..———",
                "CH":"————", "P":".——.", "3":"...——",
                "D":"—..", "Q":"——.—", "4":"....—",
                "E":".", "R":".—.", "5":".....",
                "F":"..—.", "S":"...", "6":"—....",
                "G":"——.", "T":"—", "7":"——...",
                "H":"....", "U":"..—", "8":"———..",
                "I":"..", "V":"...—", "9":"————.",
                "J":".———", "W":".——", ".":".—.—.—",
                "K":"—.—", "X":"—..—", ",":"——..——",
                "L":".—..", "Y":"—.——", "?":"..——..",
                "M":"——", "Z":"——..", "\"":".—..—.", "/":"—..—.", " ":" "}

def code(cadena):
    cadena = cadena.upper().split()
    coded = ''
    for word in cadena:
        for char in word:
            coded += naturalDict[char] + " "
        coded += " "
    return coded

def decode(cadena):
    list = cadena.split("  ")
    decoded = ''
    for word in list:
        char_list = word.split()
        for char in char_list:
            for key, value in naturalDict.items():
                if value == char:
                    decoded += key
                    break 
        decoded += " "
    return decoded

mensaje = "perro"

coded = code(mensaje)

print(coded)

print("El mensaje es:",decode(coded))

print("Mensaje:",decode(".... ——— .—.. .—  —— ——— — .... . .—. ..—. ..— —.—. —.— . .—."))



