#!/usr/bin/env python3
from time import perf_counter
import random

# Pedir el input de n números del vector
n = int(input("Ingrese un número n: "))

# Inicia el tiempo de ejecución inicial
inicio = perf_counter()

# Crea una lista con diez números pseudoaleatorios
numeros = []

for numero in range(n):
    numeros.append(bin(random.randint(1000, 9999))[2:])

# Ejecuta el algoritmo y lo imprime en pantalla
print("Números binarios: " + str(numeros))

# Imprime la diferencia del tiempo de ejecución total
tiempo = perf_counter() - inicio
print("Tiempo de ejecución: " + str(round(tiempo,4))+"s")