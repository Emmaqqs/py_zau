import tkinter as tk
# Crear ventana
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("400x300")
# Función para calcular todas las operaciones
def calcular():
    num1 = float(caja1.get())
    num2 = float(caja2.get())
    
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
        texto_division = f"División: {division}"
    else:
        texto_division = "División: Error (división por cero)"
        
    resultado_texto = (
        f"Suma: {suma}\n"
        f"Resta: {resta}\n"
        f"Multiplicación: {multiplicacion}\n"
        f"{texto_division}"
    )
    etiqueta_resultado.config(text=resultado_texto)

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese dos números")
etiqueta.pack(pady=10)

# Caja de texto 1
caja1 = tk.Entry(ventana)
caja1.pack()

# Caja de texto 2
caja2 = tk.Entry(ventana)
caja2.pack()

# Botón
boton = tk.Button(ventana, text="Calcular todas", command=calcular)
boton.pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="Resultados:", justify="left")
etiqueta_resultado.pack()
# Ejecutar ventana
ventana.mainloop()