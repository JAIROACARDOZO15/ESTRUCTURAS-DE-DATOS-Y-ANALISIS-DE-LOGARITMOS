from time import time
import random
from statistics import mean

inicio = time()
x = []
y = []
c = 0
c1 = 0
acu = 0

n = int(input("DIGITE EL VALOR DE N: "))
while n<=0:
    print("NUMERO INCORRECTO DEBE SER MAYOR QUE 0")
    n = int(input("DIGITE EL VALOR DE N: "))

while c<n:
    z = random.randint(0, 1000)
    if z%2 == 0:
        x.append(z)
        c+=1
        acu+=z

pro=acu/n
# CALCULO NUMEROS MENORES QUE EL PROMEDIO 
for i in range(n):
    if x [i]<pro:
        c1+=1
        y.append(x[i])

if c1<n/2:
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


print(x)
print(c1)
print(ordenamiento_rapido(y, 0, len(y)-1))
tiempo = time() - inicio
print("Tiempo ejecución", tiempo)