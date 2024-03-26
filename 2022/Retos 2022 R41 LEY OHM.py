# 
#   Reto #41
#   LA LEY DE OHM
#   Fecha publicación enunciado: 10/10/22
#   Fecha publicación resolución: 17/10/22
#   Dificultad: FÁCIL
#  
#   Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
#   - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
#   - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
#  

def leyOhm (v:float, r:float, i:float):
    lista = [v, r, i]
    ceros = 0
    nceros = 0
    index = 0

    for x in range(3):
        if lista[x] == 0:
            ceros += 1
            index = x
        else:
            nceros += 1

    if ceros > 1 or nceros == 3:
        return "Invalid values"

    return "v="+str(round(i * r,2)) if lista[0] == 0 else ("r="+str(round(v / i,2)) if lista [1] == 0 else "i="+str(round(v / r,2)))

def ohm_law(v=None, r=None, i=None):
    if v is not None and r is not None and i is None:
        return f"i={v / r : .2f}"
    elif v is not None and i is not None and r is None:
        return f"r={v / i : .2f}"
    elif r is not None and i is not None and v is None:
        return f"v={r * i :.2f}"
    else: 
        return "Invalid values"

print("El resultado es", leyOhm(10,20.52323,0))
print("El resultado es", leyOhm(0,20.52323,10))

print("El resultado es", ohm_law(v=10,r=20.52323))
print("El resultado es", ohm_law(r=20.52323,i=10))