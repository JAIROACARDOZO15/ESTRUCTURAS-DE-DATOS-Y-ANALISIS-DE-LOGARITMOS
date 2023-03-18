def minimizar_tiempo(tareas):
    tareas.sort(key=lambda x: x[1])
    
    tiempo_espera = [0] * len(tareas)
    for i in range(1, len(tareas)):
        for j in range(i):
            tiempo_espera[i] += tareas[j][1] - tareas[j][0]
    
    tiempo_total = sum(tiempo_espera)
 
    return tiempo_total


tareas = [(0, 5), (1, 2), (2, 7), (4, 5), (5, 6)]
tiempo_minimo_espera = minimizar_tiempo(tareas)
print("El tiempo mínimo de espera es:", tiempo_minimo_espera)
