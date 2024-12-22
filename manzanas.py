manzanas = 20
precio = 5

print(" -------------------------------------")
print(" - 🍎 🍎 LA TIENDA MANZANA  🍎 🍎    -")
print(" -------------------------------------")

nombre = input("Cual es tu nombre? ")

print(f"Bienvenido {nombre} actualmente cuento con {manzanas} manzanas disponibles, cada una por un precio de {precio} pesos")

compra = int(input("Cuantas manzanas deseas comprar? "))

if compra >= 20:
    print(f"Lo siento no puedo vender mas de {manzanas} manzanas")
else:
    pagar = compra * precio
    print(f"Tu has comprado {compra} manzanas y debes pagar {pagar} pesos")

print(f"Aun tengo {manzanas - compra} manzanas disponibles")