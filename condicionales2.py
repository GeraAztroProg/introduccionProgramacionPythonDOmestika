nombre = input("Ingresa un nombre: ")

#elif
if nombre == "Gerardo":
    print(f"Saludos {nombre}")
elif nombre == "Jose":
    print(f"Saludos {nombre}")
else:
    print("Que extraño nombre")


#Operadores logicos 
"""
and 
or
not
"""
edad = int(input("Cual es tu edad "))

# las dos deben ser verdadero
if nombre == "Gerardo" and edad >= 20:
    print(f"Saludos {nombre}, eres un adulto")
if nombre == "Gerardo" and edad < 20:
    print(f"Saludos {nombre}, eres un joven")
else:
    print("Saludos")


if nombre == "Gerardo" or nombre == "rodrigo":
    print("Me gusta tu nombre")
else:
    print("Que nombre tan extraño")