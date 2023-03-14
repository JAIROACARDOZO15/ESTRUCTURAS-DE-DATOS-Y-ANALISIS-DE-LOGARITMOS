from time import time
import random
# A=int (input())
inicio = time ()
x = []

for i in range(50000):
    x.append(random.randint(0,1000))

for i in range(1,50000):
    for j in range(0,50000-i):
        if (x[j+1] < x[j]):
            aux=x[j];
            x[j]=x[j+1];
            x[j+1]=aux;

print(x)
tiempo = time() - inicio
print("Tiempo ejecución", tiempo)