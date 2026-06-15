import tkinter as tk
import pymongo

def agregar_empleado():
    titulo = entrada_titulo.get()
    autor = entrada_autor.get()
    editorial = entrada_editorial.get()
    isbn = entrada_isbn.get()
    anio = entrada_anio.get()
    precio = entrada_precio.get()
    
    # Establece la conexión con MongoDB
    cliente = pymongo.MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")
    db = cliente["libreria"]
    coleccion = db["libros"]
    
    # Inserta el libro en la base de datos
    coleccion.insert_one({"titulo": titulo, "autor": autor, "editorial": editorial, "isbn": isbn, "anio": int(anio), "precio": float(precio)})
    
    # Muestra un mensaje en la interfaz gráfica
    etiqueta_resultado.config(text="Libro agregado!")
    
    # Limpia los campos
    entrada_titulo.delete(0, tk.END)
    entrada_autor.delete(0, tk.END)
    entrada_editorial.delete(0, tk.END)
    entrada_isbn.delete(0, tk.END)
    entrada_anio.delete(0, tk.END)
    entrada_precio.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agregar Libro")

# Agrega etiquetas y campos de entrada
tk.Label(ventana, text="Titulo:").pack()
entrada_titulo = tk.Entry(ventana)
entrada_titulo.pack()

tk.Label(ventana, text="Autor:").pack()
entrada_autor = tk.Entry(ventana)
entrada_autor.pack()

tk.Label(ventana, text="Editorial:").pack()
entrada_editorial = tk.Entry(ventana)
entrada_editorial.pack()

tk.Label(ventana, text="ISBN:").pack()
entrada_isbn = tk.Entry(ventana)
entrada_isbn.pack()

tk.Label(ventana, text="Año:").pack()
entrada_anio = tk.Entry(ventana)
entrada_anio.pack()

tk.Label(ventana, text="Precio:").pack()
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()

# Agrega el botón que ejecuta la función
boton = tk.Button(ventana, text="Agregar", command=agregar_empleado)
boton.pack()

# Etiqueta para mostrar los mensajes de confirmación
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Inicia el bucle principal de Tkinter
ventana.mainloop()