#!/usr/bin/env python3
# El facturador de una empresa atiende 5 personas por hora (12 minutos por persona), las cuáles llegan 6 por hora (1 persona cada 10 minutos) en un período de 2 horas a partir de las 8 A.M y hasta las 10 A.M, determine el promedio de las ventas de las personas atendidas en los primeros treinta y seis minutos.

# Se importa el módulo random
import random

# Se definen las variables a utilizar en el programa
ventas = []
promedio_ventas = 0
personas_atendidas = 0
tiempo_cola = 0
tiempo_atencion = 0

# Simulación durante 36 minutos
minutos_totales = 36

# Ciclo en el que se forma la gente en la cola
while tiempo_cola + 10 < minutos_totales:
    # Llega una nueva persona para hacer una compra
    ventas.append(random.randint(100, 10000))
    # Transcurren 10 minutos
    tiempo_cola += 10

# Ciclo en el que el facturador atiende a las personas en la cola
while tiempo_atencion < minutos_totales:
    # El facturador atiende a una persona
    promedio_ventas += ventas.pop(0)
    personas_atendidas += 1
    # Transcurren 12 minutos
    tiempo_atencion += 12

# Verificar si hubieron personas atendidas
if personas_atendidas > 0:
    promedio_ventas /= personas_atendidas
else:
    promedio_ventas = 0

print("El promedio de las ventas es de $" + str(int(promedio_ventas)))

from time import perf_counter
import tkinter as tk


def formar_persona():
    cola.append(perf_counter())


def abrir_negocio(posicion):
    if posicion > 0:
        tiempo_transcurrido = (perf_counter() - cola.pop(0)) / 60
        tiempo_apertura = int(tiempo_transcurrido + 3 * (posicion))
        return str(tiempo_apertura) + " m"
    else:
        return "0 m"

def mostrar_resultados():
    for i in range(len(cola)):
        label_posicion = tk.Label(text=i + 1, font=("Arial", 16), fg="#fff", bg="#000")
        label_posicion.grid(row=i, column=2, padx=10, pady=10, sticky="w")
    for i in range(len(cola)):
        label_tiempoatencion = tk.Label(
            text=abrir_negocio(i), font=("Arial", 16), fg="#000", bg="#fff"
        )
        label_tiempoatencion.grid(row=i, column=3, padx=10, pady=10, sticky="w")


cola = []

ventana = tk.Tk()
ventana.geometry("1920x1080")
ventana.title("Programa cola de cajero")
ventana.config(bg="#fff")

titulo = tk.Label(text="Programa cola de cajero", font=("Arial", 24), bg="#fff")
titulo.grid(column=0, row=0, columnspan=4, pady=20)

boton_nueva = tk.Button(
    ventana,
    text="Formar nueva persona en la cola",
    command=formar_persona,
    font=("Arial", 16),
    bg="#000",
    fg="#fff",
)
boton_nueva.grid(column=0, row=1, padx=10, pady=10)

boton_abrir = tk.Button(
    ventana,
    text="Abrir el negocio y calcular el tiempo de atención",
    command=mostrar_resultados,
    font=("Arial", 16),
    bg="#000",
    fg="#fff",
)
boton_abrir.grid(column=0, row=3, padx=10, pady=10)

boton_salir = tk.Button(
    ventana,
    text="Salir del programa",
    command=ventana.destroy,
    font=("Arial", 16),
    bg="#000",
    fg="#fff",
)
boton_salir.grid(column=0, row=4, padx=10, pady=10)

ventana.mainloop()