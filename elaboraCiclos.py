"""
Ahora, crea un programa que:

1. Solicite al usuario que ingrese un texto (cualquiera).
2. Solicite después al usuario ingresar cuántas veces desea imprimirlo (e.g. 10).

Recuerda que el programa debe imprimir el texto ingresado el número de veces solicitado, y terminar.

"""

texto = input("Ingresa una frase: ")
valor = 0
contador = int(input("Cuantas veces se va a repetir "))

while contador != valor:
    print(texto)
    valor += 1