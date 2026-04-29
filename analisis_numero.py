import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Análisis de Números")
ventana.geometry("500x400")

titulo = tk.Label(ventana, text="Anlisis de Números Enteros", font=("Arial", 16, "bold"))
titulo.pack(pady=20)

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

label_numero = tk.Label(frame_entrada, text="Ingresa un número:", font=("Arial", 12))
label_numero.pack(side=tk.LEFT, padx=10)

entrada_numero = tk.Entry(frame_entrada, font=("Arial", 12), width=15)
entrada_numero.pack(side=tk.LEFT, padx=10)

frame_resultados = tk.Frame(ventana, borderwidth=2, relief=tk.SUNKEN)
frame_resultados.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

label_resultados_titulo = tk.Label(frame_resultados, text="Resultados:", font=("Arial", 12, "bold"))
label_resultados_titulo.pack(pady=10)

label_numero_ingresado = tk.Label(frame_resultados, text="", font=("Arial", 11))
label_numero_ingresado.pack(pady=5)

label_valor_absoluto = tk.Label(frame_resultados, text="", font=("Arial", 11))
label_valor_absoluto.pack(pady=5)
afafdfadfd
label_tipo_numero = tk.Label(frame_resultados, text="", font=("Arial", 11))
label_tipo_numero.pack(pady=5)ffadafda
fddfadfaafd
def analizar_numero():
    try:fdadafdaf
        texto = entrada_numero.get()
        
        if texto == "":
            messagebox.showwarning("Advertencia", "Por favor, ingresa un número")
            return
        
        numero = int(texto)
        
        valor_abs = abs(numero)

        if numero > 0:
            tipo = "Positivo"
            color = "green"
        elif numero < 0:
            tipo = "Negativo"
            color = "red"
        else:
            tipo = "Cero"
            color = "blue"
        
        label_numero_ingresado.config(text=f"Número ingresado: {numero}", fg="black")
        label_valor_absoluto.config(text=f"Valor absoluto: {valor_abs}", fg="black")
        label_tipo_numero.config(text=f"Clasificación: {tipo}", fg=color)
        
    except ValueError:
        messagebox.showerror("Error", "Debes ingresar un número entero válido")
        entrada_numero.delete(0, tk.END)

def limpiar():
    entrada_numero.delete(0, tk.END)
    label_numero_ingresado.config(text="")
    label_valor_absoluto.config(text="")
    label_tipo_numero.config(text="")
    entrada_numero.focus()

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)
ksfdnllnkfsdnsffsnf
boton_analizar = tk.Button(frame_botones, text="Analizar", command=analizar_numero, 
                            font=("Arial", 12), padx=20, pady=10)
boton_analizar.pack(side=tk.LEFT, padx=10)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar, 
                           font=("Arial", 12), padx=20, pady=10)
boton_limpiar.pack(side=tk.LEFT, padx=10)

ventana.mainloop()