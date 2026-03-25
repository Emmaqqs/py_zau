import tkinter as tk
from tkinter import messagebox, ttk
import math

# ============ APLICACIÓN: CALCULADORA DE PROMEDIOS ============

ventana = tk.Tk()
ventana.title("Calculadora de Promedios - Sistema de Notas")
ventana.geometry("600x700")
ventana.config(bg="#2c3e50")

# Variable global para almacenar notas
notas_lista = []

# ============ FUNCIONES ============

def agregar_nota():
    """Agregar una nota a la lista"""
    try:
        nota_texto = entrada_nota.get()
        
        if not nota_texto:
            messagebox.showerror("Error", "¡Ingresa una nota!")
            return
        
        nota = float(nota_texto)
        
        if nota < 0 or nota > 20:
            messagebox.showerror("Error", "¡La nota debe estar entre 0 y 20!")
            return
        
        notas_lista.append(nota)
        entrada_nota.delete(0, tk.END)
        actualizar_lista()
        messagebox.showinfo("Éxito", f"Nota {nota} agregada ✓")
        
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

def eliminar_nota():
    """Eliminar la última nota"""
    if notas_lista:
        nota_eliminada = notas_lista.pop()
        actualizar_lista()
        messagebox.showinfo("Eliminada", f"Nota {nota_eliminada} eliminada")
    else:
        messagebox.showwarning("Vacío", "¡No hay notas para eliminar!")

def limpiar_notas():
    """Limpiar todas las notas"""
    if notas_lista:
        notas_lista.clear()
        actualizar_lista()
        messagebox.showinfo("Limpiado", "Todas las notas eliminadas")
    else:
        messagebox.showwarning("Vacío", "¡No hay notas!")

def calcular_promedio():
    """Calcular promedio y mostrar estadísticas"""
    if not notas_lista:
        messagebox.showwarning("Error", "¡Agrega notas primero!")
        return
    
    promedio = sum(notas_lista) / len(notas_lista)
    mayornota = max(notas_lista)
    menornota = min(notas_lista)
    desviacion = calcular_desviacion_estandar(notas_lista)
    
    # Determinar estado
    if promedio >= 17:
        estado = "EXCELENTE 🌟"
        color = "#27ae60"
    elif promedio >= 14:
        estado = "BUENO ✓"
        color = "#3498db"
    elif promedio >= 11:
        estado = "REGULAR"
        color = "#f39c12"
    else:
        estado = "DESAPROBADO ✗"
        color = "#e74c3c"
    
    # Crear ventana de resultados
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultados")
    ventana_resultado.geometry("400x300")
    ventana_resultado.config(bg="#ecf0f1")
    
    # Frame principal
    frame_resultado = tk.Frame(ventana_resultado, bg="#34495e", padx=20, pady=20)
    frame_resultado.pack(fill="both", expand=True)
    
    # Título
    titulo = tk.Label(frame_resultado, text="ANÁLISIS DE NOTAS", 
                     font=("Arial", 14, "bold"), bg="#34495e", fg="white")
    titulo.pack()
    
    # Promedio
    tk.Label(frame_resultado, text=f"📊 Promedio: {promedio:.2f}", 
            font=("Arial", 12, "bold"), bg="#34495e", fg="#3498db").pack(pady=5)
    
    # Estado
    tk.Label(frame_resultado, text=f"Estado: {estado}", 
            font=("Arial", 12, "bold"), bg="#34495e", fg=color).pack(pady=5)
    
    # Estadísticas
    stats_text = f"""Cantidad de notas: {len(notas_lista)}
Nota máxima: {mayornota}
Nota mínima: {menornota}
Desviación estándar: {desviacion:.2f}
Rango: {mayornota - menornota}
Suma total: {sum(notas_lista):.2f}"""
    
    tk.Label(frame_resultado, text=stats_text, 
            font=("Arial", 10), bg="#34495e", fg="white", justify="left").pack(pady=10)

def calcular_desviacion_estandar(notas):
    """Calcular desviación estándar"""
    if len(notas) < 2:
        return 0
    promedio = sum(notas) / len(notas)
    varianza = sum((n - promedio) ** 2 for n in notas) / len(notas)
    return math.sqrt(varianza)

def actualizar_lista():
    """Actualizar la visualización de notas"""
    lista_notas.delete(0, tk.END)
    for i, nota in enumerate(notas_lista, 1):
        lista_notas.insert(tk.END, f"{i}. Nota: {nota}")
    
    # Actualizar contador
    label_cantidad.config(text=f"Total de notas: {len(notas_lista)}")
    
    # Actualizar promedio en tiempo real
    if notas_lista:
        prom = sum(notas_lista) / len(notas_lista)
        label_promedio.config(text=f"Promedio actual: {prom:.2f}", fg="#3498db")
    else:
        label_promedio.config(text="Promedio actual: ---", fg="#95a5a6")

