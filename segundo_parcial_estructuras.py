# 2. Desarrollar el programa que permita construir el agendamiento de citas de un grupo de 3 abogados que atienden a su clientela, de lunes a viernes y de 8am a 12am, cada hora por usuario. El objetivo es digitar la identificación del profeional y se despliega el nombre y una lista con los días que este atiende (1-Lunes, 2-Martes, etc), el usuario digita el número del día y se visualizan las horas disponibles de este día, para digitar la cédula del usuario y asignar la cita, se debe generar un menú con las opciones de asignar cita, visualizar agenda de cada abogado y salir.

from collections import defaultdict

dias_semana = {1: "Lunes",2: "Martes",3: "Miércoles",4: "Jueves", 5: "Viernes"}

horas_disponibles = {"8am": True,"9am": True,"10am": True,"11am": True,"12pm": True}

agenda_abogados = {
    "1512": {
        "nombre": "JAIRO A CARDOZO",
        "dias_atencion": [1, 3, 5],
        "horas_disponibles": defaultdict(lambda: dict(horas_disponibles))
    }
}

def mostrar_menu():
    print("\n** MENÚ **")
    print("1. Asignar cita")
    print("2. Visualizar agenda de cada abogado")
    print("3. Salir")

def mostrar_agenda(abogado):
    print("\n La agenda del ", abogado["nombre"], "es: ")
    for dia, horas in abogado["horas_disponibles"].items():
        print("Día:", dias_semana[dia])
        print("Horas disponibles:")
        for hora, disponible in horas.items():
            if disponible:
                print("-", hora)
        print()

def asignar_cita():
    id_abogado = input("Ingrese la identificación del abogado: ")
    abogado = agenda_abogados.get(id_abogado)
    if abogado:
        print("Abogado encontrado:", abogado["nombre"])
        dia = int(input("Ingrese el número del día (1-Lunes, 2-Martes, 3-Miercoles, 4-Jueves, 5-Viernes): "))
        if dia in abogado["dias_atencion"]:
            horas = abogado["horas_disponibles"][dia]
            print("Horas disponibles que no estan agendadas:")
            for hora, disponible in horas.items():
                if disponible:
                    print("-", hora)
            hora = input("Ingrese la hora de la cita que desea asignar (ejemplo: 8am): ")
            if hora in horas and horas[hora]:
                cedula = input("Ingrese la cédula del cliente: ")
                horas[hora] = False
                print("Cita asignada con éxito, muchas gracias.")
            else:
                print("La hora ingresada no está disponible, nuestro abogado ya tiene agendada una cita.")
        else:
            print("El abogado no atiende ese día, rectificar el dia seleccionado.")
    else:
        print("La identificacion del abogado no coincide.")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        asignar_cita()
    elif opcion == "2":
        for abogado in agenda_abogados.values():
            mostrar_agenda
            mostrar_agenda(abogado)
    elif opcion == "3":
        print("¡Muchas gracias!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")