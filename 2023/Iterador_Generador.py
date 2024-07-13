# Ejercicio 1: Suma de Números Pares con Iterador

# Escribe un iterador que genere los primeros N números pares y luego calcule la suma de estos números.
# Explicación:

# 	•	IteradorNumerosPares es una clase iteradora que genera los primeros N números pares.
# 	•	En cada iteración, calcula el siguiente número par multiplicando el contador por 2 y acumula la suma de estos números.
# 	•	Al final, se imprime cada número par generado y la suma total de los números pares.

class IteradorNumerosPares:
    def __init__(self, n):
        self.n = n
        self.contador = 0
        self.suma = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.n:
            numero_par = self.contador * 2
            self.suma += numero_par
            self.contador += 1
            return numero_par
        else:
            raise StopIteration

iterador_pares = IteradorNumerosPares(5)
print(type(iterador_pares))

for numero in iterador_pares:
    print(numero)
    
print(f"Suma de los primeros 5 números pares: {iterador_pares.suma}")

# Ejercicio 2: Generador de Secuencia Fibonacci

# Crea un generador que devuelva los primeros N números de la secuencia Fibonacci.
# Explicación:

# 	•	generar_fibonacci() es una función generadora que produce los primeros N números de la secuencia Fibonacci.
# 	•	En cada iteración del bucle for, se genera el siguiente número de la secuencia Fibonacci utilizando la técnica de desempaquetado de tuplas (a, b = b, a + b).
# 	•	Se imprimen los primeros 10 números de la secuencia Fibonacci.

def generar_fibonacci(n):
    a, b = 0, 1
    contador = 0
    while contador < n:
        yield a
        a, b = b, a +  b
        contador += 1

mi_generador_fibonacci = generar_fibonacci(10)
for numero in mi_generador_fibonacci:
    print(numero)

# Ejercicio 3: Iterador de Números Impares

# Crea una clase iteradora que genere los primeros N números impares.
# Explicación:

# 	1.	IteradorNumerosImpares es una clase que implementa los métodos __iter__ y __next__.
# 	2.	__init__ inicializa el iterador con n (el número de elementos a generar), contador para llevar la cuenta de los elementos generados y numero para almacenar el último número impar generado.
# 	3.	__iter__ devuelve self para que el objeto sea un iterador.
# 	4.	__next__ genera el siguiente número impar incrementando numero en 2 y actualizando contador. Si se han generado n elementos, lanza StopIteration.

class IteradorNumerosImpares:
    def __init__(self, n):
        self.n = n
        self.contador = 0
        self.numero = -1
 
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.contador < self.n:
            self.numero += 2
            self.contador += 1
            return self.numero
        else:
            raise StopIteration
        
iterador_impares = IteradorNumerosImpares(5)
for numero in iterador_impares:
    print(f"Impares {numero}")


# Ejercicio 2: Generador de Números Cuadrados

# # Crea una función generadora que devuelva los cuadrados de los primeros N números naturales (0, 1, 2, …, N-1).
# Explicación:

# 	1.	generar_cuadrados es una función generadora que utiliza un bucle for para iterar desde 0 hasta n-1.
# 	2.	En cada iteración, yield devuelve el cuadrado del número i y pausa la ejecución de la función.
# 	3.	El bucle for en el uso del generador itera sobre los valores producidos por el generador, imprimiendo cada uno de los cuadrados.

def generar_cuadrados(n):
    for i in range(n):
        yield i * i

mi_generador_cuadrador = generar_cuadrados(5)

for numero in mi_generador_cuadrador:
    print(f"Cuadrado {numero}")

for numero in mi_generador_cuadrador:
    print(f"Cuadrado {numero}")