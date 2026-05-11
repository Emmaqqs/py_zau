from areas import area_rectangulo, area_triangulo, area_circulo, perimetro_rectangulo, perimetro_triangulo, perimetro_circulo
print(" CÁLCULO DE ÁREAS ")
print("1. Rectángulo")
print("2. Perímetro de Rectángulo")
print("3. Triángulo")
print("4. Perímetro de Triángulo")
print("5. Círculo")
print("6. Perímetro de Círculo")
while (opcion:=int(input("\n Calculo de áreas \n (1) Rectangulo \n (2) Perímetro de Rectángulo " \
"\n (3) Triángulo \n (4) Perímetro de Triángulo " \
"\n (5) Círculo \n (6) Perímetro de Círculo \n Opción: "))) != 7:
    if opcion == 1:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", area_rectangulo(b, h))
    elif opcion == 2:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Perímetro:", perimetro_rectangulo(b, h))
    elif opcion == 3:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print("Área:", area_triangulo(b, h))
    elif opcion == 4:
        l1 = float(input("Lado 1: "))
        l2 = float(input("Lado 2: "))
        l3 = float(input("Lado 3: "))
        print("Perímetro:", perimetro_triangulo(l1, l2, l3))
    elif opcion == 5:
        r = float(input("Radio: "))
        print("Área:", area_circulo(r))
    elif opcion == 6:
        r = float(input("Radio: "))
        print("Perímetro:", perimetro_circulo(r))
    else:
        print("Opción no válida")
print("Saliendo del programa...")