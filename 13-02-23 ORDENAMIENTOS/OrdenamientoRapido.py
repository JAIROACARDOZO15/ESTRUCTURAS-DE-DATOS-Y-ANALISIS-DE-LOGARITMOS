from time import time
import random
# A=int (input())
inicio = time ()
x = []
Numeros = 11000

# Define la función con el algoritmo a implementar
def ordenamiento_rapido(lista, bajo, alto):
    if bajo < alto:
        pivote = lista[alto]
        i = bajo - 1
        for j in range(bajo, alto):
            if lista[j] <= pivote:
                i = i + 1
                (lista[i], lista[j]) = (lista[j], lista[i])
        (lista[i + 1], lista[alto]) = (lista[alto], lista[i + 1])
        pi = i + 1
        ordenamiento_rapido(lista, bajo, pi - 1)
        ordenamiento_rapido(lista, pi + 1, alto)
    return lista

for i in range(Numeros):
    x.append(random.randint(0,1000))

print(ordenamiento_rapido(x, 0, len(x)-1))
tiempo = time() - inicio
print("Tiempo ejecución", tiempo)