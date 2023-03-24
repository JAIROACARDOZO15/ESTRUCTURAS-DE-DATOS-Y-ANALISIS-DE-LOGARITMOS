class Lista:
    def __init__(self):
        Lista.primer_nodo = None
    
    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.dir = self.primer_nodo
        self.primer_nodo = nuevo_nodo

    def recorrer_lista(self):
        if self.primer_nodo is None:
            print("No existe lista a recorrer")
            return
        else:
            n = self.primer_nodo
            while n is not None:
                print(n.item, "")
                n = n.dir

    def insertar_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.primer_nodo is None:
            self.primer_nodo = nuevo_nodo
            return
        n = self.primer_nodo
        while n.dir is not None:
            n = n.dir
        n.dir = nuevo_nodo

    def crear_lista(self):
        nodos = int(input("Cantidad de Nodos: "))
        while nodos <= 0:
            print("Cantidad de nodos debe ser mayor a 0")
            nodos = int(input("Cantidad de Nodos: "))
        if nodos > 0:
            for i in range(nodos):
                valor = int(input("Digite valor: "))
                self.insertar_final(valor)

    def invertir_lista(self):
        prev = None
        n = self.primer_nodo
        while n is not None:
            next = n.dir
            n.dir = prev
            prev = n
            n = next
        self.primer_nodo = prev

class Nodo:
    def __init__(self, valor):
        self.item = valor
        self.dir = None

milista = Lista()
milista.crear_lista()
milista.recorrer_lista()
milista.invertir_lista()
milista.insertar_inicio(int(input("Digite valor: ")))
milista.recorrer_lista()