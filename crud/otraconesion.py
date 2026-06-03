import tkinter as tk
import pymongo

def agregar_empleado():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    puesto = entrada_puesto.get()
    
    # Establece la conexión con MongoDB
    cliente = pymongo.MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")
    db = cliente["empresa"]
    coleccion = db["empleados"]
    
    # Inserta el empleado en la base de datos
    coleccion.insert_one({"nombre": nombre, "edad": int(edad), "puesto": puesto})
    
    # Muestra un mensaje en la interfaz gráfica
    etiqueta_resultado.config(text="Empleado agregado!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agregar Empleado")

# Agrega etiquetas y campos de entrada
tk.Label(ventana, text="Nombre:").pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

tk.Label(ventana, text="Puesto:").pack()
entrada_puesto = tk.Entry(ventana)
entrada_puesto.pack()

# Agrega el botón que ejecuta la función
boton = tk.Button(ventana, text="Agregar", command=agregar_empleado)
boton.pack()

# Etiqueta para mostrar los mensajes de confirmación
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Inicia el bucle principal de Tkinter
ventana.mainloop()