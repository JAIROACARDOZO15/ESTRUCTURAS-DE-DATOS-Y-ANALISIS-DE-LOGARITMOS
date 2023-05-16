# RECORRER GRAFO SIMPLE 

grafo = {"A":["B","C"],"B":["C","D"],"C":["D","E"],"D":["E","H","I"],"E":["F","G"],"F":[],"G":[],"H":[],"I":[],}

origen = input("Digite origen: ")
if origen.upper() not in grafo:
    print("Nodo origen no está grafo")

else: 
    C = 0
    recorrido = []
    terminales = []
    visitados = [origen]

while(len(visitados) != 0):
    nodo = visitados.pop()
    if nodo.upper() not in recorrido:
        recorrido.append(nodo.upper())
        C = C + 1

    if len(grafo[nodo.upper()])==0:
        if nodo.upper() not in terminales:
            terminales.append(nodo.upper())
            C = C + 1

    for i in grafo[nodo.upper()]:
        visitados.append(i)

print(recorrido)
print(C-1)