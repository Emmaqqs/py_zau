def calcular_promedio(lista):
    return sum(lista) / len(lista)
def obtener_maximo(lista):
    return max(lista)
def obtener_minimo(lista):
    return min(lista)
def contar_aprobados(lista):
    aprobados = 0
    for cal in lista:
        if cal >= 6:
            aprobados += 1
    return aprobados
def contar_reprobados(lista):
    reprobados = 0
    for cal in lista:
        if cal < 6:
            reprobados += 1
    return reprobados