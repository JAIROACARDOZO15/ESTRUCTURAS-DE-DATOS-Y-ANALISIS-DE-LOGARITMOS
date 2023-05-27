# construir un programa en python sobre una empresa agropecuaria tiene su propiedad dividida en 7 porteros para el engorde de bovinos, el mapa de estos potreros es el siguiente, las distancias están en Hectometros. Mediante un programa determine cuál debe ser el recorrido ideal para asegurarse de llevar suplementos alimenticios a cada uno de los potreros, la longitud del mismo en metros y calcular la cantidad de alimento en cada potrero, si la cantidad a suministrar se calcula dando 100g por cada animal.

import itertools

# Definir el mapa de los potreros con las distancias en hectómetros
mapa_potreros = {
    'Potrero1': {'Potrero2': 1, 'Potrero3': 2, 'Potrero4': 3, 'Potrero5': 4, 'Potrero6': 5, 'Potrero7': 6},
    'Potrero2': {'Potrero1': 1, 'Potrero3': 2, 'Potrero4': 3, 'Potrero5': 4, 'Potrero6': 5, 'Potrero7': 6},
    'Potrero3': {'Potrero1': 2, 'Potrero2': 2, 'Potrero4': 1, 'Potrero5': 2, 'Potrero6': 3, 'Potrero7': 4},
    'Potrero4': {'Potrero1': 3, 'Potrero2': 3, 'Potrero3': 1, 'Potrero5': 1, 'Potrero6': 2, 'Potrero7': 3},
    'Potrero5': {'Potrero1': 4, 'Potrero2': 4, 'Potrero3': 2, 'Potrero4': 1, 'Potrero6': 1, 'Potrero7': 2},
    'Potrero6': {'Potrero1': 5, 'Potrero2': 5, 'Potrero3': 3, 'Potrero4': 2, 'Potrero5': 1, 'Potrero7': 1},
    'Potrero7': {'Potrero1': 6, 'Potrero2': 6, 'Potrero3': 4, 'Potrero4': 3, 'Potrero5': 2, 'Potrero6': 1}
}

def tsp(mapa):
    # Obtener la lista de potreros
    potreros = list(mapa.keys())

    # Generar todas las permutaciones posibles de los potreros
    rutas = list(itertools.permutations(potreros))

    # Inicializar la distancia mínima y la ruta ideal
    distancia_minima = float('inf')
    ruta_ideal = []

    # Calcular la distancia total para cada ruta
    for ruta in rutas:
        distancia_total = 0

        # Calcular la distancia entre potreros consecutivos
        for i in range(len(ruta) - 1):
            distancia_total += mapa[ruta[i]][ruta[i+1]]

        # Calcular la distancia de regreso al punto de partida
        distancia_total += mapa[ruta[-1]][ruta[0]]

        # Actualizar la distancia mínima y la ruta ideal si se encuentra una mejor opción
        if distancia_total < distancia_minima:
            distancia_minima = distancia_total
            ruta_ideal = ruta

    return ruta_ideal, distancia_minima

# Función para calcular la cantidad de alimento en cada potrero
def calcular_alimento(potreros, cantidad_animales):
    alimento_por_animal = 100  # 100 gramos por animal
    alimento_por_potrero = {potrero: cantidad_animales * alimento_por_animal for potrero in potreros}
    return alimento_por_potrero

# Obtener el recorrido ideal y la distancia mínima
recorrido_ideal, distancia_minima = tsp(mapa_potreros)

# Preguntar al usuario la cantidad de animales
cantidad_animales = int(input("Ingrese la cantidad de animales en los potreros: "))

# Calcular la cantidad de alimento en cada potrero
alimento_por_potrero = calcular_alimento(recorrido_ideal, cantidad_animales)

# Imprimir el recorrido ideal y la cantidad de alimento en cada potrero
print("Recorrido ideal:")
for i in range(len(recorrido_ideal)):
    print(i+1, "-", recorrido_ideal[i])
print("Distancia mínima recorrida:", distancia_minima, "hectómetros")
print("Cantidad de alimento por potrero:")
for potrero, cantidad_alimento in alimento_por_potrero.items():
    print(potrero, "-", cantidad_alimento, "gramos")
