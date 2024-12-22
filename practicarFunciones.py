"""
Para empezar, define una nueva función que reciba 3 parámetros. Esta función debe usar el primer parámetro para decidir qué operación hacer (suma, resta, multiplicación o división) y aplicarlo sobre los 2 parámetros restantes.

Ejemplo: resultado = tufuncion(“multiplicar”, 5, 4). (El resultado debería ser igual a 20)
Nota: Aquí estoy considerando que la función se llama “tufuncion”. En tu ejercicio pon el nombre que gustes a tu función.

Comparte tus avances en el foro.
"""
def calculadora(operacion, num1, num2):

    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division":
        return num1 / num2
    else:
        return "Operacion invalida (suma, resta, multiplicacion, division)"

#Capturando los datos
num1 = int(input("Ingresa un numero entero "))
num2 = int(input("Ingresa otro numero entero"))
operacion = input ("Que operacion deseas realizar: \n suma, resta, multiplicacion, divicion ")

#Ejecutando la funcion
resultado = calculadora(operacion, num1, num2)
print(resultado)
resultado1 = calculadora(operacion, num1, num2)
print(resultado1)