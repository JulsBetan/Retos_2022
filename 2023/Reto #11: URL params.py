# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */

def get_urlParams(url):
    params = [x.split("=")[1] for x in url.split("?")[1].split("&")]
    return params

def get_URLParams(url):
    params = []
    param  = ""
    ban = 0
    ban2 = 0

    for x in url:
        if ban == 1:
            if x != '&' and ban2:
                param += x
            elif x == '&':
                params.append(param)
                param = ""
                ban2 = 0
            if x == '=':
                ban2 = 1    

        if x == '?':
            ban = 1

    if param:
        params.append(param)

    return params


url = "https://retosdeprogramacion.com?year=2023&challenge=0"

print(f"Los parametros de la URL {url} son: {get_urlParams(url)}")

print(f"Los parametros de la URL {url} son: {get_URLParams(url)}")