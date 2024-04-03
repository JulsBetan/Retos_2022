# /*
#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */


def is_par(numer):
    return "es par" if numer % 2 == 0 else "es impar"

def is_fibonacci(number):
    if number < 3: 
        return "fibonacci"
    fib1 = 1
    fib2 = 1
    fibo = 0
    cont = 4
    while True:
        fibo = fib1 + fib2
        # print(f"Fibo {fibo} cont {cont} numero {number}")
        if number == fibo:
            return "fibonacci"
        if fibo > number:
            return "no es fibonacci"
        fib1 = fib2
        fib2 = fibo
        cont += 1

def is_prime(number):
    if number <2:
        return False
    for i in range (2, number):
        if number % i == 0:
            return False
    return True

def check_number(number):
    result = "es primo" if is_prime(number) else "no es primo"  
    return result


for num in range(101):
    print(f"El numero {num} {check_number(num)}, {is_fibonacci(num)} y {is_par(num)}")