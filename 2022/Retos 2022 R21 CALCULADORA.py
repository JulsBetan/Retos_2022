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
#  */

def main():
    operation = ""
    ban1 = 0
    op1 = 0
    op2 = 0 
    symbol = ""
    result = 0
    res = ""
    with open("Challenge21.txt", "r") as file:
        content = file.readlines()

    # 5 + 10.1 - 2 * 3 / 1
    content = [x.strip() for x in content]

    for line in content:
        operation += line
        if  line.isnumeric() or line.replace('.','').isdigit():
            if ban1 == 0:
                op1 = float(line)
                ban1 = 1
            else:
                op2 = float(line)
                if symbol == "+":
                    result = op1 + op2 
                elif symbol == "-":
                    result = op1 - op2 
                elif symbol == "*":
                    result = op1 * op2
                elif symbol == "/":
                    result = op1 / op2
                else:
                    res = "Error"
                    break
                op1 = result    
            
        else:
            if (ban1 == 0):
                res = 'Error'
                break
            
            if line == "+" or line == "-" or line == "*" or line == "/":
                symbol = line
            else:
                res = "Error"
                break

    
    print("operacion", " ".join(x for x in operation.split()), " = ", "Error" if res == "Error" else result)


if __name__ == "__main__":
    main()