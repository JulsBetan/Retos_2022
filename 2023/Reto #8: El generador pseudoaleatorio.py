# /*
#  * Crea un generador de números pseudoaleatorios entre 0 y 100.
#  * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
#  *
#  * Es más complicado de lo que parece...
#  */

import threading

def random_number():
    global contador
    contador = 1

    while not stop_event.is_set():
        contador += 1
        # print(contador)
        if contador >= 101:
            contador = 1
    

def main():
    global stop_event
    stop_event = threading.Event()
    counter_thread = threading.Thread(target=random_number)
    counter_thread.start()

    print("Presiona cualquier tecla para detener el contador...")
    input()

    # Detiene el contador al salir de la función
    print("Contador detenido.")
    stop_event.set()
    counter_thread.join()  # Espera a que el hilo del contador termine
    # Imprime el valor final del contador
    print(f"Valor final del contador: {contador}")

if __name__ == "__main__":
    main()