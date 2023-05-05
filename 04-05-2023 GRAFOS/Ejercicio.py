import numpy as np

nodos = 10
matriz_ady = np.zeros((nodos , nodos))

# NODO B
matriz_ady[1,0] = 1
matriz_ady[1,4] = 1
matriz_ady[1,9] = 1

#NODO D
matriz_ady[3,2] = 1
matriz_ady[3,4] = 1

#NODO F
matriz_ady[5,1] = 1
matriz_ady[5,6] = 1

#NODO G 
matriz_ady[6,8] = 1

#NODO I
matriz_ady[8,7] = 1

print(matriz_ady)

acu = 0 
mayor = 0

for i in range(0,10):
    acu = 0
    for j in range(0,10):
        acu = acu + matriz_ady [i,j]
    if acu > mayor:
        mayor = acu
        pos = i

if pos == 0:
    print("El Nodo con mayor número de relaciones es A")

if pos == 1:
    print("El Nodo con mayor número de relaciones es B")

if pos == 2:
    print("El Nodo con mayor número de relaciones es C")

if pos == 3:
    print("El Nodo con mayor número de relaciones es D")

if pos == 5:
    print("El Nodo con mayor número de relaciones es E")

if pos == 6:
    print("El Nodo con mayor número de relaciones es F")

if pos == 7:
    print("El Nodo con mayor número de relaciones es G")

if pos == 8:
    print("El Nodo con mayor número de relaciones es H")

if pos == 9:
    print("El Nodo con mayor número de relaciones es I")

if pos == 10:
    print("El Nodo con mayor número de relaciones es J")