from time import time

class Cola:
  def _init_(self):
    self.cola=[]

  def insertar(self,valor):
    self.cola.append(valor)

  def atender(self):
    if len(self.cola)<1:
      print("Cola no tiene elementos")
      return None
    return self.cola.pop(0)

cola1=Cola()
abierto=0
personas=0
while abierto==0:
  nuevo=int(input("Digite 1 si llego una nueva persona:"))
  if nuevo==1:
    x=time()
    cola1.insertar(x)
    personas=personas+1
  if personas>7:
    timepo2=time()
    abierto=int(input("Digite 1 si se ya se abrio el negocio"))