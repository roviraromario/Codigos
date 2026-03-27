logearse = "si"
tiene_arroba = 0
tiene_punto = 0
while logearse == "si":
    nombre_de_usuario = input("Escibre tu nombre de usuario: ")

    correo = input("Escibre tu correo: ")

    if len(correo) >= 4:
        for caracteres in correo:
            if correo.startswith("@"):
                print("no puede comenzar con arroba")
            if correo.startswith("."):
                print("no puede comenzar con punto")
            if "@"  in caracteres:
                tiene_arroba += 1
            if "."  in caracteres:
                tiene_punto += 1

        if tiene_arroba > 1 or tiene_punto > 1:
                print("no puede haber mas de un @ o .")
        if "@." in correo:
                print("no puede haber @. juntos")

    else:
        print("tiene que tener minimo 4 carracteres")

    contraseña_de_usuario = input(f"Escribe tu contraseña {nombre_de_usuario}: ")

    con_caracter_especial = 0
    con_numero =0
    con_mayuscula = 0

    
    if len(contraseña_de_usuario) >= 8:
        print("tiene 8 caracteres")
        for contraseña in contraseña_de_usuario:    
            if contraseña.isdigit():
                con_numero += 1
            if contraseña.isupper():
                con_mayuscula += 1
            if contraseña.isalnum():
                con_caracter_especial += 1
        if con_numero == 0:
            print("no tienes numeros en tu contraseña")
        elif con_mayuscula == 0:
            print("no tienes mayusculas en tu contraseña")
        elif con_caracter_especial == 0:
            print("no tienes caracteres especiales en tu contraseña")
        else:
            print("entra")
        logearse = "no"
    else:
        print("tu contraseña no tiene 8 caracteres")
        logearse = input("quieres volver a logearte: ")
