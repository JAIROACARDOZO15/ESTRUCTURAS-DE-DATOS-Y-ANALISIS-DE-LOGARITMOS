# GENERAR NUMERO DE PAQUETES INGRESADOS A LA MOCHILA

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
    indice_mochila = []
    for x in sorted(lista_pesos, key=lambda x: x.report, reverse=True):
        pesoactual=int(x.peso)
        valoractual=int(x.valor)
        if capacidad-pesoactual>=0:
            capacidad=capacidad-pesoactual
            c= c+valoractual
            indice_mochila.append(x.index)
    return c, indice_mochila

capacidad= int(input("Digite capacidad en peso de la mochila: "))
peso=[1,2,4,6,8]
valores= [10,25,40,55,70]

maximo, paquetes= llenar(peso, valores, capacidad)
print("Valor máximo guardado en la mochila = ", maximo)
print("Número de paquetes ingresados a la mochila: ", len(paquetes))
print("Índices de los paquetes ingresados a la mochila: ", paquetes)
