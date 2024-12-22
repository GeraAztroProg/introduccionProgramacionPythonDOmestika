# Estas no pueden ser modificadas
lista = ["Rodrigo", "Juan"]
tupla = ("Rodrigo", "Juan")

print(lista)
print(tupla)

print(type(tupla))

lista[0] = "Gerardo"
print(lista)
# Tupla no se puede moficar tupla[0] = "Rosa"
# se usan como estructuras fijas

video_juegos = []
#nombre, genero, año
video_juegos.append(("Final Fantasy 7", "JRPG", 1997))
video_juegos.append(("Outer Wilds", "Aventura", 2019))

print(video_juegos)