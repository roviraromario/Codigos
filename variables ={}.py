caracteristicas_de_usuario = {}

def guardar_caracteristica(caracteristicas_de_usuario,clave,valor):
    caracteristicas_de_usuario[clave] = valor
    return caracteristicas_de_usuario

clave = "nombre"
valor = input("tu nombre es: ")
guardar_caracteristica(caracteristicas_de_usuario, clave, valor)
clave = "edad"
valor = input("tu edad es:")
guardar_caracteristica(caracteristicas_de_usuario, clave, valor)
print(caracteristicas_de_usuario)

print(caracteristicas_de_usuario.get("edad"))
print(caracteristicas_de_usuario.get("nombre"))