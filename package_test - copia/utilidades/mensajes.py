def mostrar_resultado(promedio):
    if promedio >= 9:
        return "Excelente"
    elif promedio >= 7:
        return "Bueno"
    elif promedio >= 6:
        return "Suficiente"
    else:
        return "Reprobado"