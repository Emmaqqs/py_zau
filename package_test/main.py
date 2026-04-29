from utilidades.promedio import calcular_promedio
from utilidades.mensajes import mostrar_resultado
c1 = float(input("Calificación 1: "))
c2 = float(input("Calificación 2: "))
c3 = float(input("Calificación 3: "))
promedio = calcular_promedio(c1, c2, c3)
resultado = mostrar_resultado(promedio)
print("Promedio:", promedio)
print("Nivel:", resultado)