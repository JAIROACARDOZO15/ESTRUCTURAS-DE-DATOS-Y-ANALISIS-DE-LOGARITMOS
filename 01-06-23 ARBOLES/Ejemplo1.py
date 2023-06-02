class Nodo:
    def __init__(self,x):
        self.der = None
        self.ixq = None
        self.valor = x

def preorden(nodo):
    if nodo:
        preorden(nodo.ixq)
        preorden(nodo.der)
        print(nodo.valor)

def Inorden(nodo):
    if nodo:
        Inorden(nodo.ixq)
        Inorden(nodo.der)
        print(nodo.valor)

def postOrden(nodo):
    if nodo:
        postOrden(nodo.ixq)
        postOrden(nodo.der)
        print(nodo.valor)

raiz = Nodo("1")
raiz.ixq = Nodo("2")
raiz.der = Nodo("5")
raiz.ixq.ixq = Nodo("3")
raiz.ixq.der = Nodo("4")
raiz.der.ixq = Nodo("6")
raiz.der.der = Nodo("7")

preorden(raiz)