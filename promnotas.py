
num_estudiantes = int(input("escribe el numero de estudiantes que vas a registrar: \n"))
son_validos = "no"
estudiantes_aprobados = 0
estudiantes_desaprobados = 0
print("----------------------------------------------------------------------")

while num_estudiantes > 0:
    son_validos = "no"
    while son_validos == "no":
        nombre = input("escribe el nombre del estudiante: \n")
        nota_mat = float(input("escribe tu nota en matematicas: \n"))
        nota_bio = float(input("escribe tu nota en biologia: \n"))
        nota_soc = float(input("escribe tu nota en sociales: \n"))
        nota_ing = float(input("escribe tu nota en ingles: \n"))
        nota_len = float(input("escribe tu nota en lenguaje: \n"))

        if nota_bio <= 5 and nota_bio > 0 and nota_ing <= 5 and nota_ing > 0 and nota_len <= 5 and nota_len > 0 and nota_soc <= 5 and nota_soc > 0  and nota_mat <= 5 and nota_mat > 0 :
            son_validos = "si"
        else:
            print("escribe notas validas")
            son_validos = "no"

        notas = [nota_ing,nota_bio,nota_len,nota_mat,nota_soc]
                  
    prom_estudiante = sum(notas) / len(notas)
    print(prom_estudiante) 
    
    if prom_estudiante >= 3:
        estudiantes_aprobados += 1
        num_estudiantes = num_estudiantes - 1     
    elif prom_estudiante < 3:
        estudiantes_desaprobados += 1
        num_estudiantes = num_estudiantes - 1
    else:
        print("tu promedio no es valido")
    print("----------------------------------------------------------------------")

print("el numero de estudiantes aprobados son:",estudiantes_aprobados)
print("el numero de estudiantes desaprobados son:",estudiantes_desaprobados)

print("----------------------------------------------------------------------")









