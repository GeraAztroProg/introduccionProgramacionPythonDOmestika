#Logico o boleano (verdadero o falso)
dato = True
print(dato)
print(type(dato))

# Se esta realizando una comparacion
datos2 = 5 > 3
print(datos2)

"""
== igual
!= disntinto
> mayor
< menor
>= mayor o igual
<= menor o igual
"""

# Control de flujo
numero = 20

if numero == 10:
    print(f"El numero es {numero}")
else:
    print("El numero no es 10")

print("Terminando programa")


nombre = input("Ingresa tu nombre")

if nombre == "Gerardo":
    print(f("Bienvenido {nombre}"))
else:
    print("Que nombre tan extraño")