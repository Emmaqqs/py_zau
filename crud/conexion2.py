import tkinter as tk
from tkinter import ttk
import pymongo

def cargar_datos():
    # Conexión a MongoDB y acceso a la colección
    cliente = pymongo.MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")
    db = cliente["empresa"]
    coleccion = db["empleados"]
    
    # Recupera todos los empleados
    registros = coleccion.find()
    
    # Limpia la tabla antes de actualizar
    for fila in tree.get_children():
        tree.delete(fila)
        
    # Inserta los datos recuperados en la tabla
    for empleado in registros:
        tree.insert("", "end", values=(empleado["_id"], empleado["nombre"], empleado["edad"], empleado["puesto"]))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Empleados en MongoDB")

# Agrega la tabla con sus cuatro columnas
tree = ttk.Treeview(ventana, columns=("ID", "Nombre", "Edad", "Puesto"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Edad", text="Edad")
tree.heading("Puesto", text="Puesto")
tree.pack()

# Añade el botón para ejecutar la función de carga
boton_cargar = tk.Button(ventana, text="Cargar Datos", command=cargar_datos)
boton_cargar.pack()

# Inicia el bucle principal de Tkinter
ventana.mainloop()