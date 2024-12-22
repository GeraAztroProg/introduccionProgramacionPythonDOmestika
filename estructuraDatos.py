"""
Crea un programa que servirá como lista para el supermercado.

Este programa debe solicitar al usuario ingresar qué quiere agregar a su lista. Debe contener también una opción para imprimir la lista (imprimiendo primero algún encabezado por ejemplo *** TU LISTA ***).

Al final debe tener una opción para salir del programa. Muestra tus avances en el foro.
"""

lista_supermercado = []

def menu():
    return int(input(f"Que deseas hacer \n1.- Agregar un producto \n2.- mostrar lista\n3.- Salir\n"))

while True:
    
    opcion = menu()
    
    if opcion == 1:
        producto = input("Que producto haz comprado")
        lista_supermercado.append(producto)
    elif opcion == 2:
        for lista in lista_supermercado:
            print(lista)
    else:
        break