import json
import random
import csv
from datetime import datetime

salir = "no"
while salir == "no":
    print("=====================================Trivias=====================================\n\n                                    1. Comenzar\n                                    2. Top\n")
    def separador():
        print("---------------------------------------------------------------------------------")
    separador()
    opcion = input("")
    match opcion:
        case "1":
            separador()
            nombre_de_usuario = input("escribe tu nombre de usuario: ")
            respuesta_correcta = 0
            respuesta_incorrecta = 0
            for i in range(6):
                with open("Preguntas.json", "r") as archivo:
                    datos = json.load(archivo)
                pregunta_elegida = random.choice(datos)
                opciones = pregunta_elegida["opciones"]
                print("Pregunta:", pregunta_elegida["pregunta"])  # Acceso correcto por clave
                print("A",opciones["A"])
                print("B",opciones["B"])
                print("C",opciones["C"])
                print("D",opciones["D"])
                respuesta = input("Tu respuesta: ")
                if respuesta == pregunta_elegida["respuesta_correcta"]:
                    respuesta_correcta += 1
                else: 
                    respuesta_incorrecta += 1
                separador()
            hora_final = datetime.now().strftime("%m/%d/%Y %H:%M")
            puntos = respuesta_correcta * 20
            print("tus puntos son: ",puntos)
            print(f"Respondiste {respuesta_correcta} preguntas correctas")
            with open("InfoDePartida.csv", "a", newline="", encoding="utf-8") as archivo:
                escritor = csv.writer(archivo)
                if archivo.tell() == 0:
                    escritor.writerow(["nombre","Hora", "Correctas", "Incorrectas", "Puntos"])
                escritor.writerow([nombre_de_usuario,hora_final, respuesta_correcta, respuesta_incorrecta, puntos])
        case "2":
            with open("InfoDePartida.csv", "r") as tabla:
                contenido = csv.reader(tabla)
                for i in contenido:
                    print(i)
            separador()
    salir = input("quieres salir?\n")