# Construir un árbol que mediante su recorrido Inorden permita generar la siguiente expresión matemática: X = 4*Y+(Z-2)/3 + (b-2)/4 , cada componente de la expresión es un nodo del árbol

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.ixq = None
        self.der = None

