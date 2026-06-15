import tkinter as tk
from tkinter import ttk, messagebox
from database import conectar
from datetime import datetime

def abrir_actividades(id_usuario):

    ventana = tk.Toplevel()

    ventana.title("Actividades")
    ventana.geometry("700x450")

    tk.Label(
        ventana,
        text="Actividad"
    ).pack()

    txt = tk.Entry(
        ventana,
        width=50
    )

    txt.pack()

    tabla = ttk.Treeview(
        ventana,
        columns=("ID", "Descripcion", "Fecha"),
        show="headings"
    )

    tabla.heading("ID", text="ID")
    tabla.heading("Descripcion", text="Descripción")
    tabla.heading("Fecha", text="Fecha")

    tabla.pack(fill="both", expand=True)

    def mostrar():

        for fila in tabla.get_children():
            tabla.delete(fila)

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        SELECT
        id_actividad,
        descripcion,
        fecha
        FROM actividades
        WHERE id_usuario=?
        """, (id_usuario,))

        for fila in cursor.fetchall():

            tabla.insert("", tk.END, values=fila)

        conexion.close()

    def guardar():

        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO actividades
        (descripcion,fecha,id_usuario)
        VALUES(?,?,?)
        """,
        (
            txt.get(),
            datetime.now().strftime("%d/%m/%Y"),
            id_usuario
        ))

        conexion.commit()
        conexion.close()

        mostrar()

        txt.delete(0, tk.END)

    tk.Button(
        ventana,
        text="Guardar Actividad",
        command=guardar
    ).pack()

    mostrar()
