# Una empresa tiene un grupo de n conductores quienes cada día realizan x viajes, cada uno, almacenar en una lista los nombres y el kilometraje promedio diario de cada conductor. Generar un menú de opciones que permita: 
#1. Mostrar el nombre del conductor con mayor recorrido
#2. Mostrar el nombre del conductor con mayor kilometraje promedio diario
#3. Generar el total de viajes generados en la empresa.
#4. Salir
lista_conductores = []
l2 = []
l3 = []
a3 = 0

n=int(input("Digite número conductores:"))
for i in range(n):
    nombre=input("Digite nombre conductor:")
    lista_conductores.append(nombre)
    x=int(input("Digite número de viajes:"))
    a3=a3+x
    a1=0
    for j in range(x):
        k=int(input("Digite número de km recorridos:"))
        a1=a1+k
    l2.append(a1)
    l3.append(a1/x)
    
opcion=0
while opcion!=4:
    print("Menu Principal")
    print("1. Conductor con mayor recorrido")
    print("2. Conductor con mayor promedio de km recorridos")
    print("3. Total viajes generados en la empresa")
    print("4. Salir")
    opcion=int(input("Digite opción:"))
    if opcion==1:
        mayor=0
        for i in range(n):
            if l2[i]>mayor:
                mayor=l2[i]
                pos=i
        print("Conductor:",lista_conductores[pos])
    if opcion==2:
        mayor=0
        for i in range(n):
            if l3[i]>mayor:
                mayor=l3[i]
                pos=i
        print("Conductor:",lista_conductores[pos])
    if opcion==3:
        print("Total de viajes:",a3)