    /*
    * Escribe un programa que muestre por consola (con un print) los
    * números de 1 a 100 (ambos incluidos y con un salto de línea entre
    * cada impresión), sustituyendo los siguientes:
    * - Múltiplos de 3 por la palabra "fizz".
    * - Múltiplos de 5 por la palabra "buzz".
    * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
    */

    func fizzbuzz()->Void{

        for i in 1...100{
            let mult3: Bool = i % 3 == 0 ? true : false
            let mult5: Bool = i % 5 == 0 ? true : false    
            let resultado: String = (mult3 && mult5) ? "FizzBuzz": (mult3 ? "Fizz" : (mult5 ? "Buzz" : "NA"))

            print("Resultado \(i) \(resultado)")
        }
        
    }

    fizzbuzz()