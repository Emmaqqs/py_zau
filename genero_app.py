import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Aplicación de Género")
ventana.geometry("400x300")

genero = tk.StringVar(value="")

titulo = tk.Label(ventana, text="Selecciona tu género:", font=("Arial", 14, "bold"))
titulo.pack(pady=20)

radio_hombre = tk.Radiobutton(ventana, text="Hombre", variable=genero, value="Hombre", font=("Arial", 12))
radio_hombre.pack(anchor=tk.W, padx=50)

radio_mujer = tk.Radiobutton(ventana, text="Mujer", variable=genero, value="Mujer", font=("Arial", 12))
radio_mujer.pack(anchor=tk.W, padx=50)

label_resultado = tk.Label(ventana, text="", font=("Arial", 12, "bold"), fg="blue")
label_resultado.pack(pady=20)

def mostrar_genero():
    opcion = genero.get()
    if opcion == "":
        messagebox.showwarning("Advertencia", "Por favor, selecciona una opción")
    else:
        label_resultado.config(text=f"Has seleccionado: {opcion}")

boton = tk.Button(ventana, text="Confirmar", command=mostrar_genero, font=("Arial", 12), bg="lightblue", padx=20, pady=10)
boton.pack(pady=20)

ventana.mainloop()
