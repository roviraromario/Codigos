
lista = [1,4,5,8,9,16,22]

pi = 0
pd = len(lista) - 1
numero = 8
find = False

if numero == lista[pi]:
    print(f"Nùmero encontrado en la posiciòn {pi} -> {lista[pi]}")
    find = True
if numero == lista[pd]:
    print(f"Nùmero encontrado en la posiciòn {pd} -> {lista[pd]}")
    find = True

while pi <= pd and not find:
    pc = (pi + pd)//2
    
    if numero == lista[pc]:
        print(f"Nùmero encontrado en la posiciòn {pc} -> {lista[pc]}")
        find = True
    elif numero > lista[pc]:
        pi = pc + 1
    else:
        pd = pc - 1

if not find:
    print("Nùmero no encontrado")