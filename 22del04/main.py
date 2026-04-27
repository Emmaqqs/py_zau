from calificaciones import calcular_promedio, evaluar_estado, clasificar
calificaciones = []
n = int(input("¿Cuántas calificaciones desea ingresar? "))
for i in range(n):
    cal = float(input(f"Calificación {i+1}: "))
    calificaciones.append(cal)
    promedio = calcular_promedio(calificaciones)
print("\nPromedio:", round(promedio, 2))
print("Estado:", evaluar_estado(promedio))
print("Nivel:", clasificar(promedio))