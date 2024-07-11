import string

def generar_palindromo(n, k):
    if k > 26:
        raise ValueError("El número de letras diferentes no puede ser mayor que 26.")
    if n < 1:
        raise ValueError("La longitud del palíndromo debe ser al menos 1.")
    if k > n:    
        raise ValueError("El número de letras diferentes no puede ser mayor que la longitud del palíndromo.")
    
    letras = list(string.ascii_lowercase[:k])
    mitad = []
    
    print(letras)
    print ((n+1) // 2)
    # Crear la mitad del palíndromo
    for i in range((n + 1) // 2):
        print (f'i%k {i%k}')
        mitad.append(letras[i % k])
        print(i % k)
        print(letras[i % k])
    
    # Si n es impar, no duplicar el elemento central
    if n % 2 == 0:
        palindromo = mitad + mitad[::-1]
    else:
        palindromo = mitad + mitad[-2::-1]
    
    return ''.join(palindromo[:n])  # Asegurar que el palíndromo tenga longitud n

# Ejemplo de uso:
n = 10
k = 3
print(generar_palindromo(n, k))

