conductores = []
n = int(input("Ingrese la cantidad de conductores en la empresa: "))
x = int(input("Ingrese la cantidad de viajes que realiza cada conductor al día: "))

for i in range(n):
    nombre = input(f"Ingrese el nombre del conductor {i+1}: ")
    km = float(input(f"Ingrese el kilometraje promedio diario del conductor {nombre}: "))
    conductores.append({"nombre": nombre, "km": km})

while True:
    print("------- MENÚ -------")
    print("1. Mostrar el nombre del conductor con mayor recorrido")
    print("2. Mostrar el nombre del conductor con mayor kilometraje promedio diario")
    print("3. Generar el total de viajes generados en la empresa")
    print("4. Salir")

    opcion = int(input("Ingrese la opción que desee ejecutar: "))

    if opcion == 1:
        conductor_mayor_recorrido = max(conductores, key=lambda c: c["km"])
        print(f"El conductor con mayor recorrido es: {conductor_mayor_recorrido['nombre']}")

    elif opcion == 2:
        conductor_mayor_promedio = max(conductores, key=lambda c: c["km"]/x)
        print(f"El conductor con mayor kilometraje promedio diario es: {conductor_mayor_promedio['nombre']}")

    elif opcion == 3:
        total_viajes = n * x
        print(f"El total de viajes generados en la empresa es: {total_viajes}")

    elif opcion == 4:
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
