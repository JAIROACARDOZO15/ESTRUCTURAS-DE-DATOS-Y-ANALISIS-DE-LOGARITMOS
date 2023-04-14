# En un parqueadero con un solo túnel de estacionamiento, se colocan los carros uno tras otro, determinar para los últimos dos carros guardados el tiempo a cobrarles a partir de un momento definido por el usuario; igualmente se debe de tener en cuenta que el parqueadero tiene una capacidad máxima de 20 carros. El valor del minuto es a $50 

from time import time
class pila:
    def __init__(self):
        self.pila = []
    def extraer(self):
        if len(self.pila)<1:
            print("Pila no tiene elementos")
            return None
        return self.pila.pop()
    def ingresar(self,item):
        self.pila.append(item)

mipila=pila()
opcion=1
limite=0
while limite<=20 and opcion ==1:
    opcion=int(input("Digite 1 si llega un carro, 2 para terminar: "))
    limite=limite+1
    if opcion ==1:
        mipila.ingresar(time())
        