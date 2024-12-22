# Creacion de una lista modificable
nombres = ["Gerardo", "Juan", "Pedro", "Santiago", "Jorge"]

print(nombres)
print(type(nombres))

# imprimir por el indice
print(nombres[0])

# modificar un elemento 
nombres[0] = "Jose"
print(nombres)

#obtener la longitd
print(len(nombres))

#agregar un elemento a la lista
nombres.append("Gerardo")
print(nombres)

# eliminar un nombre
nombres.remove("Juan")
print(nombres)

# eliminar con indice }
del nombres[1]
print(nombres)

# saber si un dato esta en lista
print("Gerardo" in nombres)

#obtener secciones de lista
print(nombres)
print(nombres[0:2])
print(nombres[2:])


#Recorrer la lista 
for nombre in nombres:
    print(nombre)

# impresiones de los indices 
for i, nombre in enumerate(nombres):
    print(i, nombre)