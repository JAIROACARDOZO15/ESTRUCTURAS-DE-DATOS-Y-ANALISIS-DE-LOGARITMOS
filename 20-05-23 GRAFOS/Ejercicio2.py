# Construir un programa en python sobre  una empresa requiere transportar X cantidad de peso por una ruta por definir entre dos puntos de acuerdo al grafo de la parte inferior, calcular el costo de transportar la carga entre dos puntos si el km de recorrido es a $20.000 por cada kg y los tramos entre cada nodo son en km. Se debe generar una cotización para el cliente, especificando el orígen y destino, la ruta a seguir y el costo del transporte
import heapq

# Definir el grafo como un diccionario de diccionarios
grafo = {
    'A': {'B': 5, 'D': 9, 'E': 2},
    'B': {'A': 5, 'C': 2},
    'C': {'B': 2, 'D': 3},
    'D': {'A': 9, 'C': 3, 'E': 2},
    'E': {'A': 2, 'D': 2}
}

def dijkstra(grafo, origen, destino):
    # Inicializar las estructuras de datos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    anteriores = {nodo: None for nodo in grafo}

    # Utilizar una cola de prioridad para almacenar los nodos a visitar
    cola = [(0, origen)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si ya se ha visitado el nodo, continuar al siguiente
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Explorar los nodos vecinos y actualizar las distancias
        for nodo_vecino, peso_arista in grafo[nodo_actual].items():
            distancia = distancia_actual + peso_arista
            if distancia < distancias[nodo_vecino]:
                distancias[nodo_vecino] = distancia
                anteriores[nodo_vecino] = nodo_actual
                heapq.heappush(cola, (distancia, nodo_vecino))

    # Reconstruir la ruta desde el destino hasta el origen
    ruta = []
    nodo_actual = destino
    while nodo_actual is not None:
        ruta.insert(0, nodo_actual)
        nodo_actual = anteriores[nodo_actual]

    return ruta, distancias[destino]

# Función para calcular el costo del transporte
def calcular_costo(carga, ruta):
    costo_total = carga * len(ruta) * 20000
    return costo_total

# Preguntar al usuario el origen, destino y cantidad de carga
origen = input("Ingrese el punto de origen: ")
destino = input("Ingrese el punto de destino: ")
carga = float(input("Ingrese la cantidad de carga en kg: "))

# Obtener la ruta más corta y el costo del transporte
ruta_mas_corta, distancia_total = dijkstra(grafo, origen, destino)
costo_transporte = calcular_costo(carga, ruta_mas_corta)

# Imprimir la cotización para el cliente
print("Cotización:")
print("Origen:", origen)
print("Destino:", destino)
print("Ruta:", " -> ".join(ruta_mas_corta))
print("Distancia total:", distancia_total)
print("Costo del transporte:", costo_transporte)