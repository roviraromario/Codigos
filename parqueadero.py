
numero = 0
n = 0
datos.open("datos.txt", "r")
for i in datos:
    if "vacio" in i:
        numero +=1
print(numero)

quiere_parquear = "si"
while quiere_parquear == "si":
    quiere_parquear = input("quieres parquearte?")
    if quiere_parquear == "si":
        nombre = input("escribe tu nombre")
        if numero > 0:
            datos.open("datos.txt", "w")
            for i in datos:
                if "vacio" in i:
                        
                    print("lel")
