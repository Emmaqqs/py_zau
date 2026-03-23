import tkinter as tk
from tkinter import messagebox
# Crear ventana
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("400x300")
# Función para sumar
def sumar():
    num1 = int(caja1.get())
    num2 = int(caja2.get())
    resultado = num1 + num2
    messagebox.showinfo("Resultado", "La suma es: " +
    str(resultado))
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
boton = tk.Button(ventana, text="Sumar", command=sumar)
boton.pack(pady=10)
# Ejecutar ventana
ventana.mainloop()