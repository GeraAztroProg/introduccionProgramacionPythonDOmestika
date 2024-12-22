# Lista de elementos en modo llave/valor

persona = {
    "nombre": "Gerardo",
    "apellido": "Garduño",
    "edad": 34
}
print(persona)
print(type(persona))

#Son modficables pero no se acumulan los datos y se modifican
persona["apellido"] = "Gonzalez"
print(persona)

# agregar valores 
persona["apodo"] = "GameHack"
print(persona)

# obtencion de una lista de las llaves
lista_llave = persona.keys()
print(lista_llave)

for key in persona.keys():
    print(key)

# obtencion de una lista de valores
lista_valores = persona.values()
print(lista_valores)

for values in persona.values():
    print(values)

# lista de tuplas
lista_tuplas = persona.items()
print(lista_tuplas)

for key, value in persona.items():
    print(key)
    print(value)

#validacion 
print("apodo" in persona)