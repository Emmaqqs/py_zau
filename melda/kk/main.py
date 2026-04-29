from promedio import (
    calcular_promedio,
    obtener_maximo,
    obtener_minimo,
    contar_aprobados,
    contar_reprobados
)
calificaciones = []
n = int(input("¿Cuántas calificaciones desea ingresar? "))
for i in range(n):
    cal = float(input(f"Calificación {i+1}: "))
    calificaciones.append(cal)
prom = calcular_promedio(calificaciones)
maximo = obtener_maximo(calificaciones)
minimo = obtener_minimo(calificaciones)
aprobados = contar_aprobados(calificaciones)
reprobados = contar_reprobados(calificaciones)
print("\n--- RESULTADOS ---")
print("Promedio:", round(prom, 2))
print("Mayor:", maximo)
print("Menor:", minimo)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)