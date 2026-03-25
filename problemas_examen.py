# ============ PROBLEMAS TIPO EXAMEN ============
# Ejercicios comunes que pueden preguntar

print("=" * 50)
print("PROBLEMAS TIPO EXAMEN DE SISTEMAS")
print("=" * 50)

# PROBLEMA 1: Calcular promedio
print("\n1. PROMEDIO DE CALIFICACIONES")
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

notas = [8.5, 9.0, 8.8, 9.5, 9.2]
promedio = calcular_promedio(notas)
print(f"Notas: {notas}")
print(f"Promedio: {promedio:.2f}")
if promedio >= 9:
    print("Resultado: EXCELENTE ✓")
elif promedio >= 8:
    print("Resultado: BUENO ✓")
else:
    print("Resultado: REGULAR")

# PROBLEMA 2: Decidir aprobado/desaprobado
print("\n2. APROBAR O DESAPROBAR")
def estado_estudiante(nota, minimo=7.0):
    if nota >= minimo:
        return "APROBADO"
    else:
        return "DESAPROBADO"

notas_estudiantes = {
    "Emma": 9.5,
    "Carlos": 6.8,
    "Ana": 7.0,
    "Luis": 5.5,
    "María": 8.2
}

for nombre, nota in notas_estudiantes.items():
    estado = estado_estudiante(nota)
    print(f"{nombre}: {nota} → {estado}")

# PROBLEMA 3: Contar pares e impares
print("\n3. CONTAR PARES E IMPARES")
def contar_pares_impares(numeros):
    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 != 0)
    return pares, impares

numeros = list(range(1, 11))  # [1, 2, 3, ..., 10]
pares, impares = contar_pares_impares(numeros)
print(f"Números: {numeros}")
print(f"Pares: {pares}")
print(f"Impares: {impares}")

# PROBLEMA 4: Validar contraseña
print("\n4. VALIDAR CONTRASEÑA")
def validar_contraseña(password):
    requisitos = {
        "largo": len(password) >= 8,
        "mayusc": any(c.isupper() for c in password),
        "minusc": any(c.islower() for c in password),
        "numeros": any(c.isdigit() for c in password),
        "caracteres_especiales": any(c in "!@#$%^&*" for c in password)
    }
    
    valida = all(requisitos.values())
    return valida, requisitos

contraseñas = ["hola", "Hola1234", "Hola1234!", "Pass@123"]
for pwd in contraseñas:
    valida, req = validar_contraseña(pwd)
    print(f"\nContraseña: {pwd}")
    print(f"  Válida: {valida}")
    print(f"  Requisitos: {req}")

# PROBLEMA 5: Búsqueda lineal
print("\n5. BÚSQUEDA EN LISTA")
def buscar_elemento(lista, elemento):
    for i, valor in enumerate(lista):
        if valor == elemento:
            return i
    return -1

numeros = [10, 20, 30, 40, 50]
print(f"Lista: {numeros}")
pos = buscar_elemento(numeros, 30)
print(f"Posición de 30: {pos if pos != -1 else 'No encontrado'}")

pos = buscar_elemento(numeros, 100)
print(f"Posición de 100: {pos if pos != -1 else 'No encontrado'}")

# PROBLEMA 6: Tabla de multiplicar
print("\n6. TABLA DE MULTIPLICAR")
def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

print("Tabla del 7:")
tabla_multiplicar(7)

# PROBLEMA 7: Números primos
print("\n7. NÚMEROS PRIMOS")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def listar_primos(hasta):
    return [n for n in range(2, hasta + 1) if es_primo(n)]

primos = listar_primos(30)
print(f"Números primos hasta 30: {primos}")

# PROBLEMA 8: Ordenar lista (Burbuja)
print("\n8. ORDENAMIENTO (MÉTODO BURBUJA)")
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [64, 34, 25, 12, 22, 11, 90]
print(f"Original: {numeros}")
ordenados = ordenar_burbuja(numeros.copy())
print(f"Ordenado: {ordenados}")

# PROBLEMA 9: Invertir palabra
print("\n9. INVERTIR PALABRAS")
def invertir_palabra(palabra):
    return palabra[::-1]

