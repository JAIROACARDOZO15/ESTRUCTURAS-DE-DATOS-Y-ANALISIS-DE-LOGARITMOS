from time import time
import random
# A=int (input())
inicio = time ()
pares = 0
porcentaje = 0
x = []
Numeros = 500000

for i in range(Numeros):
    x.append(random.randint(0,1000))

for i in range (1, Numeros):
    if (x[i] % 2 == 0):
        pares = pares + 1

if Numeros > 0:
    porcentaje = (pares/Numeros)*100

print(x)
tiempo = time() - inicio
print("Tiempo ejecución", tiempo, "\nPorcentaje de numeros pares encontrados: ", porcentaje, "%" )