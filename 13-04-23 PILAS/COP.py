parqueadero = []

while True:
    print("------- MENÚ -------")
    print("1. Ingresar un carro al parqueadero")
    print("2. Calcular el tiempo de estacionamiento para los últimos dos carros")
    print("3. Salir")

    opcion = int(input("Ingrese la opción que desee ejecutar: "))

    if opcion == 1:
        if len(parqueadero) >= 20:
            print("El parqueadero está lleno.")
        else:
            placa = input("Ingrese la placa del carro: ")
            hora_llegada = float(input("Ingrese la hora de llegada (en horas, ej: 9.5): "))
            parqueadero.append({"placa": placa, "hora_llegada": hora_llegada})
            print(f"El carro con placa {placa} ha sido estacionado en el parqueadero.")

    elif opcion == 2:
        if len(parqueadero) < 2:
            print("Debe haber al menos dos carros en el parqueadero para realizar esta operación.")
        else:
            hora_cobro = float(input("Ingrese la hora a partir de la cual desea calcular el tiempo de estacionamiento (en horas, ej: 9.5): "))
            carro1 = parqueadero[-1]
            carro2 = parqueadero[-2]
            tiempo_estacionamiento = hora_cobro - max(carro1["hora_llegada"], carro2["hora_llegada"])
            valor_cobro = tiempo_estacionamiento * 50
            print(f"El tiempo de estacionamiento para los últimos dos carros es de {tiempo_estacionamiento} horas, y el valor a cobrar es de ${valor_cobro}.")

    elif opcion == 3:
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")
