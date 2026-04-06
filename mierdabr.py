import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def calcular_conversiones():
    try:
        # txtMetros es tu entrada de texto
        metros = float(txtMetros.get())
        # Cálculos de conversión
        centimetros = metros * 100
        pulgadas = centimetros / 2.54
        pies = pulgadas / 12
        yardas = pies / 3
        # Limpiar ListBox (lstR) antes de mostrar
        lstR.delete(0, tk.END)
        # Insertar resultados con el formato de la imagen
        lstR.insert(tk.END, f"MEDIDA EN METROS: {metros:.2f}")
        lstR.insert(tk.END, "------------------------------------------")
        lstR.insert(tk.END, f"MEDIDA EN CENTIMETROS: {centimetros:.2f}")
        lstR.insert(tk.END, f"MEDIDA EN PULGADAS: {pulgadas:.2f}")
        lstR.insert(tk.END, f"MEDIDA EN PIES: {pies:.2f}")
        lstR.insert(tk.END, f"MEDIDA EN YARDAS: {yardas:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")

def limpiar():
    txtMetros.delete(0, tk.END)
    lstR.delete(0, tk.END)
# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Control de medidas")
ventana.geometry("450x550")
# --- IMAGEN ---
try:
    img = Image.open("sastre.png")
    img = img.resize((400, 150), Image.Resampling.LANCZOS)
    foto = ImageTk.PhotoImage(img)
    lblImagen = tk.Label(ventana, image=foto)
    lblImagen.pack(pady=10)
except Exception:
    tk.Label(ventana, text="[ Imagen no encontrada ]").pack()
tk.Label(ventana, text="CONTROL DE MEDIDAS", font=("Arial", 12, "bold")).pack()
# --- ENTRADA Y BOTÓN CALCULAR ---
frame1 = tk.Frame(ventana)
frame1.pack(pady=10)
tk.Label(frame1, text="INGRESE VALOR EN METROS: ").pack(side=tk.LEFT)
txtMetros = tk.Entry(frame1) # Este es tu txtMetros
txtMetros.pack(side=tk.LEFT, padx=5)
btnCalcular = tk.Button(frame1, text="CALCULAR", command=calcular_conversiones)
btnCalcular.pack(side=tk.LEFT)
# --- LISTBOX (lstR) ---
tk.Label(ventana, text="** RESUMEN DE CONVERSIONES **").pack()
lstR = tk.Listbox(ventana, width=50, height=8, font=("Courier New", 10))
lstR.pack(pady=10)
# --- BOTONES INFERIORES ---
frame2 = tk.Frame(ventana)
frame2.pack(pady=10)
btnLimpiar = tk.Button(frame2, text="LIMPIAR", command=limpiar)
btnLimpiar.pack(side=tk.LEFT, padx=10)
btnSalir = tk.Button(frame2, text="SALIR", command=ventana.destroy)
btnSalir.pack(side=tk.LEFT, padx=10)
ventana.mainloop()