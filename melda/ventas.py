def calcular_total(precio, cantidad):
    return precio * cantidad
def calcular_descuento(total):
    if total >= 1000:
        return total * 0.20
    elif total >= 500:
        return total * 0.10
    else:
        return 0
def calcular_total_final(total, descuento):
    return total - descuento