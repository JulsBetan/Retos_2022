# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */

import requests
import rumps

class AwesomeStatusBarApp (rumps.App) :
    def __init__(self):
        super (AwesomeStatusBarApp, self).__init__("BettaTech" )
        self.menu = ["Querying API..."]

    @rumps.timer (1)
    def sayhi(self, _) :
        headers = {
            'Content-Type': 'application/json',
        }
        r = requests.get ("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
        print(r.json() ['data'] ['rates']['MXN'])
        self.title = r.json()['data']['rates']['MXN']

if __name__ == "__main__":
    AwesomeStatusBarApp().run()