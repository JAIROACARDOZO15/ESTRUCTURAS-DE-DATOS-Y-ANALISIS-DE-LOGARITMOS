#!/usr/bin/env python3
from time import perf_counter
import random


def ordenamiento_rapido(lista, izquierda, derecha):
    if izquierda < derecha:
        pivote = lista[derecha]
        i = izquierda - 1
        for j in range(izquierda, derecha):
            if lista[j] <= pivote:
                i = i + 1
                (lista[i], lista[j]) = (lista[j], lista[i])
        (lista[i + 1], lista[derecha]) = (lista[derecha], lista[i + 1])
        pi = i + 1
        ordenamiento_rapido(lista, izquierda, pi - 1)
        ordenamiento_rapido(lista, pi + 1, derecha)
    return lista


# Inicia el tiempo de ejecución inicial
inicio = perf_counter()
entradas_n = 20000
numeros = []
numeros_menores = []
sumatoria = 0

while len(numeros) < entradas_n:
    valor = random.randint(0, 1000)
    if valor % 2 == 0:
        numeros.append(valor)
        sumatoria += valor

promedio = sumatoria / len(numeros)

menores_promedio = 0

for numero in numeros:
    if numero < promedio:
        menores_promedio += 1
        numeros_menores.append(numero)

if menores_promedio < (entradas_n / 2):
    print(
        "Lista ordenada: "
        + str(ordenamiento_rapido(numeros_menores, 0, len(numeros_menores) - 1))
    )

# Imprime la diferencia del tiempo de ejecución total
tiempo = perf_counter() - inicio
print("Tiempo de ejecución: " + str(round(tiempo, 4)) + " s")