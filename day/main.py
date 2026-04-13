from Operaciones import calcular_area_rectangulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
area = calcular_area_rectangulo(base, altura)
print("El área del rectángulo es:", area)