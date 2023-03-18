def mergesort(lista):
    if len(lista)==0 or len(lista)==1:
        return lista
    else:
        mitad=len(lista)//2
        izq=mergesort(lista[:mitad])
        der=mergesort(lista[mitad:])
        union=merge(izq,der)
        return union
def merge(izq,der):
    lista=[]
    i=0
    j=0
    while i<len(izq) and j<len(der):
        if izq[i]<der[j]:
            lista.append(izq[i])
            i=i+1
        else:
            lista.append(der[j])
            j=j+1
    lista=lista+der[j:]
    lista=lista+izq[i:]
    return lista

lista=[5,4,3,7,9]
print(mergesort(lista))