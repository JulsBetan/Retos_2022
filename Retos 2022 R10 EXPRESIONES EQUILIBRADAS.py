""" /*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */ """

symbols_open = {"{":"}", "(":")", "[":"]"}
symbols_close = {"]":"[", ")":"(", "}":"{"}

def push(symbol, stack):
    stack.append(symbol)

def pop (stack):
    symbol = stack[-1]
    del stack[-1]
    return symbol

def isEmpty(stack):
    return len(stack) == 0
 
def isBalanced(expression):
    stack = []
    for char in expression:
        if symbols_open.get(char,"no" != "no"):
            push(char, stack)
        elif symbols_close.get(char,"no" != "no"):
            if isEmpty(stack):
                return "Cadena no balanceada " + expression 
            symbol = pop(stack)
            if symbol != symbols_close[char]:
                return "Cadena no balanceada " + expression 

    if isEmpty(stack):
        return "Cadena balanceada " + expression          
    else:
        return "Cadena no balanceada " + expression 

print(isBalanced("{a + b [c] * (2x2)}}}}"))
print(isBalanced("{ [ a * ( c + d ) ] - 5 }"))
print(isBalanced("{ a * ( c + d ) ] - 5 }"))
print(isBalanced("{a^4 + (((ax4)}"))
print(isBalanced("{ ] a * ( c + d ) + ( 2 - 3 )[ - 5 }"))
print(isBalanced("{{{{{{(}}}}}}"))
print(isBalanced("(a)")) 