import tkinter as tk
from database import crear_bd
from ventanas.registro import abrir_registro
from ventanas.login import abrir_login

crear_bd()

ventana = tk.Tk()

ventana.title(
    "Sistema de Usuarios"
)
ventana.geometry("500x350")
tk.Label(
    ventana,
    text="SISTEMA DE USUARIOS",
    font=("Arial", 18, "bold")
).pack(pady=30)
tk.Button(
    ventana,
    text="Registrarse",
    width=25,
    height=2,
    command=abrir_registro
).pack(pady=10)
tk.Button(
    ventana,
    text="Iniciar Sesión",
    width=25,
    height=2,
    command=abrir_login
).pack(pady=10)
tk.Button(
    ventana,
    text="Salir",
    width=25,
    height=2,
    command=ventana.destroy
).pack(pady=10)
ventana.mainloop()
