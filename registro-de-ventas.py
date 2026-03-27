import re
print("-----------------------------------------------------------")
print("tienda de frutas")
print("-----------------------------------------------------------")

user_name = input("bot: buenas ¿como te llamas? ")
print("bot: un gusto conocerte", user_name)

fresas = 6
peras = 20
manzanas = 27
banana = 14
sandia = 21
naranja = 18

print("-----------------------------------------------------------")
print("fresas = 6")
print("peras = 20")
print("manzanas = 27")
print("banana = 14")
print("sandia = 21")
print("naranja = 18")
print("-----------------------------------------------------------")


costo_de_pedido = 0

quiere_comprar = input("quieres comprar frutas? (si/no) ")

if quiere_comprar == "si":
    print(f"bot: Escribe lo que quieres pedir {user_name}")
    print("escribe por ejemplo (cantidad fruta) separado por coma")
    print("ejemplo: 5 manzanas, 2 fresas")

    pedido_de_usuario = input("")

    # Corregir formato: insertar espacio entre número y letra
    pedido_corregido = re.sub(r'(\d)([a-zA-Z])', r'\1 \2', pedido_de_usuario)

    # Dividir por comas y limpiar espacios extra
    pedido_lista = [item.strip() for item in pedido_corregido.split(",") if item.strip()]

    print("Tu pedido:", ", ".join(pedido_lista))

    for pedido in pedido_lista:
        cantidad, fruit = pedido.split(" ")
        cantidad = int(cantidad)

        print(f"pediste: {cantidad} {fruit}")

        if fruit in ["fresa", "fresas"]:
            costo_de_pedido += fresas * cantidad
        elif fruit in ["manzana", "manzanas"]:
            costo_de_pedido += manzanas * cantidad
        elif fruit in ["pera", "peras"]:
            costo_de_pedido += peras * cantidad
        elif fruit in ["banana", "bananas"]:
            costo_de_pedido += banana * cantidad
        elif fruit in ["sandia", "sandias"]:
            costo_de_pedido += sandia * cantidad
        elif fruit in ["naranja", "naranjas"]:
            costo_de_pedido += naranja * cantidad
        else:
            print("Fruta no disponible")

    es_miembro = input("bot :¿tienes membresia? (si/no) ")

    if es_miembro == "si":
        costo_total = costo_de_pedido * 0.90
    else:
        costo_total = costo_de_pedido

    descuento = costo_total - costo_de_pedido
    print(f"gracias por tu compra {user_name}")

    print("-----------------------------------------------------------")
    print(f"comprador: {user_name}")
    print(f"subtotal: {costo_de_pedido}")
    print(f"tiene membresia?: {es_miembro}")
    print(f"tu descuento es de: {descuento}")
    print(f"total a pagar: {costo_total}")

    print("-----------------------------------------------------------")

else:
    print("gracias por venir a la tienda")