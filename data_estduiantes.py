salir = "no"
notas_materias = {}
inicio_sesion = "no"
materias = ["matematicas", "lenguaje", "sociales", "biologia", "ingles"]

mejor_promedio = 0

def contrañea_valida(contraseña):
    if len(contraseña) < 8:
        return False
    if not any(char.isupper() for char in contraseña):
        return False
    if not any(char.islower() for char in contraseña):
        return False
    if not any(char.isdigit() for char in contraseña):
        return False
    return True

def separador():
    print("-----------------------------------------")

def separador2():
    print("-------------------/////-----------------")

while salir == "no": 
    opcion = input("- escribe \n1 para crear nueva cuenta \n2 para iniciar sesion\n3 salir\n  respuesta:")
    if opcion == "1":
        separador()
        tipo_usuario = input(" escribe \n1 si eres estudiante \n2 si eres profesor\n  respuesta:")
        if tipo_usuario == "1":
            separador()
            nombre_usuario = input("escribe tu nombre de usuario: ")
            contraseña = input("escribe tu contraseña: ")

            if not contrañea_valida(contraseña):
                separador2()
                print("contraseña invalida, debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                continue

            with open("datos.txt","a") as datos:
                datos.write("estudiante|"+ nombre_usuario+"|"+ contraseña+"|"+"\n")

            separador()
        elif tipo_usuario == "2":
            separador()
            nombre_usuario = input("escribe tu nombre de usuario: ")
            contraseña = input("escribe tu contraseña: ")

            if not contrañea_valida(contraseña):
                separador2()
                print("contraseña invalida, debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula y un número.")
                continue
                
            with open("datos.txt","a") as datos:
                datos.write("profesor|"+ nombre_usuario +"|"+ contraseña+"|"+"\n")
        else: 
            separador()
            print("usuario invalido")
            
    elif opcion == "2":
        separador()
        opcion_inicio_sesion = input("1 si eres estudiante \n2 si eres profesor \n  respuesta:")
        if opcion_inicio_sesion == "1":
                nombre_inicio = input("escribe tu nombre de  usuario: ")
                contraseña_inicio = input("escribe tu contraseña: ")

                with open("datos.txt","r") as datos:
                    contenido = datos.readlines()
                    for i in contenido:
                            if "estudiante" and nombre_inicio and contraseña_inicio in i:
                                inicio_sesion = "si"
                                usuario_iniciado = i
                                valores = i.split("|")
                                print("-------------sesion iniciada--------------")

                while inicio_sesion == "si":
                    estudiante_=input("escribe: \n1 para ver notas \n2 para ver promedio \n3 para cerrar sesion\n  respuesta: ")
                    cuenta = valores
                    num = 0
                    for e in valores:
                        num += 1
                    if num > 3:
                        notas = cuenta[4]
                    else:
                        notas = "no tienes notas"
                    match estudiante_:
                        case "1":
                            print("-----ver notas----")
                            print(f"notas: {notas}\n \n")
                        case "2":
                            print("-----ver promedio----")
                            if notas != "no tienes notas":
                                promedio = sum(notas.values()) / len(notas)
                                cuenta.append([promedio])
                                print(f"promedio: {promedio}\n \n")
                            else:
                                print(notas)
                        case "3":
                            print("-----sesion cerrada----\n")
                            inicio_sesion = "no"
                        case _:
                            print("-----respuesta invalida----")

        elif opcion_inicio_sesion == "2":
                nombre_inicio = input("escribe tu nombre de  usuario: ")
                contraseña_inicio = input("escribe tu contraseña: ")

                with open("datos.txt","r") as datos:
                    contenido = datos.readlines()
                    for i in contenido:
                            if "profesor" and nombre_inicio and contraseña_inicio in i:
                                inicio_sesion = "si"
                                usuario_iniciado = i
                                valores = i.split("|")
                                print("-------------sesion iniciada--------------")
                
                while inicio_sesion == "si":
                    profesor_= input("escribe:\n1 agregar notas a estudiante \n2 ver estudiante con mejor promedio \n3 notas del grupo\n4 cerrar sesion\n  respuesta: ")
                    match profesor_:
                        case "1":
                            print("-----agregar notas----")
                            with open("datos.txt","r") as datos:
                                contenido = datos.readlines()
                                numero = 1
                                for i in contenido:
                                    valores = i.split("|")
                                    valores.remove('\n')
                                    print(valores)
                                    usuario = valores[1]
                                    numero += 1
                                    if "estudiante" in i:
                                        print(usuario)
                            estudiante_poner_nota = input("escribe el nombre del estudiante que quieres ponerle nota: ")
                            with open("datos.txt","r") as datos:
                                contenido = datos.readlines()
                                numero_con_nombre = 0
                                for i in contenido:
                                    if estudiante_poner_nota in i:
                                        numero_con_nombre += 1
                                        print(i)
                                        estudiante = i


                                        print(estudiante)
                                        materia= input("escribe el nombre de la materia: ")
                                        if materia not in materias:
                                            separador()
                                            print("materia invalida")
                                            continue
                                        nota = float(input("escribe la nota del estudiante: "))
                                        nota = str(nota)
                            with open("datos.txt","a") as datos:

                                datos.write(estudiante+"|"+materia+"_"+nota+"|"+"\n")

                            if numero_con_nombre == 0:
                                print("---------------  Error  ------------------")
                                print("no existe ningun estudiante con ese nombre")
                                print("------------------------------------------")
                        case "2":
                            """for estudiante_promedio in usuarios:
                                cuenta = estudiante_promedio
                                notas = cuenta[2]
                                if notas == None:
                                    print("nadie tiene notas")
                                promedio = sum(notas.values()) / len(notas)
                                if mejor_promedio < promedio:
                                    mejor_promedio = promedio
                                    mejor_cuenta = cuenta[0]

                            print(mejor_cuenta)
                            print(mejor_promedio)"""
                        case "3":
                            """estudiantes = usuarios
                            for estudiante in estudiantes:
                                if estudiante[0] and estudiante [2] != None:
                                    nombre = estudiante[0]
                                    nota = estudiante[2]
                                    print(nombre, nota)

                                print()"""

                        case "4":
                            print("-----cerrar sesion----\n")
                            inicio_sesion = "no"
                        case _:
                            print("-----respuesta invalida----")
                    
    elif opcion == "3":
        salir = "si"
    else:
        separador()
        print("opcion invalida")
    
