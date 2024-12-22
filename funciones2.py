
import random

# La longitud del nonbre 
nombre = "Gerardo"
print("La longitud del nombre es:" , len(nombre))

#Funciones matematicas
print(abs(-10)) # absoluto

#numero aleatorio aleatorio
resultado = random.randint(1,100)
print(resultado)

def saludar_y_sumar(nombre, num1, num2):
    print("Saludos", nombre)
    print("El resultado de la suma es:", num1 + num2)

saludar_y_sumar("gerardo", 15, 12)

# valores opcionales 

def saludar_y_sumar(nombre, num1, num2 = 4):
    print("Saludos", nombre)
    print("El resultado de la suma es:", num1 + num2)

saludar_y_sumar("gerardo", 15)