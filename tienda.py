def mensaje_Inicio():# Mandar un mensaje de la tienda
    print(" -------------------------------------")
    print(" -      BIENVENIDOS A LA TIENDA      -")
    print(" -                 D E               -")
    print(" -              MASCOTAS             -")
    print(" -------------------------------------")

def saludo():# Pedir los datos del usuario
    nombre = input("Cual es tu nombre? ")
    apellido = input("Cual es tu apellido? ")
    print(f"Hola bienvenidos a la tienda de mascotas {nombre} {apellido}")

def mostrar_menu():# lgica del programa(inven, comp, salir)
    return int(input("Seleccionar la opcion que deseas hacer: \n1. Conocer cuantos animales tiene la tienda\n2. Comprar un animal\n3. Salir\n"))

def mostrar_inventario():# Mostrar el inventario
    print(f"Los animales que tenemos son: \n 🐶 {num_perros} perros \n 🐱 {num_gatos} gatos \n 🐦 {num_pajaros} pajaros \n")
    print(f"En total son {str(num_perros + num_gatos + num_pajaros)}")


#Variables de animales 
num_perros  = 10
num_gatos   = 8
num_pajaros = 25

mensaje_Inicio()
saludo()

def comprar_animal():
    num_perros  = 10
    num_gatos   = 8
    num_pajaros = 25

    compra = int(input("Que animal deseas comprar:\n1. perro 🐶\n2. gato 🐱 \n3. pajaro 🐦 \n"))
    if compra == 1:
        print("Haz comprado un perro 🐶")
        num_perros = num_perros - 1
        print(f"Los animales que tenemos son: \n 🐶 {num_perros} perros \n 🐱 {num_gatos} gatos \n 🐦 {num_pajaros} pajaros \nEn total son {str(num_perros + num_gatos + num_pajaros)}")
    elif compra == 2:
        print("Haz comprado un gato 🐱")
        num_gatos = num_gatos - 1
        print(f"Los animales que tenemos son: \n 🐶 {num_perros} perros \n 🐱 {num_gatos} gatos \n 🐦 {num_pajaros} pajaros \nEn total son {str(num_perros + num_gatos + num_pajaros)}")
    elif compra == 3:
        print("Haz comprado un gato  🐦" )
        num_pajaros = num_pajaros - 1
        print(f"Los animales que tenemos son: \n 🐶 {num_perros} perros \n 🐱 {num_gatos} gatos \n 🐦 {num_pajaros} pajaros \nEn total son {str(num_perros + num_gatos + num_pajaros)}")
    else:
        print("opcion invalida")

while True:
#Crear la logica del programa 
    opcion = mostrar_menu()

    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        comprar_animal()
    elif opcion == 3:
        break