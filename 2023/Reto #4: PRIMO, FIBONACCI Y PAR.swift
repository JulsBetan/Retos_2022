/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

 func is_par(number: Int) -> String {
    return number % 2 == 0  ? "es par" : "es impar"
 }

func is_fibonacci(number: Int)  -> String {
    if number < 3 {  
        return "fibonacci"
    }    
    var fib1 = 1
    var fib2 = 1
    var fibo = 0
    var cont = 4
    while true {
        fibo = fib1 + fib2
        // print(f"Fibo {fibo} cont {cont} numero {number}")
        if number == fibo {
            return "fibonacci"
        }
        if fibo > number{
            return "no es fibonacci"
        }
        fib1 = fib2
        fib2 = fibo
        cont += 1
    }
}

func is_prime(number: Int) -> Bool{
    if number < 2 {
        return false
    }
    for i in  (2...number){
        if number % i == 0{
            return false
        }
    }
    return true
}

func check_number(number: Int) -> String {
    let result = is_prime(number: number) ? "es primo" : "no es primo"  
    return result
}

for num in (0...100) {
    print("El numero \(num) \(check_number(number: num)), \(is_fibonacci(number: num)) y \(is_par(number: num))")
}