# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  * 
#  * Ejemplo: 4
#  *         _
#  *       _|       
#  *     _|
#  *   _|
#  * _|
#  * 
#  */

def draw_scalator(steps):

    if steps == 0:
         print("__")
         return 

    h = abs(steps)*2+1
    v = abs(steps)+1
    grill = [[" "] * h for _ in range(v) ]


    if steps > 0:
        posh = h-1
    else:
        posh = 0
    char = '_'
    rango = 1
    
    for y in range(v):
        if y == 0:
            rango = 1
        else: 
            rango = 2

        for _ in range (rango):
            grill[y][posh] = char
            if steps > 0:
                posh -= 1
            else:
                posh += 1

            if char == '_':
                char = '|'
            else:
                char = '_'
    

    for x in grill:
        print("".join(x))

    return 


draw_scalator(4)
draw_scalator(-10)
     
#         _     
#       _|
#     _|
#   _|
# _|

# _
#  |_
#    |_
#      |_
#        |_