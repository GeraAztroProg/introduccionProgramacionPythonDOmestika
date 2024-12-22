import random

def tirarDados():
    return random.randint(2,12)

def pedir_respuesta():
    print("Ingresa tu prediccion: \n1. Par\n2. Impar\n3. Salir del juego")

    return int(input())

def imprimir_respuesta(valor, prediccion):
    es_par = (valor % 2 == 0)
    if es_par and prediccion == 1:
        print("GANASTE, numero de los dados", valor)
    elif  not es_par and prediccion == 2:
        print("GANASTE, numero de los dados", valor)
    else:
        print("PERDISTE, numero de los dados", valor)

while True:
    valor = tirarDados()

    prediccion = pedir_respuesta()

    if prediccion == 3:
        break

    imprimir_respuesta(valor, prediccion)

print("Gracias por jugar")