def editar_nota():
    """Editar una nota existente"""
    seleccion = lista_notas.curselection()
    if not seleccion:
        messagebox.showwarning("Error", "¡Selecciona una nota para editar!")
        return
    
    indice = seleccion[0]
    ventana_editar = tk.Toplevel(ventana)
    ventana_editar.title("Editar Nota")
    ventana_editar.geometry("300x150")
    ventana_editar.config(bg="#ecf0f1")
    
    tk.Label(ventana_editar, text=f"Nota actual: {notas_lista[indice]}", 
            font=("Arial", 10), bg="#ecf0f1").pack(pady=5)
    
    tk.Label(ventana_editar, text="Nueva nota:", bg="#ecf0f1").pack()
    entrada_editar = tk.Entry(ventana_editar, font=("Arial", 12))
    entrada_editar.pack(pady=5)
    entrada_editar.insert(0, str(notas_lista[indice]))
    
    def guardar_edicion():
        try:
            nueva_nota = float(entrada_editar.get())
            if nueva_nota < 0 or nueva_nota > 20:
                messagebox.showerror("Error", "¡La nota debe estar entre 0 y 20!")
                return
            notas_lista[indice] = nueva_nota
            actualizar_lista()
            ventana_editar.destroy()
            messagebox.showinfo("Éxito", "Nota actualizada ✓")
        except ValueError:
            messagebox.showerror("Error", "¡Ingresa un número válido!")
    
    tk.Button(ventana_editar, text="Guardar", command=guardar_edicion, 
             bg="#27ae60", fg="white").pack(pady=5)

# ============ INTERFAZ PRINCIPAL ============

# HEADER
header = tk.Frame(ventana, bg="#34495e", height=60)
header.pack(fill="x")
tk.Label(header, text="📚 CALCULADORA DE PROMEDIOS", 
        font=("Arial", 16, "bold"), bg="#34495e", fg="white").pack(pady=10)

# SECCIÓN DE ENTRADA
frame_entrada = tk.Frame(ventana, bg="#ecf0f1", padx=15, pady=15)
frame_entrada.pack(fill="x", padx=10, pady=10)

tk.Label(frame_entrada, text="Ingresa una nota (0-20):", 
        font=("Arial", 11, "bold"), bg="#ecf0f1").pack()

frame_input = tk.Frame(frame_entrada, bg="#ecf0f1")
frame_input.pack(pady=5)

entrada_nota = tk.Entry(frame_input, font=("Arial", 12), width=15)
entrada_nota.pack(side="left", padx=5)
entrada_nota.focus()

# Binding para Enter
entrada_nota.bind("<Return>", lambda e: agregar_nota())

boton_agregar = tk.Button(frame_input, text="Agregar", command=agregar_nota, 
                         bg="#3498db", fg="white", font=("Arial", 10, "bold"))
boton_agregar.pack(side="left", padx=5)

# SECCIÓN DE BOTONES
frame_botones = tk.Frame(ventana, bg="#2c3e50")
frame_botones.pack(fill="x", padx=10, pady=5)

botones = [
    ("Editar", editar_nota, "#f39c12"),
    ("Eliminar Última", eliminar_nota, "#e74c3c"),
    ("Limpiar Todo", limpiar_notas, "#c0392b"),
]

for texto, comando, color in botones:
    tk.Button(frame_botones, text=texto, command=comando, 
             bg=color, fg="white", font=("Arial", 9, "bold"), width=15).pack(side="left", padx=5)

# SECCIÓN DE INFORMACIÓN
frame_info = tk.Frame(ventana, bg="#ecf0f1", padx=15, pady=10)
frame_info.pack(fill="x", padx=10, pady=5)

label_cantidad = tk.Label(frame_info, text="Total de notas: 0", 
                         font=("Arial", 10), bg="#ecf0f1", fg="#34495e")
label_cantidad.pack()

label_promedio = tk.Label(frame_info, text="Promedio actual: ---", 
                         font=("Arial", 10, "bold"), bg="#ecf0f1", fg="#95a5a6")
label_promedio.pack()

# SECCIÓN DE LISTA
frame_lista = tk.Frame(ventana, bg="#ecf0f1", padx=15, pady=10)
frame_lista.pack(fill="both", expand=True, padx=10, pady=5)

tk.Label(frame_lista, text="Notas ingresadas:", 
        font=("Arial", 10, "bold"), bg="#ecf0f1").pack(anchor="w")

# Listbox con scrollbar
scrollbar = tk.Scrollbar(frame_lista)
scrollbar.pack(side="right", fill="y")

lista_notas = tk.Listbox(frame_lista, font=("Arial", 10), 
                        yscrollcommand=scrollbar.set, height=8)
lista_notas.pack(fill="both", expand=True)
scrollbar.config(command=lista_notas.yview)

# BOTÓN CALCULAR (Grande y destacado)
boton_calcular = tk.Button(ventana, text="🎯 CALCULAR PROMEDIO", 
                           command=calcular_promedio,
                           bg="#27ae60", fg="white", font=("Arial", 14, "bold"),
                           padx=20, pady=10)
boton_calcular.pack(pady=15)

# FOOTER con info teórica
frame_footer = tk.Frame(ventana, bg="#34495e")
frame_footer.pack(fill="x", side="bottom")

info_text = tk.Label(frame_footer, 
                    text="Promedio = Suma de notas ÷ Cantidad | Aprobado: ≥11 | Bueno: ≥14 | Excelente: ≥17",
                    font=("Arial", 8), bg="#34495e", fg="#95a5a6", justify="center")
info_text.pack(pady=5)

ventana.mainloop()
