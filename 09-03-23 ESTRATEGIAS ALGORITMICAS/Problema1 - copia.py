from time import time
import random
inicio = time ()

n = 10000
acu = 0
divisor = []
for i in range(1,10000):
    if (n%i ==0):
        acu = acu + i
    divisor.append(acu)


tiempo = time() - inicio
print("Tiempo ejecución", tiempo)