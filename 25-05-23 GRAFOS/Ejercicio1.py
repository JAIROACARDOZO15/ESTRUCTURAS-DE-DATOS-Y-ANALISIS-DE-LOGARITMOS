#Se recibe un archivo de texto en el que se encuentran las solicitudes de manejo de 5 documentos, en donde se define el destino final de los mismos, identificación y el nombre del solicitante. EI vértice A es la oficina que recibe los documentos. Determinar la duración en días de trámite para cada documento generando un ticket para cada usuario (archivo de texto cuyo nombre es la letra A seguida de la identificación del usuario) informando l0 anterior. Calcular el total de días requeridos para todos los documentos y generar una estadística de las oficinas con documentos requeridos y el número de solicitudes por usuario. Todo lo anterior se debe manejar desde un menú de opciones.

import datetime

def recibir_solicitudes():
    archivo = input("Ingrese el nombre del archivo de texto: ")
    with open(archivo, 'r') as file:
        lineas = file.readlines()

    documentos = []
    for linea in lineas:
        datos = linea.strip().split(',')
        documento = {
            'destino': datos[0],
            'identificacion': datos[1],
            'solicitante': datos[2]
        }
        documentos.append(documento)

    return documentos

def procesar_documentos(documentos):
    total_dias = 0
    estadisticas_oficinas = {}
    estadisticas_usuarios = {}

    for documento in documentos:
        destino = documento['destino']
        identificacion = documento['identificacion']
        solicitante = documento['solicitante']

        # Calcular duración en días
        duracion = int(input(f"Ingrese la duración en días para el documento {identificacion}: "))
        total_dias += duracion

        # Generar ticket
        ticket = f"A{identificacion}.txt"
        with open(ticket, 'w') as file:
            file.write(f"Destino: {destino}\n")
            file.write(f"Identificación: {identificacion}\n")
            file.write(f"Solicitante: {solicitante}\n")
            file.write(f"Duración en días: {duracion}\n")
            file.write(f"Fecha de recepción: {datetime.date.today().strftime('%d-%m-%Y')}\n")
            fecha_entrega = datetime.date.today() + datetime.timedelta(days=duracion)
            file.write(f"Fecha de entrega: {fecha_entrega.strftime('%d-%m-%Y')}\n")

        # Actualizar estadísticas de oficinas
        if destino in estadisticas_oficinas:
            estadisticas_oficinas[destino] += 1
        else:
            estadisticas_oficinas[destino] = 1

        # Actualizar estadísticas de usuarios
        if identificacion in estadisticas_usuarios:
            estadisticas_usuarios[identificacion] += 1
        else:
            estadisticas_usuarios[identificacion] = 1

    return total_dias, estadisticas_oficinas, estadisticas_usuarios

def mostrar_estadisticas(total_dias, estadisticas_oficinas, estadisticas_usuarios):
    print("Estadísticas:")
    print(f"Total de días requeridos para todos los documentos: {total_dias}")
    print("Oficinas con documentos requeridos:")
    for oficina, cantidad in estadisticas_oficinas.items():
        print(f"{oficina}: {cantidad} solicitudes")
    print("Número de solicitudes por usuario:")
    for usuario, cantidad in estadisticas_usuarios.items():
        print(f"Usuario {usuario}: {cantidad} solicitudes")

def menu():
    documentos = []

    while True:
        print("\nMenú de opciones:")
        print("1. Recibir solicitudes")
        print("2. Procesar documentos")
        print("3. Mostrar estadísticas")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            documentos = recibir_solicitudes()
        elif opcion == '2':
            if len(documentos) == 0:
                print("No se han recibido solicitudes aún.")
            else:
                total_dias, estadisticas_oficinas, estadisticas_usuarios = procesar_documentos(documentos)
                print("Documentos procesados correctamente.")
        elif opcion == '3':
            if len(documentos) == 0:
                print("No se han recibido solicitudes aún.")
            else:
                mostrar_estadisticas(total_dias, estadisticas_oficinas, estadisticas_usuarios)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
