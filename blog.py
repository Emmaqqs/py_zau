import pandas as pd

# Datos basados en los hallazgos mencionados en el análisis previo
# 10 encuestados (vecinos de Chalco/periferia)
data = {
    'ID_Encuestado': range(1, 11),
    'Acceso_Internet_Estable': ['No', 'No', 'Sí', 'No', 'No', 'Sí', 'No', 'No', 'No', 'Sí'],
    'Conoce_Firma_Electronica': ['No', 'No', 'No', 'No', 'Sí', 'No', 'No', 'Sí', 'No', 'No'],
    'Dificultad_Uso_Portal (1-5)': [5, 4, 4, 5, 3, 4, 5, 4, 5, 3],
    'Preferencia_Tramite': ['Físico', 'Físico', 'Físico', 'Físico', 'Físico', 'Físico', 'Físico', 'Físico', 'Físico', 'Físico'],
    'Confianza_en_Sistema (1-5)': [1, 2, 2, 1, 3, 2, 1, 2, 1, 3]
}

df = pd.DataFrame(data)

# Guardar a Excel
file_path = 'Datos_Investigacion_Emma.xlsx'
df.to_excel(file_path, index=False)

print(file_path)