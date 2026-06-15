import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar

def abrir_registro():

    ventana = tk.Toplevel()

    ventana.title("Registro")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Nombre").pack()

    txt_nombre = tk.Entry(ventana)
    txt_nombre.pack()

    tk.Label(ventana, text="Correo").pack()

    txt_correo = tk.Entry(ventana)
    txt_correo.pack()

    tk.Label(ventana, text="Contraseña").pack()

    txt_password = tk.Entry(ventana, show="*")
    txt_password.pack()

    combo = ttk.Combobox(
        ventana,
        values=["Administrador", "Empleado", "Cliente"]
    )

    combo.pack()
    combo.current(0)

    def guardar():

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id_rol FROM roles WHERE nombre_rol=?",
            (combo.get(),)
        )

        id_rol = cursor.fetchone()[0]

        try:

            cursor.execute("""
            INSERT INTO usuarios
            (nombre,correo,password,id_rol)
            VALUES(?,?,?,?)
            """,
            (
                txt_nombre.get(),
                txt_correo.get(),
                txt_password.get(),
                id_rol
            ))

            conexion.commit()

            messagebox.showinfo(
                "Correcto",
                "Usuario registrado"
            )

            ventana.destroy()

        except:

            messagebox.showerror(
                "Error",
                "Correo existente"
            )

        conexion.close()

    tk.Button(
        ventana,
        text="Registrar",
        command=guardar
    ).pack(pady=10)
