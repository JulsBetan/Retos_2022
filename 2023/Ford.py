# print(list(reversed(range(1,11))))

# print(list(range(1,11)).reverse())

class Drink:
    def __init__(self, name) -> None:
       self.__name = name
    def getDetail(self):
        return "la bebida es: " + self.__name

class Product:
    def __init__(self, cost, price) -> None:
       self.cost = cost
       self.price = price 
    def getGain(self):
        return self.price - self.cost

class Beer(Drink, Product):
    cont = 0

    def __init__(self, name, brand, alcohol, cost, price) -> None:
        Drink.__init__(self, name)
        Product.__init__(self, cost, price)
        self.__brand = brand
        self.__alcohol = alcohol
        Beer.cont += 1
    def getDetail(self):
        return super().getDetail() + " de marca: " + self.__brand + " con " + str(self.__alcohol) + " grados de alcohol."

    @staticmethod
    def getClassInfo():
        return "Se han creado " + str(Beer.cont) + " Objetos."


drink = Drink("agua") 
beer = Beer("Heineken 0.0", "Heineken", 0.0, 10, 20)

print(drink.getDetail())
print(beer.getDetail())
print("Con ganancia: ", beer.getGain())
print(Beer.cont)
beer1 = Beer("Pale Ale", "Minerva", 5.0, 12, 23)
print(beer1.getDetail())
print("Con ganancia: ", beer1.getGain())
print(Beer.cont)
print(Beer.getClassInfo())