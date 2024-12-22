print("Hola")

i = 0

#Ciclo es una iteracion o bucle 
while i < 10:

    if i < 5:
        print(f"El numero {i} es menor a 5")
    else:
        print(f"El numero {i} es mayor o igual que 5")
    
    #Permite que el ciclo termine
    i += 1

print("Termino la iteracion")


#Iteracion a travez de rango o lista 
for x in "Gerardo":
    print(x)

for y in range(5):
    print(y)

# ciclo infinito para un menu
while True:
    print("Escribe la opcion deseada: \n1. Saludar\n2. Salir")
    
    respuesta = int(input("Que respuesta es: "))

    if respuesta == 1:
        print("Saludos terricola")
    elif respuesta == 2:
        break # salir de la iteracion 
