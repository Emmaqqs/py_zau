import tkinter as tk
from tkinter import messagebox
from database import conectar
from ventanas.actividades import abrir_actividades

def abrir_login():

    ventana = tk.Toplevel()

    ventana.title("Login")
    ventana.geometry("350x250")

    tk.Label(
        ventana,
        text="Correo"
    ).pack()

    txt_correo = tk.Entry(ventana)
    txt_correo.pack()

    tk.Label(
        ventana,
        text="Contraseña"
    ).pack()

    txt_password = tk.Entry(
        ventana,
        show="*"
    )

    txt_password.pack()

    def validar():

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT
        id_usuario,
        nombre
        FROM usuarios
        WHERE correo=?
        AND password=?
        """,
        (
            txt_correo.get(),
            txt_password.get()
        ))

        usuario = cursor.fetchone()

        if usuario:

            messagebox.showinfo(
                "Bienvenido",
                usuario[1]
            )

            ventana.destroy()

            abrir_actividades(usuario[0])

        else:

            messagebox.showerror(
                "Error",
                "Datos incorrectos"
            )

        conexion.close()

    tk.Button(
        ventana,
        text="Entrar",
        command=validar
    ).pack(pady=15)
