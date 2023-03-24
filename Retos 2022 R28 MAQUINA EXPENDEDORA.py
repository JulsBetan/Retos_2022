# /*
#  * Reto #28
#  * MÁQUINA EXPENDEDORA
#  * Fecha publicación enunciado: 11/07/22
#  * Fecha publicación resolución: 18/07/22
#  * Dificultad: MEDIA
#  *
#  * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
#  * que reciba dinero (array de monedas) y un número que indique la selección del producto.
#  * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
#  * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
#  * - Si no hay dinero de vuelta, el array se retornará vacío.
#  * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
#  * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
#  */

from enum import Enum

class Money(Enum):
    five = 5
    ten = 10
    fifty = 50
    oneHundred = 100
    twoHundred = 200

prices = {"mouse":50, "keyboard":250, "SSD":350, "airpods":450, "ipad":550}

products = {1:"mouse", 2: "keyboard", 3: "SSD", 4: "airpods", 5: "ipad"}

products = {1:["mouse",50], 2: ["keyboard",250], 3: ["SSD",350], 4: ["airpods",450], 5: ["ipad",550]}

products = {1:{"name":"mouse","money":50}, 
            2: {"name":"keyboard","money":250}, 
            3: {"name":"SSD","money":350}, 
            4: {"name":"airpods","money":450}, 
            5: {"name":"ipad","money":550}}


for x in products:
    print(x, products[x]["name"])

def your_change(change):
    money = [200, 100, 50, 10, 5]
    money_array = []

    remaining = change 

    for x in money:
        times = remaining // x
        for y in range(times):
            money_array.append(x)
        remaining = remaining % x
    
    return money_array

# def buy_products(money, product):
#     if product in products:
#         print (products[product][1])
#         if products[product][1] > sum(money):
#             return "es mas caro", money
#         else:
#             change = sum(money) - products[product][1]
#             return products[product][0] , your_change(change)
#     else:
#         return "no existe", money 
    
def buy_products(money, product):
    if product in products:
        print (products[product]["money"])
        if products[product]["money"] > sum(money):
            return "es mas caro", money
        else:
            change = sum(money) - products[product]["money"]
            return products[product]["name"] , your_change(change)
    else:
        return "no existe", money 

product, change = buy_products([Money.five.value, Money.ten.value,Money.oneHundred.value], 1)
print (f"Tu producto: {product}, tu cambio {change}")

product, change = buy_products([Money.oneHundred.value, Money.five.value, Money.ten.value,Money.oneHundred.value, Money.twoHundred.value, Money.twoHundred.value,Money.oneHundred.value], 5)
print (f"Tu producto: {product}, tu cambio {change}")

#115 -50 = 65

#5+10+100+200+200+100

