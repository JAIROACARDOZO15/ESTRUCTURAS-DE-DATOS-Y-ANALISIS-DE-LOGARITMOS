# 1. Construir el correspondiente árbol binario de 4 niveles para la siguiente secuencia de números: 13,15,30,8,18,20,12,10,6,28,26,29,33,40,31 implemente con código básico y con la libreria Anytree para graficarlo


from anytree import Node, RenderTree
import os


class Nodo:
    def __init__(self, x):
        self.valor = x
        self.der = None
        self.izq = None


# Se define la lista recorrido para imprimir los nodos de forma más limpia
recorridos = []


# Se define la función para imprimir los nodos en preorden
def preorden(nodo):
    if nodo:
        recorridos.append(nodo.valor)
        preorden(nodo.izq)
        preorden(nodo.der)
    return recorridos


# Se define la función para imprimir los nodos en inorden
def inorden(nodo):
    if nodo:
        inorden(nodo.izq)
        recorridos.append(nodo.valor)
        inorden(nodo.der)
    return recorridos


# Se define la función para imprimir los nodos en postorden
def postorden(nodo):
    if nodo:
        postorden(nodo.izq)
        postorden(nodo.der)
        recorridos.append(nodo.valor)
    return recorridos


# Se define la función para determinar el recorrido total
def calcular_recorrido(lista, llegada):
    recorrido = 0
    for nodo in lista:
        if nodo == llegada:
            recorrido += 1
            break
        else:
            recorrido += 1
    return recorrido


# Se definen todos los nodos del árbol
raiz = Nodo(23)
raiz.izq = Nodo(15)  
raiz.der = Nodo(29)  
raiz.izq.izq = Nodo(8)  
raiz.izq.der = Nodo(18)  
raiz.izq.izq.izq = Nodo(6)  
raiz.izq.izq.der = Nodo(10)  
raiz.izq.der.izq = Nodo(12)  
raiz.izq.der.der = Nodo(20)  
raiz.der.izq = Nodo(28)  
raiz.der.der = Nodo(33)  
raiz.der.izq.izq = Nodo(26)  
raiz.der.izq.der = Nodo(30)  
raiz.der.der.izq = Nodo(31)  
raiz.der.der.der = Nodo(40)  

# Encontrar la diferencia entre el mayor valor y menor valor del árbol binario representado en el ejercicio anterior.
print(max(preorden(raiz)) - min(preorden(raiz)))


raiz = Node(23)
raizizq = Node(15, parent=raiz)
raizder = Node(29, parent=raiz)
raizizqizq = Node(8, parent=raizizq)
raizizqder = Node(18, parent=raizizq)
raizizqizqizq = Node(6, parent=raizizqizq)
raizizqizqder = Node(10, parent=raizizqizq)
raizizqderizq = Node(12, parent=raizizqder)
raizizqderder = Node(20, parent=raizizqder)
raizderizq = Node(28, parent=raizder)
raizderder = Node(33, parent=raizder)
raizderizqizq = Node(26, parent=raizderizq)
raizderizqder = Node(30, parent=raizderizq)
raizderderizq = Node(31, parent=raizderder)
raizderderder = Node(40, parent=raizderder)

for pre, fill, node in RenderTree(raiz):
    print("%s%s" % (pre, node.name))

# Crear una lista con todas las hojas del árbol binario del punto 1
class Nodo:
    def __init__(self, x):
        self.valor = x
        self.der = None
        self.izq = None


def encontrar_hojas(nodo, hojas):
    if nodo:
        if nodo.izq is None and nodo.der is None:
            hojas.append(nodo.valor)
        encontrar_hojas(nodo.izq, hojas)
        encontrar_hojas(nodo.der, hojas)


# Crear el árbol
raiz = Nodo(23)
raiz.izq = Nodo(15)
raiz.der = Nodo(29)
raiz.izq.izq = Nodo(8)
raiz.izq.der = Nodo(18)
raiz.izq.izq.izq = Nodo(6)
raiz.izq.izq.der = Nodo(10)
raiz.izq.der.izq = Nodo(12)
raiz.izq.der.der = Nodo(20)
raiz.der.izq = Nodo(28)
raiz.der.der = Nodo(33)
raiz.der.izq.izq = Nodo(26)
raiz.der.izq.der = Nodo(30)
raiz.der.der.izq = Nodo(31)
raiz.der.der.der = Nodo(40)

# Encontrar las hojas del árbol
hojas = []
encontrar_hojas(raiz, hojas)

# Imprimir la lista de hojas
print("Lista de hojas del árbol:")
print(hojas)
