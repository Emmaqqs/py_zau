# ============ CHEAT SHEET SISTEMAS - EXAMEN ============
# Copia y pega que funciona todo

# 1. OPERACIONES ARITMÉTICAS
print("=== OPERACIONES ARITMÉTICAS ===")
a, b = 10, 3
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b}")
print(f"División entera: {a // b}")
print(f"Módulo (residuo): {a % b}")
print(f"Potencia: {a ** b}")

import math
print(f"Raíz cuadrada de 16: {math.sqrt(16)}")
print(f"Potencia (math): {math.pow(2, 3)}")
print(f"Redondear arriba (ceil): {math.ceil(3.2)}")
print(f"Redondear abajo (floor): {math.floor(3.9)}")
print(f"Pi: {math.pi:.4f}")
print()

# 2. TIPOS DE DATOS
print("=== TIPOS DE DATOS ===")
entero = 42
decimal = 3.14
texto = "Hola"
booleano = True
lista = [1, 2, 3]
diccionario = {"nombre": "Emma"}

print(f"type(42) = {type(entero).__name__}")
print(f"type(3.14) = {type(decimal).__name__}")
print(f"type('Hola') = {type(texto).__name__}")
print(f"type(True) = {type(booleano).__name__}")
print(f"type([1,2,3]) = {type(lista).__name__}")
print()

# 3. CONVERSIONES (CASTING)
print("=== CASTING (Conversiones) ===")
num_texto = "123"
num_int = int(num_texto)  # "123" → 123
num_float = float(num_texto)  # "123" → 123.0
num_str = str(123)  # 123 → "123"
booleano_num = bool(1)  # 1 → True

print(f"int('123') = {num_int} tipo: {type(num_int).__name__}")
print(f"float('123') = {num_float} tipo: {type(num_float).__name__}")
print(f"str(123) = '{num_str}' tipo: {type(num_str).__name__}")
print(f"bool(1) = {booleano_num}")
print()

# 4. STRINGS
print("=== STRINGS ===")
texto = "Hola Emma"
print(f"Original: '{texto}'")
print(f"Mayúsculas: {texto.upper()}")
print(f"Minúsculas: {texto.lower()}")
print(f"Largo: {len(texto)}")
print(f"Primera letra [0]: {texto[0]}")
print(f"Última letra [-1]: {texto[-1]}")
print(f"Primeras 4 [0:4]: {texto[0:4]}")
print(f"Contiene 'Emma': {'Emma' in texto}")
print(f"Reemplazar: {texto.replace('Emma', 'Carlos')}")
print(f"Dividir: {texto.split()}")
print()

# 5. LISTAS
print("=== LISTAS ===")
numeros = [1, 2, 3, 4, 5]
print(f"Lista: {numeros}")
print(f"Primer elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")
print(f"Tamaño: {len(numeros)}")
print(f"Suma: {sum(numeros)}")
print(f"Máximo: {max(numeros)}")
print(f"Mínimo: {min(numeros)}")
print(f"¿3 está en lista?: {3 in numeros}")

# Métodos de listas
numeros.append(6)  # Agregar
print(f"Después de append(6): {numeros}")
numeros.remove(3)  # Eliminar
print(f"Después de remove(3): {numeros}")
numeros_copia = numeros.copy()
numeros_copia.pop()  # Elimina último
print(f"Después de pop(): {numeros_copia}")
print()

# 6. DICCIONARIOS
print("=== DICCIONARIOS ===")
estudiante = {
    "nombre": "Emma",
    "edad": 20,
    "carrera": "Sistemas",
    "calificacion": 9.5
}
print(f"Diccionario: {estudiante}")
print(f"Nombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']}")
print(f"Claves: {list(estudiante.keys())}")
print(f"Valores: {list(estudiante.values())}")
print(f"¿Tiene 'nombre'?: {'nombre' in estudiante}")

# Agregar/modificar
estudiante["telefono"] = "123456"
print(f"Después de agregar: {estudiante}")
print()

# 7. COMPRENSIONES DE LISTA
print("=== COMPRENSIONES DE LISTA ===")
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

pares = [x for x in range(1, 21) if x % 2 == 0]
print(f"Pares del 1-20: {pares}")

multiplicados = [x * 2 for x in range(1, 6)]
print(f"Multiplicados por 2: {multiplicados}")
print()

# 8. CONTROL DE FLUJO
print("=== IF / ELIF / ELSE ===")
edad = 20
if edad < 13:
    resultado = "Niño"
elif edad < 18:
    resultado = "Adolescente"
elif edad < 65:
    resultado = "Adulto"
