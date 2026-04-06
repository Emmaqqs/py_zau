import tkinter as tk
from tkinter import messagebox
def calcular():
    try:
        metros = float(txtMetros.get())
        cm = metros * 100
        pulgadas = cm / 2.54
        pies = pulgadas / 12
        yardas = pies / 3
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, "=== RESUMEN DE CONVERSIONES ===")
        listbox.insert(tk.END, f"Metros: {metros:.2f}")
        listbox.insert(tk.END, f"Centímetros: {cm:.2f}")
        listbox.insert(tk.END, f"Pulgadas: {pulgadas:.2f}")
        listbox.insert(tk.END, f"Pies: {pies:.2f}")
        listbox.insert(tk.END, f"Yardas: {yardas:.2f}")
    except:
        messagebox.showerror("Error", "Ingresa un valor válido")
def limpiar():
    txtMetros.delete(0, tk.END)
    listbox.delete(0, tk.END)
ventana = tk.Tk()
ventana.title("Control de Medidas")
ventana.geometry("400x350")
tk.Label(ventana, text="Ingrese valor en metros").pack(pady=5)
txtMetros = tk.Entry(ventana)
txtMetros.pack()
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=5)
tk.Button(ventana, text="Limpiar", command=limpiar).pack(pady=5)
tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=5)
listbox = tk.Listbox(ventana, width=50, height=10)
listbox.pack(pady=10)
ventana.mainloop()