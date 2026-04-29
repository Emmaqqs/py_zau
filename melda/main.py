from ventas import calcular_total, calcular_descuento, calcular_total_final
precio = float(input("Precio del producto: "))
cantidad = int(input("Cantidad: "))
total = calcular_total(precio, cantidad)
descuento = calcular_descuento(total)
total_final = calcular_total_final(total, descuento)
print("\nTotal:", total)
print("Descuento:", descuento)
print("Total a pagar:", total_final)