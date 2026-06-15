import tkinter as tk
from tkinter import ttk
import pymongo

def cargar_datos():
    # Conexión a MongoDB y acceso a la colección
    cliente = pymongo.MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")
    db = cliente["libreria"]
    coleccion = db["libros"]
    
    # Recupera todos los libros
    registros = coleccion.find()
    
    # Limpia la tabla antes de actualizar
    for fila in tree.get_children():
        tree.delete(fila)
        
    # Inserta los datos recuperados en la tabla
    for libro in registros:
        tree.insert("", "end", values=(libro["_id"], libro["titulo"], libro["autor"], libro["editorial"], libro["isbn"], libro["precio"]))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Libros en MongoDB")

# Agrega la tabla con sus seis columnas
tree = ttk.Treeview(ventana, columns=("ID", "Titulo", "Autor", "Editorial", "ISBN", "Precio"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Titulo", text="Titulo")
tree.heading("Autor", text="Autor")
tree.heading("Editorial", text="Editorial")
tree.heading("ISBN", text="ISBN")
tree.heading("Precio", text="Precio")
tree.pack()

# Añade el botón para ejecutar la función de carga
boton_cargar = tk.Button(ventana, text="Cargar Datos", command=cargar_datos)
boton_cargar.pack()

# Inicia el bucle principal de Tkinter
ventana.mainloop()