palabra = "sistemas"
invertida = invertir_palabra(palabra)
print(f"Original: {palabra}")
print(f"Invertida: {invertida}")

# PROBLEMA 10: Contar repetidos
print("\n10. CONTAR ELEMENTOS REPETIDOS")
def contar_elementos(lista):
    contador = {}
    for elemento in lista:
        if elemento in contador:
            contador[elemento] += 1
        else:
            contador[elemento] = 1
    return contador

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frecuencia = contar_elementos(numeros)
print(f"Lista: {numeros}")
print(f"Frecuencia: {frecuencia}")

# PROBLEMA 11: Suma de dígitos
print("\n11. SUMA DE DÍGITOS")
def suma_digitos(numero):
    return sum(int(d) for d in str(numero))

num = 12345
suma = suma_digitos(num)
print(f"Número: {num}")
print(f"Suma de dígitos: {suma}")

# PROBLEMA 12: Fibonacci
print("\n12. SERIE FIBONACCI")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    serie = [0, 1]
    for i in range(2, n):
        serie.append(serie[i-1] + serie[i-2])
    return serie

fib = fibonacci(10)
print(f"Fibonacci (primeros 10): {fib}")

# PROBLEMA 13: Procesar lista de datos
print("\n13. PROCESAR LISTA DE DATOS")
def procesar_datos(datos):
    resultado = {
        "cantidad": len(datos),
        "primero": datos[0],
        "ultimo": datos[-1],
        "alfabético": sorted(datos),
        "mayúsculas": [d.upper() for d in datos]
    }
    return resultado

datos = ["Emma", "Carlos", "Ana", "Luis", "María"]
procesado = procesar_datos(datos)
print(f"Datos originales: {datos}")
print(f"Cantidad: {procesado['cantidad']}")
print(f"Primer elemento: {procesado['primero']}")
print(f"Último elemento: {procesado['ultimo']}")
print(f"Ordenado alfabéticamente: {procesado['alfabético']}")
print(f"En mayúsculas: {procesado['mayúsculas']}")

# PROBLEMA 14: Conversión de temperaturas
print("\n14. CONVERSIÓN DE TEMPERATURAS")
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.2f}°F")

temp_f = 77
temp_c = fahrenheit_a_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.2f}°C")

# PROBLEMA 15: Validar email básico
print("\n15. VALIDAR EMAIL")
def validar_email(email):
    return '@' in email and '.' in email

emails = ["emma@gmail.com", "carlos.sistemas", "ana@hotmail.es", "usuario"]
print("Validación de emails:")
for email in emails:
    valido = validar_email(email)
    print(f"  {email}: {'✓ Válido' if valido else '✗ Inválido'}")

# PROBLEMA 16: Cifrado simple (ROT13)
print("\n16. CIFRADO SIMPLE")
def cifrar_rot13(texto):
    resultado = []
    for char in texto:
        if char.isalpha():
            if char.isupper():
                resultado.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                resultado.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        else:
            resultado.append(char)
    return ''.join(resultado)

mensaje = "Hola Emma"
cifrado = cifrar_rot13(mensaje)
print(f"Original: {mensaje}")
print(f"Cifrado: {cifrado}")
print(f"Descifrado: {cifrar_rot13(cifrado)}")

# PROBLEMA 17: Estadísticas
print("\n17. ESTADÍSTICAS (Media, Mediana, Moda)")
def estadisticas(numeros):
    media = sum(numeros) / len(numeros)
    
    ordenados = sorted(numeros)
    n = len(ordenados)
    if n % 2 == 0:
        mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    else:
        mediana = ordenados[n//2]
    
    # Moda simple (el que aparece más)
    frecuencia = {}
    for num in numeros:
        frecuencia[num] = frecuencia.get(num, 0) + 1
    moda = max(frecuencia, key=frecuencia.get)
    
    return media, mediana, moda

datos = [2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 9]
media, mediana, moda = estadisticas(datos)
print(f"Datos: {datos}")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")

print("\n" + "=" * 50)
print("✅ FIN DE PROBLEMAS TIPO EXAMEN")
print("=" * 50)
