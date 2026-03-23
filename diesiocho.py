import tkinter as tk
from tkinter import messagebox
def registrar():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    messagebox.showinfo("Registro", f"Nombre: {nombre} Edad: {edad}")
ventana = tk.Tk()
ventana.title("Registro")
tk.Label(ventana,text="Nombre").grid(row=0,column=0)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0,column=1)
tk.Label(ventana,text="Edad").grid(row=1,column=0)
entrada_edad = tk.Entry(ventana)
entrada_edad.grid(row=1,column=1)
tk.Button(ventana,text="Registrar",command=registrar).grid(row=2,column=1)
ventana.mainloop()