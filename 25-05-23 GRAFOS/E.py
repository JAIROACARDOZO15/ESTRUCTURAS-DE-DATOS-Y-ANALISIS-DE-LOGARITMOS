#!/usr/bin/env python3
# Se recibe un archivo de texto en el que se encuentran las solicitudes de manejo de 5 documentos, en donde se define el destino final de los mismos, identificación y el nombre del solicitante. El vértice A es la oficina que recibe los documentos Determinar la duración en días de trámite para cada documento generando un ticket para cada usuario (archivo de texto cuyo nombre es la letra A seguida de la identificación del usuario) informando lo anterior. Calcular el area total de días requeridos para todos los documentos y generar una estadistica de las oficinas con documentos requeridos y el número de solicitudes por usuario. Todo lo anterior se debe manejar desde un menú de opciones.

# Se importan los módulos necesarios para la ejecución
import networkx as nx
import numpy as np
from datetime import date, timedelta

# Se define un diccionario y una matriz para crear el grafo
nombres_nodos = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H"}
matriz_ady = [
    [0, 3, 1, 0, 0, 0, 0, 0],
    [3, 0, 0, 1, 0, 0, 5, 0],
    [1, 0, 0, 2, 0, 5, 0, 0],
    [0, 1, 2, 0, 4, 2, 0, 0],
    [0, 0, 0, 4, 0, 0, 2, 1],
    [0, 0, 5, 2, 0, 0, 0, 3],
    [0, 5, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 1, 3, 0, 0],
]

# Se crea el grafo con los datos anteriores
grafo = nx.from_numpy_array(np.array(matriz_ady))  # type: ignore
grafo = nx.relabel_nodes(grafo, nombres_nodos)  # type: ignore
archivo = []

# Se crea un ciclo while infinito en donde se muestra el menú de opciones
while True:
    menu = input(
        "1. Importar archivo de solicitudes\n2. Generar tickets de usuarios\n3. Calcular el número de días requeridos para todos los documentos\n4. Generar estadísticas de las oficinas\n5. Salir\n"
    )
    # Se importa el archivo de texto con todas las solicitudes
    if menu == "1":
        # Se lee el archivo solicitudes
        with open("solicitudes.txt", "r") as archivo:
            # Se separa el archivo por líneas y por comas para obtener una lista de listas
            archivo = [linea.split(",") for linea in archivo.read().splitlines()]
            print("Archivo importado satisfactoriamente!")
    # Se generan los tickets de los usuarios
    elif menu == "2":
        contador = 1
        # Se recorren todas las personas en la lista principal
        for solicitud in archivo:
            # Se crea un ticket para cada solicitud con su correspondiente id
            ticket = open("A" + str(contador) + str(solicitud[1]) + ".txt", "w")
            duracion_dias = str(nx.dijkstra_path_length(grafo, "A", solicitud[0]))
            # Se agrega la duración del trámite a la lista principal
            solicitud.append(duracion_dias)
            # Se escriben los datos requeridos en el ticket
            ticket.write(
                "               TICKET DE ATENCIÓN"
                + "\n-------------------------------------------------"
                + "\nOficina de destino: "
                + solicitud[0]
                + "\nIdentificación solicitante: "
                + str(solicitud[1])
                + "\nNombre solicitante: "
                + solicitud[2]
                + "\nFecha de recibido: "
                + str(date.today().strftime("%d/%m/%Y"))
                + "\nFecha de posible entrega: "
                + str(
                    (date.today() + timedelta(days=int(duracion_dias))).strftime(
                        "%d/%m/%Y"
                    )
                )
                + "\nDuración del trámite: "
                + solicitud[3]
                + " días"
                + "\n-------------------------------------------------"
            )
            # Se cierra el archivo al que se escribió
            ticket.close()
            contador += 1
        print("Tickets generados satisfactoriamente!")
    elif menu == "3":
        # Se hace la sumatoria de los días totales para todos los trámites
        dias_totales = 0
        for solicitud in archivo:
            dias_totales += int(solicitud[3])
        print("Los trámites se van a tardar " + str(dias_totales) + " días en total!")
    elif menu == "4":
        # Se imprimen las estadísticas de cada oficina y cada persona
        print("---ESTADÍSTICAS---")
        print("\nNúmero de documentos envíados para cada oficina")
        # Se recorren todas las oficinas en el grafo
        for oficina in nombres_nodos.values():
            documentos = 0
            # Se recorren todas las solicitudes del archivo
            for solicitud in archivo:
                # Si el grafo se encuentra en la solicitud se cuenta
                if solicitud.count(oficina) == 1:
                    documentos += 1
            # Se imprime el número de documentos por cada oficina
            print(oficina + ": " + str(documentos))
        print("\nNúmero de documentos envíados por cada persona")
        # Se define una lista para almacenar los nombres de todos los solicitantes
        nombres = []
        # Se recorren las solicitudes y se agregan los nombres
        for nombre in archivo:
            # Se verifica que el nombre no esté ya en la lista para no repetirse
            if nombre[2] not in nombres:
                nombres.append(nombre[2])
        # Se recorren todos los nombres de los solicitantes
        for nombre in nombres:
            documentos = 0
            # Se recorren todas las solicitudes del archivo
            for solicitud in archivo:
                # Si el nombre se encuentra en la solicitud se cuenta
                if solicitud.count(nombre) == 1:
                    documentos += 1
            # Se imprime el número de documentos por cada persona
            print(nombre + ": " + str(documentos))
    elif menu == "5":
        print("Gracias por usar nuestros servicios!")
        # Se rompe el ciclo while con el menú para detener el programa
        break
    else:
        # Se verifica que el usuario digite una opción disponible
        print("Las opciones válidas son del 1 al 5!")