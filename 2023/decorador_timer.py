import time
import functools

# Definimos el decorador
def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Tiempo de inicio
        print(f"Start Time: {start_time:.4f}")
        result = func(*args, **kwargs)  # Llamamos a la función decorada
        end_time = time.time()  # Tiempo de fin
        duration = end_time - start_time  # Duración de la ejecución
        print(f"End Time: {end_time:.4f}")
        print(f"Duration: {duration:.4f} seconds")
        return result
    return wrapper

# Una función que simula un retraso
@timing_decorator
def delayed_function():
    print("Function is starting...")
    time.sleep(2)  # Retraso de 2 segundos
    print("Function is ending...")

# Llamamos a la función decorada
delayed_function()