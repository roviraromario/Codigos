
partidos_de_ligas = int(input("escribe la cantidad de partidos de liga:\n"))
while partidos_de_ligas < 0:
    print("cantidad invalida\n")
    partidos_de_ligas = int(input("Escribe los pardidos de la liga:\n"))
partidos_jugados = int(input("Escribe los pardidos que ha jugado el juju:\n"))

while partidos_jugados > partidos_de_ligas:
        print("no puedes jugar mas partidos de los que tiene la liga")
        partidos_jugados = int(input("Escribe los pardidos que ha jugado el juju:\n"))

partidos_ganados = 0
partidos_perdidos = 0
partidos_empatados = 0
goles_contra = 0
goles_favor = 0

for partidos in range(1, partidos_jugados + 1, 1):
    print("partido numero: ",partidos)
    marcador_favor = int(input(f"escibe goles metio el juju en el partido numero {partidos}: "))
    marcador_contra = int(input(f"escibe goles cuantos goles le metieron a el juju en el partido numero {partidos}: "))

    if marcador_favor > marcador_contra:
        partidos_ganados += 1
        goles_contra = goles_contra + marcador_contra
        goles_favor = goles_favor + marcador_favor
    elif marcador_favor < marcador_contra:
        partidos_perdidos += 1
        goles_contra = goles_contra + marcador_contra
        goles_favor = goles_favor + marcador_favor
    else:
        partidos_empatados += 1
        goles_contra = goles_contra + marcador_contra
        goles_favor = goles_favor + marcador_favor

print("-------------------------------------------------------------------")
print("partidos ganados = ", partidos_ganados)
print("partidos perdidos = ",partidos_perdidos)
print("partidos empatados = ", partidos_empatados)

puntos = (partidos_ganados * 3) + partidos_empatados

print("puntos = ", puntos)
print("goles a favor = ", goles_favor)
print("goles en contra = ", goles_contra)

diferencia_de_goles = goles_favor - goles_contra

print("diferencia de goles es = ", diferencia_de_goles)

print("-------------------------------------------------------------------")