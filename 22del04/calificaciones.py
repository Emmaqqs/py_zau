def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)
def evaluar_estado(promedio):
    if promedio >= 6:
        return "Aprobado"
    else:
        return "Reprobado"
def clasificar(promedio):
    if promedio >= 9:
        return "Excelente"
    elif promedio >= 8:
        return "Muy bueno"
    elif promedio >= 7:
        return "Bueno"
    elif promedio >= 6:
        return "Suficiente"
    else:
        return "Insuficiente"