import tkinter as tk
from tkinter import ttk, messagebox


def calcular():
    n1 = float(caja1.get())
    n2 = float(caja2.get())
    op = combo.get()
    if op == "Suma":
        r = n1 + n2
    elif op == "Resta":
        r = n1 - n2
    elif op == "Multiplicación":
        r = n1 * n2
    elif op == "División":
        if n2 == 0:
            messagebox.showerror("Error", "No se puede dividir entre 0")
            return
        r = n1 / n2
    messagebox.showinfo("Resultado", f"Resultado: {r}")


ventana = tk.Tk()
ventana.title("Operaciones básicas")
caja1 = tk.Entry(ventana)
caja1.pack()
caja2 = tk.Entry(ventana)
caja2.pack()
combo = ttk.Combobox(
    ventana,
    values=["Suma", "Resta", "Multiplicación", "División"]
)
combo.pack()
combo.current(0)
tk.Button(ventana, text="Calcular", command=calcular).pack()
ventana.mainloop()