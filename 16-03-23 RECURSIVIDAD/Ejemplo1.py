class Mochila:
    def __init__(self,peso,valor,posicion):
        self.index=posicion 
        self.peso=peso 
        self.valor=valor 
        self.report=valor//peso 

def llenar(peso,valores,capacidad):
    lista_pesos=[]
    for i in range(len(peso)):
        lista_pesos.append(Mochila(peso[i],valores[i],i))

    c=0
    for x in lista_pesos:
        pesoactual=int(x.peso)
        valoractual=int(x.valor)
        if capacidad-pesoactual>=0:
            capacidad=capacidad-pesoactual
            c= c+valoractual
    return c

capacidad= int(input("DIgite capacidad en peso de la mochila: "))
peso=[1,2,4,6,8]
valores= [10,25,40,55,70]

maximo= llenar(peso, valores, capacidad)
print("Valor maximo guardado en la mochila = ", maximo)