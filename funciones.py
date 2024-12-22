
#funcion
def saludar():
    print("Hola terricola")
    # pass -> se usa para solo nombrar a la funcion y saltar hasta que se ponga el codigo

# Llamar a la funcion
saludar()
saludar()
saludar()

# funcion con parametro 
def saludar2(nombre):
    print(f"Hola terricola {nombre}")

# llamando a la funcion con argumento
saludar2("Gerardo")    

def Cfar(celsius):
    # (C * 1.8)+32
    far = (celsius * 1.8) +32
    return f"los grados {celsius} son {far} fahrenheit"

# funcion con regreso de valor
resultado = Cfar(32)
print(resultado)

# dinamico, reutilizable y facil de contener
type(52)
range(2,10)

print("hfghfsh")