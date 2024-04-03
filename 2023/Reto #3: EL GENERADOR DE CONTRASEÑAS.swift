/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */



 func gen_password(args: [Int]) -> String{
    var characters = Array("abcdefghijklmnopqrstuvwxyz")

    if args[1] == 1 {
        characters += Array("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    }
    if args[2] == 1 {
        characters += Array("0123456789")
    }
    if args[3] == 1 {
        characters += Array("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    }
    print(characters)

    let lenght = args[0] == 0 ? 8 : 16
    var password = ""

    for _ in 0..<lenght {
        password.append(characters.randomElement()!)
    }

    return password

 } 

 print ("La contraseña generada es: \(gen_password(args: [1, 0, 1, 1]))")