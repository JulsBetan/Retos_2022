# /*
#  * Crea una función que dibuje una espiral como la del ejemplo.
#  * - Únicamente se indica de forma dinámica el tamaño del lado.
#  * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
#  *
#  * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  * ════╗
#  * ╔══╗║
#  * ║╔╗║║
#  * ║╚═╝║
#  * ╚═══╝
#  */

def espiral(size):
	print (f"La espiral tiene tamaño: {size}.")

	if size < 5 :
		raise ValueError("El tamaño mínimo de la espiral es 5. ")
        
size = int(input("Introduzca el tamaño de la espiral:"))
espiral(size)

	
