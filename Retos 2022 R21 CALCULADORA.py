#  /*
#  * Reto #21
#  * CALCULADORA .TXT
#  * Fecha publicación enunciado: 23/05/22
#  * Fecha publicación resolución: 01/06/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
#  * 

def main():
    operation = ""
    ban1 = 0
    ban2 = 0 
    op1 = 0
    op2 = 0 
    result = "Error"
    with open("Challenge21.txt", "r") as file:
        content = file.readlines()

    for line in content:
        operation += line
        if not line.isnumeric():
            if (ban1 == 0):
                result = 'Error'
                break
            else:
                if line == "+":
                    result = op1 + op2 
                elif line == "-":
                    result = op1 - op2 
                elif line == "*":
                    result = op1 * op2
                elif line == "/":
                    result = op1 / op2
                else:
                    result = "Err"
                    break
            op1 = result
        else:
            if ban1 == 0:
                op1 = float(line)
                ban1 = 1
            else:
                op2 = float(line)

    
    print("operacion", " ".join(x for x in operation.split()), " = ", result)


if __name__ == "__main__":
    main()