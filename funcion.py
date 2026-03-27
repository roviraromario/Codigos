def saludar (a, b):
    c = ((a**2) + (b**2))**(1/2)
    return c + 5

print ("pa ve 2 ", saludar(3,4))


def pinguino (a: int, b: str):
# a guarda edad
# b tipo de sangre 
    if a <= 18 and a <= 28:
        if b == "A":
            return True
    return False


for i in range(4):
        print(f"La persona nº{i+1}: ", pinguino(18,"A"))