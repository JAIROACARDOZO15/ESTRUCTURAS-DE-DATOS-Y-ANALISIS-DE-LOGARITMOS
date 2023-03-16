#!/usr/bin/env python3
# Adivinar una clave alfanumérica con caracteres especiales de cualquier longitud
# Nota: Esta implementación es mucho más eficiente que lo usual (hashcat) ya que no se está adivinando toda la contraseña a la vez si no que se está realizando por cada digito, lo que reduce las posibilidades y lo hace mucho más rápido, se podría decir que usa el concepto divide y vencerás
# Importa los módulos necesarios para la ejecución
from time import perf_counter
import string

# Pedir el input de la clave por adivinar
clave = input("Ingrese una clave: ")

# Empieza a tomar el tiempo de ejecución
inicio = perf_counter()

# Define las variables necesarias para realizar la comparación de cada digito
intento = ""
numeros = list(string.digits)
letras = list(string.ascii_lowercase + string.ascii_letters)
simbolos = list(string.punctuation)

# Crea un foor loop anidado (n^2) en el que recorre todos los digitos y los compara con todas las posibilidades
for digito in clave:
    # Comparamos con todas las letras
    for letra in letras:
        # Si la comparación es verdadera, se agrega el digito al intento y rompemos el último ciclo for
        if letra == digito:
            intento += letra
            break
    # Comparamos con todos los números
    for numero in numeros:
        # Si la comparación es verdadera, se agrega el digito al intento y rompemos el último ciclo for
        if numero == digito:
            intento += numero
            break
    # Comparamos con todos los simbolos
    for simbolo in simbolos:
        # Si la comparación es verdadera, se agrega el digito al intento y rompemos el último ciclo for
        if simbolo == digito:
            intento += simbolo
            break

# Imprime la clave ingresada ya una vez se adivinó completamente
print("La clave ingresada es: " + intento)

# Imprime la diferencia del tiempo de ejecución total
tiempo = perf_counter() - inicio
print("Tiempo de ejecución: " + str(round(tiempo, 4)) + " s")