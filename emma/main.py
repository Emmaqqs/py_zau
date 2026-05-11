from operaciones import area_rectangulo, area_triangulo, area_circulo
print(" CÁLCULO DE ÁREAS ")
print("1. Rectángulo")
print("2. Triángulo")
print("3. Círculo")
opcion = int(input("Seleccione una opción: "))
if opcion == 1:
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Área:", area_rectangulo(b, h))
elif opcion == 2:
    b = float(input("Base: "))
    h = float(input("Altura: "))
    print("Área:", area_triangulo(b, h))
elif opcion == 3:
    r = float(input("Radio: "))
    print("Área:", area_circulo(r))
else:
    print("Opción no válida")