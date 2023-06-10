#Para un nodo definido por el usuario decir cuantos nodos se recorrieron antes de llegar a el
class Nodo:
    def __init__(self,x):
        self.der = None
        self.ixq = None
        self.valor = x

def preorden(nodo):
    if nodo:
        print(nodo.valor)
        preorden(nodo.ixq)
        preorden(nodo.der)

def Inorden(nodo):
    if nodo:
        Inorden(nodo.ixq)
        print(nodo.valor)
        Inorden(nodo.der)

def postOrden(nodo):
    if nodo:
        postOrden(nodo.ixq)
        postOrden(nodo.der)
        print(nodo.valor)

raiz = Nodo("A")
raiz.ixq = Nodo("B")
raiz.ixq.der = Nodo("F")
raiz.ixq.der.der = Nodo("G")
raiz.ixq.ixq = Nodo("C")
raiz.ixq.ixq.der = Nodo("E")
raiz.ixq.ixq.ixq = Nodo("D")
raiz.der = Nodo("H")
raiz.der.ixq = Nodo("I")
raiz.der.ixq.ixq = Nodo("k")
raiz.der.ixq.ixq.der = Nodo("L")
raiz.der.der = Nodo("J")
raiz.der.der.ixq = Nodo("M")
raiz.der.der.der = Nodo("N")
raiz.der.der.der.ixq = Nodo("O")


preorden(raiz)