# Ejercicio 1: Ordenar clientes
clientes_e1 = [
    {"nombre": "Ana", "compras": 5},
    {"nombre": "Luis", "compras": 12},
    {"nombre": "Carlos", "compras": 3}
]

# Ordenar de mayor a menor según compras
clientes_ordenados = sorted(clientes_e1, key=lambda x: x["compras"], reverse=True)

# Imprimir el cliente con más compras
top_cliente = clientes_ordenados[0]
print(f"Ejercicio 1: {top_cliente['nombre']} - {top_cliente['compras']} compras")


# Ejercicio 2: Total gastado por cliente
ventas = [
    {"cliente": "Ana", "total": 200},
    {"cliente": "Luis", "total": 150},
    {"cliente": "Ana", "total": 300},
    {"cliente": "Carlos", "total": 100},
    {"cliente": "Luis", "total": 50}
]

totales_por_cliente = {}

print("\n--- Procesando ventas (Ejercicio 2) ---")
for venta in ventas:
    nombre = venta["cliente"]
    monto = venta["total"]
    if nombre in totales_por_cliente:
        totales_por_cliente[nombre] += monto
    else:
        totales_por_cliente[nombre] = monto
    print(f"Venta: {nombre} - ${monto} | Acumulado: {totales_por_cliente[nombre]}")

print(f"\nResultado final Ejercicio 2: {totales_por_cliente}")


# Ejercicio 3: Cliente más valioso
# Usando el resultado del ejercicio 2
cliente_top_nombre = ""
max_gasto = 0

for nombre, total in totales_por_cliente.items():
    if total > max_gasto:
        max_gasto = total
        cliente_top_nombre = nombre

print(f"Ejercicio 3: Cliente top: {cliente_top_nombre} - ${max_gasto}")


# Ejercicio 4: Aplicar descuentos
clientes_e4 = [
    {"nombre": "Ana", "total": 500},
    {"nombre": "Luis", "total": 1200},
    {"nombre": "Carlos", "total": 300}
]

# Generar nueva lista sin modificar la original
clientes_con_descuento = []
print("\n--- Aplicando descuentos (Ejercicio 4) ---")
for cliente in clientes_e4:
    nuevo_total = cliente["total"]
    if nuevo_total > 1000:
        nuevo_total *= 0.90 # Aplicar 10% de descuento
        print(f"Descuento aplicado a {cliente['nombre']}: de {cliente['total']} a {nuevo_total}")
    else:
        print(f"{cliente['nombre']} no califica para descuento (Total: {nuevo_total})")
    
    clientes_con_descuento.append({
        "nombre": cliente["nombre"],
        "total": nuevo_total
    })

print(f"\nResultado final Ejercicio 4: {clientes_con_descuento}")

