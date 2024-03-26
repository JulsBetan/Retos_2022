""" /*
 * Reto #20
 * PARANDO EL TIEMPO
 * Fecha publicación enunciado: 16/05/22
 * Fecha publicación resolución: 23/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución 
 * del programa principal. Se podría ejecutar varias veces al mismo tiempo.
 */ """

import asyncio

async def sum(num1, num2, secs):
    print("Waiting {} seconds...".format(secs))
    await asyncio.sleep(secs)
    return num1 + num2

result = asyncio.run(sum(10, 5, 5))

print("La suma asincrona es:", result)

#Usando Task #Da error de no running event loop

""" task = asyncio.create_task(sum(20, 50, 3))

asyncio.wait(task)

result = task.result()

print("La suma asincrona es:", result) """