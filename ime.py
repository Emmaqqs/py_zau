ventas = [
    {"cliente": "Liliana Leyva", "total": 1100},
    {"cliente": "Fabiola De Jesus", "total": 2050},
    {"cliente": "Efrain Montes", "total": 4400},
    {"cliente": "Omar Montes", "total": 2020},
    {"cliente": "Dulce Sanchez", "total": 5000},
    {"cliente": "Brenda Primero", "total": 4080},
    {"cliente": "Graciela Flores", "total": 1900},
    {"cliente": "Nadia Flores", "total": 900},
    {"cliente": "Itzel Salas", "total": 10000},
    {"cliente": "Lupita Luna", "total": 6000},
    {"cliente": "Maria Luna", "total": 2090},
    {"cliente": "Victor Iturbide", "total": 6400},
    {"cliente": "Pamela Ceron", "total": 2800},
    {"cliente": "Judith Quintana", "total": 1700},
    {"cliente": "Ivon Flores", "total": 2380},
    {"cliente": "Paloma Flores", "total": 1230},
    {"cliente": "Estefany Salas", "total": 1700},
    {"cliente": "Alejandra Antonio", "total": 1200},
    {"cliente": "Jesus Encarnación", "total": 3500}
]

totales_por_cliente = {}
clientes_con_descuento = {}

for venta in ventas:
    cliente = venta["cliente"]
    total = venta["total"]
    
    if cliente in totales_por_cliente:
        totales_por_cliente[cliente] += total
    else:
        totales_por_cliente[cliente] = total

for cliente in totales_por_cliente:
    if totales_por_cliente[cliente] > 5000:
        descuento = totales_por_cliente[cliente] * 0.10
        totales_por_cliente[cliente] -= descuento
        clientes_con_descuento[cliente] = totales_por_cliente[cliente]
ordenado = sorted(totales_por_cliente.items(), key=lambda x: x[1], reverse=True)

top3 = ordenado[:3]
print("Top 3 clientes con descuento aplicado:")
for cliente, total in top3:
    print(f"{cliente}: ${total:.2f}")