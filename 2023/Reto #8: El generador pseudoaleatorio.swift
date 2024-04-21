/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

import Foundation

var contador = 0

func randomNumber() {
    while true {
        contador += 1
        if contador >= 101 {
            contador = 1
        }
        if stopEvent.wait(timeout: .now()) == .success {
            break
        }
    }
}

let stopEvent = DispatchSemaphore(value: 0)

func main() {
    let counterThread = Thread {
        randomNumber()
    }
    counterThread.start()

    print("Presiona cualquier tecla para detener el contador...")
    _ = readLine()

    // Detiene el contador al salir de la función
    print("Contador detenido.")
    stopEvent.signal()

    // Espera a que el hilo del contador termine
    counterThread.cancel()

    // Imprime el valor final del contador
    print("Valor final del contador: \(contador)")
}

main()


