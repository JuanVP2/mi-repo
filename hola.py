print ("¡Hola, Mundo!")

a = 5
b = 10
c = 15

resultado = (a + b) * c
print("El resultado es:", resultado)


edad = 15

if edad < 18:
    print("eres menor de edad")
elif edad >=18 and edad <=60:
    print("eres adulto")
elif edad > 15:  #no se ejecuta
    print("mayor de 15 ")
elif edad == 60:
    print("eres viejo")
else:
    print("eres mayor")


frutas = ["manzana", "banana", "naranja"]

for i in frutas:
    print(i)


contador = 0

while contador <= 5:
    print(contador)
    contador += 1

for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

frutas = ["manzana", "banana", "naranja"]


frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]


frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]


frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]


fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"


frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]


frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]


numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}


def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


import math

resultado = math.sqrt(25) #raiz cuadrada
print(resultado)  # Imprime 5.0 



import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual



numeros = [1,2,3,4,5,6,12,9,8,25,32,2,4,6]

def pares(numeros):
    return numeros % 2 == 0 

def pares_unicos(numeros):
    numeros_pares = set()
    for numero in numeros:
        if pares(numero):
            numeros_pares.add(numero)
    return numeros_pares

def suma(numeros):
    return sum(numeros)

numero = pares_unicos(numeros)
print(f"cadena de numeros {numero}")
print(f"suma: {suma(numero)}")