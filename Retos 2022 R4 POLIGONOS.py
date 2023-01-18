""" /*π
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */ """

from inspect import _void

class Polygon():
    def area(self)->float:
        pass
    def printArea(self)->_void:
        pass

class Rectangulo(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self)->float:
        return self.width * self.height
    def printArea(self):
        print("El área del rectángulo es", self.area())

class Cuadrado(Polygon):
    def __init__(self, side):
        self.side = side
    def area(self)->float:
        return self.side * self.side
    def printArea(self):
        print("El área del cuadrado es", self.area())

class Triangulo(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self)->float:
        return self.base * self.height / 2
    def printArea(self):
        print("El área del triangulo es", self.area())

def area(polygon:Polygon):
    polygon.printArea()


area(Rectangulo(10,5))
area(Cuadrado(10))
area(Triangulo(10,10))