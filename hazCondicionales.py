"""
Crea un programa que imprima un mensaje solicitando al usuario un número entre el 1 y el 100:

a) Si el número es menor a 1, debe imprimir un mensaje “Favor de ingresar un número mayor a 0”.
b) Si el número es mayor a 100, debe imprimir un mensaje “Favor de ingresar un número menor o igual a 100”.
c) Si el número sí es entre 1 y 100, debe imprimir un mensaje “¡Muy bien! El <número> es una gran opción.
"""

numero = int(input("Ingresa un numero (1/100): "))

if numero <= 1:
    print("Favor de ingresar un numero mayor a 0")
elif numero >= 100:
    print("Favor de ingresar un numero menor o igual a 100 ")
else:
    print(f"!Muy bien! el {numero} es gran opcion")