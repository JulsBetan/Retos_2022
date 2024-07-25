# /*
#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗ ═════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */

def espiral(size):
	print (f"La espiral tiene tamaño: {size}.")

	if size < 5 :
		raise ValueError("El tamaño mínimo de la espiral es 5. ")
    
	array = [list('#'*size) for _ in range(size)]    
	horizontal = True
	positive = True
	indX = 0
	indY = 0
	menorX = 0
	mayorX = size-1
	menorY = 0
	mayorY = size-1
	
	array[0][0] = '═'
	for pos in range(1, size*size):
		if horizontal:
			if positive:
				indY += 1
			else:
				indY -= 1

			if indY == mayorY and positive:
				menorX += 1
				char = '╗'
				horizontal = False
			elif indY == menorY and not positive:
				mayorX -= 1
				char = '╚' 
				positive = False
				horizontal = False
			else:
				char = '═'
		else:
			if positive:
				indX += 1
			else:
				indX -= 1

			if indX == mayorX and positive:
				mayorY -= 1
				char = '╝'
				horizontal = True
				positive = False
			elif indX == menorX and not positive:
				menorY += 1
				char = '╔' 
				positive = True
				horizontal = True
			else:
				char = '║'

		array[indX][indY] = char
	for row in array:
		print("".join(x for x in row))

size = int(input("Introduzca el tamaño de la espiral:"))
espiral(size)

	
