class Nodo:
    def __init__(self, x):
        self.der = None
        self.ixq = None
        self.valor = x
        self.nodos_recorridos = 0  # Nuevo atributo para almacenar la cantidad de nodos recorridos

def preorden(nodo, objetivo, recorridos):
    if nodo:
        recorridos.append(nodo.valor)  # Almacenar el valor del nodo recorrido
        if nodo.valor == objetivo:
            print(f"Se recorrieron {len(recorridos) - 1} nodos antes de llegar al nodo {objetivo}.")
        preorden(nodo.ixq, objetivo, recorridos)
        preorden(nodo.der, objetivo, recorridos)
        recorridos.pop()  # Eliminar el valor del nodo recorrido al retroceder en el árbol

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

objetivo = input("Ingrese el valor del nodo objetivo: ")
preorden(raiz, objetivo, [])
