from operaciones import calcular_area

# Solicitar datos al usuario
print("=== Calcular Área de un Rectángulo ===")
ancho = float(input("Ingresa el ancho del rectángulo: "))
alto = float(input("Ingresa el alto del rectángulo: "))

# Llamar a la función para calcular el área
area = calcular_area(ancho, alto)

# Mostrar resultado
print(f"\nEl área del rectángulo es: {area} unidades²")
