import threading  # Módulo para trabajar con threads
import time      # Módulo para usar time.sleep()

# ============================================
# EJEMPLO 1: THREAD SIMPLE CON COMENTARIOS
# ============================================

# Definir una función que será ejecutada por el thread
def tarea_simple(nombre, segundos):
    """
    Esta función simula una tarea que toma tiempo.
    
    Parámetros:
    - nombre: el nombre de la tarea (para identificarla)
    - segundos: cuántos segundos durará la tarea
    """
    # Mostrar que la tarea comenzó
    print(f"[INICIO] Tarea '{nombre}' comenzó")
    
    # Esperar N segundos (simula que está haciendo algo)
    time.sleep(segundos)
    
    # Mostrar que la tarea terminó
    print(f"[FIN] Tarea '{nombre}' terminó después de {segundos} segundos")


print("=" * 50)
print("EJEMPLO 1: Ejecutar tareas en paralelo")
print("=" * 50)

# Crear dos threads
# Thread 1: ejecutará tarea_simple con nombre="Descargar" y segundos=2
thread1 = threading.Thread(target=tarea_simple, args=("Descargar", 2))

# Thread 2: ejecutará tarea_simple con nombre="Procesar" y segundos=3
thread2 = threading.Thread(target=tarea_simple, args=("Procesar", 3))

# IMPORTANTE: En este momento los threads AÚN NO ESTÁN EJECUTÁNDOSE
print("Threads creados, pero aún no inician...")
print()

# Iniciar los threads (ahora sí comienzan a ejecutarse)
print("Iniciando threads...")
thread1.start()
thread2.start()

# Esto se ejecuta mientras los threads trabajan (EN PARALELO)
print("Los threads están ejecutándose mientras yo imprimo esto")
print()

# Esperar a que los threads terminen antes de continuar
# join() pausa la ejecución hasta que el thread finalice
print("Esperando a que terminen los threads...")
thread1.join()  # Espera a que termine thread1
thread2.join()  # Espera a que termine thread2

print("¡Los threads terminaron!")
print()


# ============================================
# EJEMPLO 2: MÚLTIPLES THREADS EN UN BUCLE
# ============================================

def descargar_archivo(numero):
    """
    Simula descargar un archivo.
    
    Parámetros:
    - numero: identificador del archivo a descargar
    """
    # Cada descarga toma entre 1 y 2 segundos
    tiempo = 1 + (numero * 0.3)
    
    print(f"  Descargando archivo #{numero}...")
    time.sleep(tiempo)  # Esperar a que "termine" la descarga
    print(f"  ✓ Archivo #{numero} descargado en {tiempo:.1f}s")


print("=" * 50)
print("EJEMPLO 2: Descargar múltiples archivos")
print("=" * 50)

# Lista para guardar los threads que vamos a crear
lista_threads = []

# Crear 5 threads, uno para cada archivo
print("Creando 5 threads para descargar 5 archivos...\n")
for i in range(5):
    # Crear un thread que descargará el archivo i
    t = threading.Thread(target=descargar_archivo, args=(i,))
    
    # Agregar el thread a la lista
    lista_threads.append(t)
    
    # Iniciar el thread
    t.start()

# En este punto, todos los threads están ejecutándose EN PARALELO
print("Todos los threads se iniciaron. Esperando que terminen...\n")

# Esperar a que terminen TODOS los threads
for t in lista_threads:
    t.join()

print("\n¡Todas las descargas completadas!")
print()


# ============================================
# EJEMPLO 3: CONTEO COMPARTIDO ENTRE THREADS
# ============================================

# Esta es una variable compartida entre threads
contador_global = 0

# Esta es una variable que protege cambios a contador_global
# Sin esto, habría problemas si dos threads quieren cambiar contador_global al mismo tiempo
lock = threading.Lock()


def contar_hasta(numero):
    """
    Incrementa el contador global 'numero' veces.
    
    Usa 'lock' para evitar que dos threads cambien el contador simultáneamente.
    
    Parámetros:
    - numero: cuántas veces incrementar el contador
    """
    global contador_global  # Indica que usamos la variable global
    
    for i in range(numero):
        # Adquirir el lock (bloquea a otros threads)
        lock.acquire()
        
        try:
            # Solo este thread puede cambiar contador_global ahora
            contador_global = contador_global + 1
        
        finally:
            # Liberar el lock (permite que otros threads accedan)
            lock.release()


print("=" * 50)
print("EJEMPLO 3: Contador compartido (thread-safe)")
print("=" * 50)

contador_global = 0  # Reiniciar el contador

# Crear 3 threads, cada uno incrementará el contador 10 veces
print("Creando 3 threads para incrementar un contador...\n")

threads_contadores = []
for i in range(3):
    # Cada thread incrementará 10 veces
    t = threading.Thread(target=contar_hasta, args=(10,))
    threads_contadores.append(t)
    t.start()

# Esperar a que todos terminen
for t in threads_contadores:
    t.join()

# El resultado debe ser 3 × 10 = 30
print(f"Contador final: {contador_global} (esperado: 30)")
print()


# ============================================
# EJEMPLO 4: THREAD CON NOMBRE
# ============================================

def tarea_con_nombre():
    """
    Esta función muestra el nombre del thread que la ejecuta.
    """
    # Obtener el nombre del thread actual
    nombre_thread = threading.current_thread().name
    
    print(f"Ejecutando en: {nombre_thread}")
    time.sleep(1)
    print(f"{nombre_thread} terminó")


print("=" * 50)
print("EJEMPLO 4: Usar nombres en threads")
print("=" * 50)
print()

# Crear threads con nombres personalizados
thread_a = threading.Thread(target=tarea_con_nombre, name="TareaA")
thread_b = threading.Thread(target=tarea_con_nombre, name="TareaB")

# Iniciar
thread_a.start()
thread_b.start()

# Esperar
thread_a.join()
thread_b.join()

print("\n¡Ejemplo completado!")
