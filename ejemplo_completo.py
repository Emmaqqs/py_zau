import tkinter as tk
from tkinter import messagebox
import math

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Completo: Sistemas - Acordeón Examen")
ventana.geometry("800x900")
ventana.config(bg="#f0f0f0")

# Crear un Canvas con Scrollbar
canvas = tk.Canvas(ventana, bg="#060606", highlightthickness=0)
scrollbar = tk.Scrollbar(ventana, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Frame dentro del canvas para contener todos los widgets
main_frame = tk.Frame(canvas, bg="#f0f0f0")
canvas_window = canvas.create_window((0, 0), window=main_frame, anchor="nw")

# Actualizar el scroll region cuando cambia el tamaño
def on_frame_configure(event=None):
    canvas.configure(scrollregion=canvas.bbox("all"))

main_frame.bind("<Configure>", on_frame_configure)

# ============ SECCIÓN 1: TIPOS DE DATOS =============
frame_tipos = tk.Frame(main_frame, bg="lightblue", padx=10, pady=10)
frame_tipos.pack(fill="x", padx=5, pady=5)

tk.Label(frame_tipos, text="1. TIPOS DE DATOS", font=("Arial", 12, "bold"), bg="lightblue").pack()

frame_entrada_tipos = tk.Frame(frame_tipos, bg="lightblue")
frame_entrada_tipos.pack()

tk.Label(frame_entrada_tipos, text="Número:", bg="lightblue").pack(side="left")
entrada_numero = tk.Entry(frame_entrada_tipos, width=15)
entrada_numero.pack(side="left", padx=5)

def mostrar_tipos():
    try:
        valor_texto = entrada_numero.get()
        valor_int = int(valor_texto)
        valor_float = float(valor_texto)
        valor_bool = bool(valor_int)
        
        info = f"""Conversiones de tipos:
Texto original: {valor_texto} (str)
Como int: {valor_int} (int)
Como float: {valor_float} (float)
Como bool: {valor_bool} (bool)

Tipo original detectado: {type(valor_texto).__name__}
Tipo como int: {type(valor_int).__name__}
"""
        messagebox.showinfo("Tipos de Datos", info)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

boton_tipos = tk.Button(frame_entrada_tipos, text="Ver tipos", command=mostrar_tipos, bg="yellow")
boton_tipos.pack(side="left", padx=5)

# ============ SECCIÓN 2: OPERACIONES BÁSICAS =============
frame_operaciones = tk.Frame(main_frame, bg="lightgreen", padx=10, pady=10)
frame_operaciones.pack(fill="x", padx=5, pady=5)

tk.Label(frame_operaciones, text="2. OPERACIONES ARITMÉTICAS BÁSICAS", font=("Arial", 12, "bold"), bg="lightgreen").pack()

frame_numeros = tk.Frame(frame_operaciones, bg="lightgreen")
frame_numeros.pack()

tk.Label(frame_numeros, text="Número 1:", bg="lightgreen").pack(side="left", padx=5)
entrada_num1 = tk.Entry(frame_numeros, width=10)
entrada_num1.pack(side="left", padx=2)

tk.Label(frame_numeros, text="Número 2:", bg="lightgreen").pack(side="left", padx=5)
entrada_num2 = tk.Entry(frame_numeros, width=10)
entrada_num2.pack(side="left", padx=2)

def calcular_operaciones():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2 if num2 != 0 else "No se puede dividir por 0"
        division_entera = num1 // num2 if num2 != 0 else "N/A"
        modulo = num1 % num2 if num2 != 0 else "N/A"
        potencia = num1 ** num2 if num2 < 100 else "Número muy grande"
        
        info = f"""Operaciones entre {num1} y {num2}:
        
Suma (+): {suma}
Resta (-): {resta}
Multiplicación (*): {multiplicacion}
División (/): {division}
División Entera (//): {division_entera}
Módulo (%): {modulo}
Potencia (**): {potencia}
"""
        messagebox.showinfo("Operaciones Básicas", info)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa números válidos!")

boton_operaciones = tk.Button(frame_operaciones, text="Calcular", command=calcular_operaciones, bg="lightgreen")
boton_operaciones.pack(pady=5)

# ============ SECCIÓN 3: CON LIBRERÍA MATH =============
frame_math = tk.Frame(main_frame, bg="lightyellow", padx=10, pady=10)
frame_math.pack(fill="x", padx=5, pady=5)

tk.Label(frame_math, text="3. OPERACIONES CON LIBRERÍA MATH", font=("Arial", 12, "bold"), bg="lightyellow").pack()

frame_math_entrada = tk.Frame(frame_math, bg="lightyellow")
frame_math_entrada.pack()

tk.Label(frame_math_entrada, text="Número:", bg="lightyellow").pack(side="left", padx=5)
entrada_math = tk.Entry(frame_math_entrada, width=15)
entrada_math.pack(side="left", padx=5)

def calcular_math():
    try:
        numero = float(entrada_math.get())
        
        if numero < 0:
            messagebox.showerror("Error", "¡Ingresa un número positivo para raíz cuadrada!")
            return
        
        raiz_cuadrada_math = math.sqrt(numero)
        raiz_cuadrada_manual = numero ** 0.5
        potencia_math = math.pow(numero, 2)
        redondear_arriba = math.ceil(numero)
        redondear_abajo = math.floor(numero)
        
        info = f"""Operaciones Math con {numero}:

Raíz cuadrada (math.sqrt): {raiz_cuadrada_math:.4f}
Raíz cuadrada (** 0.5): {raiz_cuadrada_manual:.4f}
Potencia al cuadrado (math.pow): {potencia_math:.4f}
Redondear arriba (math.ceil): {redondear_arriba}
Redondear abajo (math.floor): {redondear_abajo}

Constantes matemáticas:
Pi (math.pi): {math.pi:.6f}
e (math.e): {math.e:.6f}
"""
        messagebox.showinfo("Operaciones Math", info)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

boton_math = tk.Button(frame_math, text="Calcular Math", command=calcular_math, bg="gold")
boton_math.pack(pady=5)

# ============ SECCIÓN 4: EJEMPLO COMBINADO =============
frame_combo = tk.Frame(main_frame, bg="lightcoral", padx=10, pady=10)
frame_combo.pack(fill="x", padx=5, pady=5)

tk.Label(frame_combo, text="4. EJEMPLO COMBINADO", font=("Arial", 12, "bold"), bg="lightcoral").pack()

frame_combo_entrada = tk.Frame(frame_combo, bg="lightcoral")
frame_combo_entrada.pack()

tk.Label(frame_combo_entrada, text="Base:", bg="lightcoral").pack(side="left", padx=5)
entrada_base = tk.Entry(frame_combo_entrada, width=10)
entrada_base.pack(side="left", padx=2)

tk.Label(frame_combo_entrada, text="Exponente:", bg="lightcoral").pack(side="left", padx=5)
entrada_exp = tk.Entry(frame_combo_entrada, width=10)
entrada_exp.pack(side="left", padx=2)

def calcular_combo():
    try:
        base = float(entrada_base.get())
        exp = float(entrada_exp.get())
        
        # Conversiones de tipo
        base_int = int(base)
        exp_int = int(exp)
        
        # Operaciones
        potencia_manual = base ** exp
        potencia_math_lib = math.pow(base, exp)
        raiz = base ** (1/exp) if exp != 0 else "N/A"
        
        info = f"""Cálculos con Base={base} y Exponente={exp}:

CONVERSIONES DE TIPO:
Base como str: "{str(base)}"
Base como int: {base_int}
Exponente como int: {exp_int}

POTENCIAS:
{base} ^ {exp} (manual): {potencia_manual}
{base} ^ {exp} (math.pow): {potencia_math_lib}
Raíz: {raiz}
"""
        messagebox.showinfo("Ejemplo Combinado", info)
    except (ValueError, ZeroDivisionError) as e:
        messagebox.showerror("Error", f"¡Error en el cálculo: {e}!")

boton_combo = tk.Button(frame_combo, text="Calcular Combo", command=calcular_combo, bg="red")
boton_combo.pack(pady=5)

# ============ SECCIÓN 5: ESTRUCTURAS DE CONTROL (IF/ELSE) =============
frame_control = tk.Frame(main_frame, bg="lightsteelblue", padx=10, pady=10)
frame_control.pack(fill="x", padx=5, pady=5)

tk.Label(frame_control, text="5. CONTROL DE FLUJO (IF/ELSE)", font=("Arial", 12, "bold"), bg="lightsteelblue").pack()

frame_edad = tk.Frame(frame_control, bg="lightsteelblue")
frame_edad.pack()

tk.Label(frame_edad, text="Edad:", bg="lightsteelblue").pack(side="left", padx=5)
entrada_edad = tk.Entry(frame_edad, width=10)
entrada_edad.pack(side="left", padx=5)

def verificar_edad():
    try:
        edad = int(entrada_edad.get())
        
        if edad < 0:
            resultado = "ERROR: Edad no puede ser negativa"
        elif edad < 13:
            resultado = f"Tienes {edad} años: MENOR DE EDAD (Niño)"
        elif edad < 18:
            resultado = f"Tienes {edad} años: ADOLESCENTE"
        elif edad < 65:
            resultado = f"Tienes {edad} años: ADULTO"
        else:
            resultado = f"Tienes {edad} años: ADULTO MAYOR"
        
        messagebox.showinfo("Control de Flujo", resultado)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa una edad válida!")

boton_edad = tk.Button(frame_control, text="Verificar Edad", command=verificar_edad, bg="steelblue", fg="white")
boton_edad.pack(pady=5)

# ============ SECCIÓN 6: LISTAS Y DICCIONARIOS =============
frame_colecciones = tk.Frame(main_frame, bg="lavender", padx=10, pady=10)
frame_colecciones.pack(fill="x", padx=5, pady=5)

tk.Label(frame_colecciones, text="6. LISTAS Y DICCIONARIOS", font=("Arial", 12, "bold"), bg="lavender").pack()

def mostrar_colecciones():
    # LISTAS
    numeros = [1, 2, 3, 4, 5]
    nombres = ["Emma", "Carlos", "Ana", "Luis"]
    mixta = [10, "hola", 3.14, True]
    
    # DICCIONARIOS
    estudiante = {
        "nombre": "Emma",
        "edad": 20,
        "carrera": "Sistemas",
        "calificacion": 9.5
    }
    
    calificaciones = {
        "Matemáticas": 8.5,
        "Física": 9.0,
        "Programación": 9.8
    }
    
    # OPERACIONES
    info = f"""LISTAS:
Lista de números: {numeros}
Primer elemento: {numeros[0]}
Último elemento: {numeros[-1]}
Cantidad: {len(numeros)}
Suma: {sum(numeros)}
Máximo: {max(numeros)}
Mínimo: {min(numeros)}

Lista de nombres: {nombres}
¿"Emma" está? {"Emma" in nombres}

Lista mixta (tipos distintos): {mixta}
Tipo del elemento 0: {type(mixta[0]).__name__}
Tipo del elemento 1: {type(mixta[1]).__name__}

DICCIONARIOS:
Estudiante: {estudiante}
Nombre: {estudiante["nombre"]}
Edad: {estudiante["edad"]}
Calificación: {estudiante["calificacion"]}

Calificaciones por materia:
Math: {calificaciones["Matemáticas"]}
Física: {calificaciones["Física"]}
Programación: {calificaciones["Programación"]}
Promedio: {sum(calificaciones.values()) / len(calificaciones):.2f}
"""
    messagebox.showinfo("Listas y Diccionarios", info)

boton_colecciones = tk.Button(frame_colecciones, text="Ver Listas y Dicts", command=mostrar_colecciones, bg="purple", fg="white")
boton_colecciones.pack(pady=5)

# ============ SECCIÓN 7: BUCLES (FOR Y WHILE) =============
frame_bucles = tk.Frame(main_frame, bg="#FFB6C1", padx=10, pady=10)
frame_bucles.pack(fill="x", padx=5, pady=5)

tk.Label(frame_bucles, text="7. BUCLES (FOR Y WHILE)", font=("Arial", 12, "bold"), bg="#FFB6C1").pack()

frame_num_bucles = tk.Frame(frame_bucles, bg="#FFB6C1")
frame_num_bucles.pack()

tk.Label(frame_num_bucles, text="Número:", bg="#FFB6C1").pack(side="left", padx=5)
entrada_bucle = tk.Entry(frame_num_bucles, width=10)
entrada_bucle.pack(side="left", padx=5)

def mostrar_bucles():
    try:
        n = int(entrada_bucle.get())
        
        # BUCLE FOR
        tabla_multiplicar = ""
        for i in range(1, 11):
            tabla_multiplicar += f"{n} x {i} = {n*i}\n"
        
        # BUCLE WHILE
        numero = n
        factorial = 1
        while numero > 0:
            factorial *= numero
            numero -= 1
        
        # LISTA CON COMPRENSIÓN
        cuadrados = [x**2 for x in range(1, 6)]
        numeros_pares = [x for x in range(1, 20) if x % 2 == 0]
        
        info = f"""BUCLE FOR - Tabla del {n}:
{tabla_multiplicar}

BUCLE WHILE - Factorial de {n}:
Resultado: {factorial}

COMPRENSIÓN DE LISTAS:
Cuadrados (1-5): {cuadrados}
Números pares (1-20): {numeros_pares}

RESUMEN:
- FOR: itera sobre secuencias
- WHILE: itera mientras condición sea verdadera
- Comprensión: forma compacta de crear listas
"""
        messagebox.showinfo("Bucles", info)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

boton_bucles = tk.Button(frame_bucles, text="Ver Bucles", command=mostrar_bucles, bg="#FF69B4", fg="white")
boton_bucles.pack(pady=5)

# ============ SECCIÓN 8: STRINGS Y OPERACIONES =============
frame_strings = tk.Frame(main_frame, bg="#FFE4B5", padx=10, pady=10)
frame_strings.pack(fill="x", padx=5, pady=5)

tk.Label(frame_strings, text="8. STRINGS Y OPERACIONES", font=("Arial", 12, "bold"), bg="#FFE4B5").pack()

frame_texto = tk.Frame(frame_strings, bg="#FFE4B5")
frame_texto.pack()

tk.Label(frame_texto, text="Texto:", bg="#FFE4B5").pack(side="left", padx=5)
entrada_texto = tk.Entry(frame_texto, width=20)
entrada_texto.pack(side="left", padx=5)

def operaciones_strings():
    texto = entrada_texto.get()
    
    if not texto:
        messagebox.showerror("Error", "¡Ingresa un texto!")
        return
    
    info = f"""OPERACIONES CON STRINGS:

Texto original: "{texto}"
Largo: {len(texto)} caracteres
Mayúsculas: {texto.upper()}
Minúsculas: {texto.lower()}
Capitalizado: {texto.capitalize()}
Título: {texto.title()}

¿Contiene 'a'?: {'a' in texto.lower()}
Posición de primera letra: {texto[0]}
Última letra: {texto[-1]}
Primeras 3 letras: {texto[:3]}
Últimas 3 letras: {texto[-3:]}

Reemplazar 'a' por '*': {texto.replace('a', '*').replace('A', '*')}
Dividido por espacios: {texto.split()}

FORMATO:
Saludo: Hola, {texto}!
F-string: f"Tu nombre es {{texto}}" = f"Tu nombre es {texto}"
"""
    messagebox.showinfo("Strings", info)

boton_strings = tk.Button(frame_strings, text="Analizar Texto", command=operaciones_strings, bg="orange")
boton_strings.pack(pady=5)

# ============ SECCIÓN 9: FUNCIONES PERSONALIZADAS =============
frame_funciones = tk.Frame(main_frame, bg="#E0FFE0", padx=10, pady=10)
frame_funciones.pack(fill="x", padx=5, pady=5)

tk.Label(frame_funciones, text="9. FUNCIONES PERSONALIZADAS", font=("Arial", 12, "bold"), bg="#E0FFE0").pack()

# Definir funciones antes de usarlas
def es_par(numero):
    return numero % 2 == 0

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def calcular_promedio(*calificaciones):
    return sum(calificaciones) / len(calificaciones) if calificaciones else 0

frame_func_entrada = tk.Frame(frame_funciones, bg="#E0FFE0")
frame_func_entrada.pack()

tk.Label(frame_func_entrada, text="Número:", bg="#E0FFE0").pack(side="left", padx=5)
entrada_func = tk.Entry(frame_func_entrada, width=10)
entrada_func.pack(side="left", padx=5)

def analizar_numero():
    try:
        num = int(entrada_func.get())
        
        par_impar = "PAR" if es_par(num) else "IMPAR"
        primo = "SÍ, es primo" if es_primo(num) else "NO, no es primo"
        promedio_ejemplo = calcular_promedio(8.5, 9.0, 8.8, 9.5)
        
        info = f"""FUNCIONES PERSONALIZADAS:

Número ingresado: {num}
¿Es par? {par_impar}
¿Es primo? {primo}
Divisible por 3: {num % 3 == 0}

FUNCIÓN CON *args (promedio variable):
calcular_promedio(8.5, 9.0, 8.8, 9.5) = {promedio_ejemplo:.2f}

CONCEPTOS:
- def nombre(parámetros): define función
- return: devuelve un valor
- *args: múltiples argumentos
- **kwargs: argumentos con nombre
"""
        messagebox.showinfo("Funciones", info)
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa un número válido!")

boton_funciones = tk.Button(frame_funciones, text="Analizar Número", command=analizar_numero, bg="green", fg="white")
boton_funciones.pack(pady=5)

# ============ SECCIÓN 10: MANEJO DE EXCEPCIONES =============
frame_excepciones = tk.Frame(main_frame, bg="#FFE4E1", padx=10, pady=10)
frame_excepciones.pack(fill="x", padx=5, pady=5)

tk.Label(frame_excepciones, text="10. MANEJO DE EXCEPCIONES (TRY/EXCEPT)", font=("Arial", 12, "bold"), bg="#FFE4E1").pack()

def mostrar_excepciones():
    ejemplos = """TIPOS DE EXCEPCIONES COMUNES:

1. ValueError: Conversión de tipo incorrecta
   int("hola") → ValueError

2. ZeroDivisionError: División por cero
   10 / 0 → ZeroDivisionError

3. IndexError: Índice fuera de rango
   lista[100] cuando lista solo tiene 5 elementos

4. KeyError: Clave no existe en diccionario
   diccionario["clave_inexistente"]

5. TypeError: Tipo incorrecto para operación
   "hola" + 5 → TypeError

ESTRUCTURA TRY/EXCEPT:
try:
    # Código que puede fallar
    resultado = 10 / int(entrada)
except ValueError:
    print("Debes ingresar un número")
except ZeroDivisionError:
    print("No puedes dividir por cero")
except Exception as e:
    print(f"Error desconocido: {e}")
finally:
    print("Esto siempre se ejecuta")
"""
    messagebox.showinfo("Excepciones", ejemplos)

boton_excepciones = tk.Button(frame_excepciones, text="Ver Excepciones", command=mostrar_excepciones, bg="indianred", fg="white")
boton_excepciones.pack(pady=5)

# ============ SECCIÓN 11: ARCHIVO Y FICHEROS =============
frame_archivos = tk.Frame(main_frame, bg="#E0FFFF", padx=10, pady=10)
frame_archivos.pack(fill="x", padx=5, pady=5)

tk.Label(frame_archivos, text="11. LECTURA Y ESCRITURA DE ARCHIVOS", font=("Arial", 12, "bold"), bg="#E0FFFF").pack()

def demostrar_archivos():
    import os
    
    ruta = "c:\\Users\\emma1\\Documents\\py_zau\\archivo_ejemplo.txt"
    
    # ESCRIBIR ARCHIVO
    contenido = """Este es un archivo de ejemplo
Línea 2: Con varias líneas
Línea 3: Para demostrar lectura/escritura
Línea 4: ¡Examen de Sistemas!"""
    
    try:
        # Escribir
        with open(ruta, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido)
        
        # Leer
        with open(ruta, 'r', encoding='utf-8') as archivo:
            contenido_leido = archivo.read()
        
        # Leer línea por línea
        with open(ruta, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        # Información del archivo
        tamaño = os.path.getsize(ruta)
        existe = os.path.exists(ruta)
        
        info = f"""OPERACIONES CON ARCHIVOS:

Ruta: {ruta}
¿Existe? {existe}
Tamaño: {tamaño} bytes

CONTENIDO ESCRITO Y LEÍDO:
{contenido_leido}

LÍNEAS (readlines):
{lineas}

MÉTODOS COMUNES:
- open(ruta, 'r') : Leer
- open(ruta, 'w') : Escribir (sobrescribe)
- open(ruta, 'a') : Añadir al final
- archivo.read() : Lee todo
- archivo.readlines() : Lee líneas como lista
- archivo.write(texto) : Escribe texto
- archivo.close() : Cierra archivo
- with open(): Cierra automáticamente

MANEJO DE RUTAS:
import os
os.path.exists(ruta) : ¿Existe?
os.path.getsize(ruta) : Tamaño
os.remove(ruta) : Elimina
os.listdir(carpeta) : Lista carpeta
"""
        messagebox.showinfo("Archivos", info)
    except Exception as e:
        messagebox.showerror("Error", f"Error al manejar archivos: {e}")

boton_archivos = tk.Button(frame_archivos, text="Ver Archivos", command=demostrar_archivos, bg="teal", fg="white")
boton_archivos.pack(pady=5)

# ============ SECCIÓN 12: RESUMEN RÁPIDO =============
frame_resumen = tk.Frame(main_frame, bg="#FFFACD", padx=10, pady=10)
frame_resumen.pack(fill="x", padx=5, pady=5)

tk.Label(frame_resumen, text="12. RESUMEN - CHECKLIST EXAMEN", font=("Arial", 12, "bold"), bg="#FFFACD").pack()

def mostrar_resumen():
    resumen = """✅ OPERACIONES ARITMÉTICAS:
   - Básicas: +, -, *, /, //, %, **
   - math.sqrt(), math.pow(), math.ceil(), math.floor()

✅ TIPOS DE DATOS:
   - int, float, str, bool, list, dict, tuple, set
   - type(variable), int(), float(), str(), bool()

✅ CONTROL DE FLUJO:
   - if / elif / else
   - Operadores: ==, !=, <, >, <=, >=, and, or, not

✅ BUCLES:
   - for: for i in range(5)
   - while: while condición
   - break, continue
   - Comprensiones: [x for x in lista]

✅ COLECCIONES:
   - Listas: [1, 2, 3], append(), remove(), pop()
   - Diccionarios: {"clave": valor}, keys(), values()
   - Tuplas: (1, 2, 3) (inmutables)

✅ STRINGS:
   - Largo: len(str), upper(), lower()
   - Índices: str[0], str[-1], str[1:3]
   - replace(), split(), join()

✅ FUNCIONES:
   - def nombre(parámetros):
   - return valor
   - *args, **kwargs

✅ EXCEPCIONES:
   - try / except / finally
   - ValueError, ZeroDivisionError, IndexError, KeyError

✅ ARCHIVOS:
   - open(ruta, 'r'/'w'/'a')
   - with open(): lectura/escritura automática
   - read(), readlines(), write()

✅ TKINTER (INTERFAZ GRÁFICA):
   - Tk() : ventana
   - Label, Entry, Button
   - messagebox.showinfo/showerror
   - .pack(), .grid()
"""
    messagebox.showinfo("Resumen Examen", resumen)

boton_resumen = tk.Button(frame_resumen, text="Ver Resumen", command=mostrar_resumen, bg="gold", fg="black", font=("Arial", 10, "bold"))
boton_resumen.pack(pady=5)

# ============ BOTÓN SALIR =============
boton_salir = tk.Button(main_frame, text="Salir", command=ventana.quit, bg="gray", fg="white", font=("Arial", 10, "bold"))
boton_salir.pack(pady=10)

ventana.mainloop()