else:
    resultado = "Adulto Mayor"
print(f"Edad {edad}: {resultado}")

# Con operadores lógicos
numero = 15
if numero > 10 and numero < 20:
    print(f"{numero} está entre 10 y 20")
print()

# 9. BUCLES
print("=== BUCLES ===")
# FOR
print("Tabla del 5:")
for i in range(1, 6):
    print(f"5 x {i} = {5*i}")

# WHILE
print("\nContador (while):")
contador = 0
while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

# BREAK Y CONTINUE
print("\nCon break y continue:")
for i in range(10):
    if i == 2:
        continue  # Salta
    if i == 7:
        break  # Sale del bucle
    print(i, end=" ")
print()
print()

# 10. FUNCIONES
print("=== FUNCIONES ===")

def saludar(nombre):
    """Función que saluda"""
    return f"Hola, {nombre}!"

def es_par(numero):
    return numero % 2 == 0

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_variable(*numeros):
    """Suma cualquier cantidad de números"""
    return sum(numeros)

print(saludar("Emma"))
print(f"¿4 es par?: {es_par(4)}")
print(f"¿7 es primo?: {es_primo(7)}")
print(f"Suma (2,3,4,5): {suma_variable(2, 3, 4, 5)}")
print()

# 11. EXCEPCIONES
print("=== EXCEPCIONES (TRY/EXCEPT) ===")

def dividir_seguro(a, b):
    try:
        resultado = a / b
        return f"{a} / {b} = {resultado}"
    except ZeroDivisionError:
        return "ERROR: No puedes dividir por cero"
    except TypeError:
        return "ERROR: Tipos incorrectos"
    finally:
        print("  (Esto siempre se ejecuta)")

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))
print()

# 12. LECTURA Y ESCRITURA DE ARCHIVOS (Referencia)
print("=== ARCHIVOS (Referencia Teórica) ===")
print("""MÉTODOS PARA ARCHIVOS:
- open(ruta, 'r') : Leer
- open(ruta, 'w') : Escribir (sobrescribe)
- open(ruta, 'a') : Añadir al final
- archivo.read() : Lee todo
- archivo.readlines() : Lee líneas como lista
- archivo.write(texto) : Escribe texto

MEJOR PRÁCTICA:
with open(ruta, 'r', encoding='utf-8') as f:
    contenido = f.read()

MANEJO DE RUTAS:
import os
os.path.exists(ruta) : ¿Existe?
os.path.getsize(ruta) : Tamaño
os.remove(ruta) : Elimina
os.listdir(carpeta) : Lista carpeta
""")
print()

# 13. DICCIONARIOS AVANZADO
print("=== DICCIONARIOS ANIDADOS ===")
escuela = {
    "estudiantes": [
        {"nombre": "Emma", "nota": 9.5},
        {"nombre": "Carlos", "nota": 8.7},
        {"nombre": "Ana", "nota": 9.2}
    ],
    "profesor": {
        "nombre": "Dr. García",
        "asignatura": "Sistemas"
    }
}

print(f"Primer estudiante: {escuela['estudiantes'][0]['nombre']}")
print(f"Profesor: {escuela['profesor']['nombre']}")
print()

# 14. TUPLAS (Inmutables)
print("=== TUPLAS ===")
coordenadas = (10, 20)
colores = ("rojo", "verde", "azul")
print(f"Tupla: {coordenadas}")
print(f"Primer elemento: {coordenadas[0]}")
print(f"Largo: {len(coordenadas)}")
print(f"¿10 está?: {10 in coordenadas}")
# coordenadas[0] = 5  # ERROR: Las tuplas no se pueden modificar
print()

# 15. CONJUNTOS (Sets - sin duplicados)
print("=== CONJUNTOS (SETS) ===")
numeros_set = {1, 2, 3, 3, 4, 4, 5}  # Los duplicados se eliminan
print(f"Set: {numeros_set}")
print(f"Largo: {len(numeros_set)}")

numeros_set.add(6)
print(f"Después de add(6): {numeros_set}")
numeros_set.remove(3)
print(f"Después de remove(3): {numeros_set}")
print()

# 16. LAMBDA (Funciones anónimas)
print("=== LAMBDA ===")
cuadrado = lambda x: x ** 2
print(f"Cuadrado de 5: {cuadrado(5)}")

# Con map
numeros = [1, 2, 3, 4, 5]
cuadrados_lambda = list(map(lambda x: x**2, numeros))
print(f"Cuadrados con map: {cuadrados_lambda}")

# Con filter
pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares con filter: {pares_lambda}")
print()

print("\\n✅ FIN DEL CHEAT SHEET")
