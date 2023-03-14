from time import time
import random
inicio = time ()

for n in range(1, 10000):
    divisores = []
    for divisor in range(1, n):
        if n % divisor == 0:
            divisores.append(divisor)

    if sum(divisores) == n:
        print(n)

tiempo = time() - inicio
print("Tiempo ejecución", tiempo)