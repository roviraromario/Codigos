filas = 8
columnas = 10
sala = [["_" for _ in range(columnas)]for _ in range(filas)]
pedir_silla = "si"
def separador():
        print("____________________________________________________________")

def imprime():
    print("  1234567890")
    for numero, fila in enumerate(sala):
        print(f"{numero+1} {"".join (fila)}")

print("bienvenido a cinelel\n")
while pedir_silla == "si":
    pedir_silla = input("Quieres reservar una nueva silla: ")
    if pedir_silla == "si":
        imprime()
        separador()
        posicion_y = int(input("escribe tu fila: ")) - 1
        possicion_x = int(input("escribe tu columna: ")) - 1
        posicion = sala[posicion_y][possicion_x]
        separador()
        if posicion == "_":
            sala[posicion_y][possicion_x] = "X"
            print("---------------------reservacion valida---------------------") 
            
            print(f"tu puesto ahora es: \nfila:{posicion_y + 1} \ncolumna:{possicion_x + 1}")
            separador()
        else:
            print("- esta silla ya esta reservada\n")
        quiere_ver = input("escribe si quieres verlo graficamente: ")
        if quiere_ver == "si":imprime()
else:
    print("gracias por venir")
