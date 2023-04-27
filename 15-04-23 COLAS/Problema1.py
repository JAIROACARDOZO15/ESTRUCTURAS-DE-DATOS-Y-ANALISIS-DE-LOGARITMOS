# En un parqueadero con un solo túnel de estacionamiento, se colocan los carros uno tras otro, determinar para os últimos dos carros guardados el tiempo a cobrarles a partir de un momento definido por el usuario; igualmente se debe tener en cuenta que el parqueadero tiene una capacidad máxima de 20 carros. El valor del minuto es a $50.

# Importa los módulos necesarios
from time import perf_counter

# Se definen las variables a utilizar
estacionamiento = []
vehiculos_actuales = 0
vehiculos_max = 20
valor_minuto = 50

# Siempre mostrar el menu
while True:
    menu = input(
        """1. Ingresar vehículo al parqueadero
2. Calcular el costo total de los dos últimos vehículos
3. Salir del programa
"""
    )

    if menu == "1":
        if vehiculos_actuales < vehiculos_max:
            estacionamiento.append(perf_counter())
            vehiculos_actuales += 1
        else:
            print("No pueden ingresar más vehículos al parqueadero!")
    elif menu == "2":
        # Calcular el costo total para los n últimos vehículos
        for i in range(2):
            print(((perf_counter() - estacionamiento.pop()) / 60) * valor_minuto)
        # Detiene la ejecución del programa después de mostrar el resultado
        break
    elif menu == "3":
        # Detiene la ejecución del programa por elección del usuario
        break