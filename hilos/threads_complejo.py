import threading
import time
import queue
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# ============== EJEMPLO 1: SINCRONIZACIÓN CON LOCKS ==============
print("=" * 60)
print("EJEMPLO 1: SINCRONIZACIÓN CON LOCKS")
print("=" * 60)

class Contador:
    """Contador thread-safe con Lock"""
    def __init__(self):
        self.valor = 0
        self.lock = threading.Lock()
    
    def incrementar(self):
        """Incrementa de forma segura"""
        with self.lock:  # Adquiere el lock automáticamente
            temp = self.valor
            time.sleep(0.0001)  # Simula procesamiento
            self.valor = temp + 1
    
    def obtener(self):
        with self.lock:
            return self.valor

contador = Contador()

def incrementar_100_veces():
    for _ in range(100):
        contador.incrementar()

# Crear 5 threads
threads = [threading.Thread(target=incrementar_100_veces) for _ in range(5)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Valor final (esperado 500): {contador.obtener()}\n")


# ============== EJEMPLO 2: COMUNICACIÓN CON QUEUE ==============
print("=" * 60)
print("EJEMPLO 2: COMUNICACIÓN CON QUEUE")
print("=" * 60)

def productor(q, id_productor):
    """Produce datos y los pone en la cola"""
    for i in range(3):
        dato = f"Producto-{id_productor}-{i}"
        q.put(dato)
        print(f"[Productor {id_productor}] Envió: {dato}")
        time.sleep(0.5)
    q.put(None)  # Señal de fin

def consumidor(q, id_consumidor):
    """Consume datos de la cola"""
    while True:
        dato = q.get()
        if dato is None:
            print(f"[Consumidor {id_consumidor}] Terminado")
            break
        print(f"[Consumidor {id_consumidor}] Recibió: {dato}")
        time.sleep(0.3)

cola = queue.Queue()

# 2 productores y 2 consumidores
productores = [threading.Thread(target=productor, args=(cola, i)) for i in range(2)]
consumidores = [threading.Thread(target=consumidor, args=(cola, i)) for i in range(2)]

for t in productores + consumidores:
    t.start()
for t in productores + consumidores:
    t.join()

print()


# ============== EJEMPLO 3: THREADPOOLEXECUTOR ==============
print("=" * 60)
print("EJEMPLO 3: THREADPOOLEXECUTOR (Pool de threads)")
print("=" * 60)

def tarea_larga(numero):
    """Simula una tarea que toma tiempo"""
    print(f"[{threading.current_thread().name}] Procesando {numero}")
    time.sleep(1)
    resultado = numero ** 2
    print(f"[{threading.current_thread().name}] {numero}² = {resultado}")
    return resultado

# Pool de máximo 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    # map() ejecuta la función con cada elemento
    resultados = list(executor.map(tarea_larga, range(1, 6)))
    print(f"Resultados: {resultados}\n")


# ============== EJEMPLO 4: THREAD CON EXCEPCIONES ==============
print("=" * 60)
print("EJEMPLO 4: MANEJO DE EXCEPCIONES EN THREADS")
print("=" * 60)

class ThreadConResultado(threading.Thread):
    """Thread que captura el resultado y excepciones"""
    def __init__(self, target, args=()):
        super().__init__()
        self.target = target
        self.args = args
        self.resultado = None
        self.excepcion = None
    
    def run(self):
        try:
            self.resultado = self.target(*self.args)
        except Exception as e:
            self.excepcion = e
            print(f"Error en thread: {e}")

def tarea_con_riesgo(numero):
    if numero < 0:
        raise ValueError("No se aceptan números negativos")
    return numero * 2

# Crear threads con riesgo
t1 = ThreadConResultado(target=tarea_con_riesgo, args=(5,))
t2 = ThreadConResultado(target=tarea_con_riesgo, args=(-3,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Thread 1 - Resultado: {t1.resultado}, Excepción: {t1.excepcion}")
print(f"Thread 2 - Resultado: {t2.resultado}, Excepción: {t2.excepcion}\n")


# ============== EJEMPLO 5: SIMULACIÓN PRODUCER-CONSUMER COMPLEJA ==============
print("=" * 60)
print("EJEMPLO 5: SISTEMA PRODUCTOR-CONSUMIDOR COMPLEJO")
print("=" * 60)

class SistemaProductorConsumidor:
    def __init__(self, capacidad=5):
        self.cola = queue.Queue(maxsize=capacidad)
        self.activo = True
        self.items_procesados = 0
        self.lock = threading.Lock()
    
    def productor(self, id_prod):
        """Produce 5 items"""
        for i in range(5):
            item = f"Item-{id_prod}-{i}"
            self.cola.put(item)
            print(f"[Productor {id_prod}] Produjo: {item} (Cola: {self.cola.qsize()})")
            time.sleep(0.2)
    
    def consumidor(self, id_cons):
        """Consume items"""
        while True:
            try:
                item = self.cola.get(timeout=1)
                print(f"  [Consumidor {id_cons}] Consumió: {item}")
                
                with self.lock:
                    self.items_procesados += 1
                
                time.sleep(0.3)
            except queue.Empty:
                break
    
    def ejecutar(self):
        productores = [
            threading.Thread(target=self.productor, args=(i,)) 
            for i in range(2)
        ]
        consumidores = [
            threading.Thread(target=self.consumidor, args=(i,)) 
            for i in range(2)
        ]
        
        # Iniciar todos
        for t in productores + consumidores:
            t.start()
        
        # Esperar a todos
        for t in productores:
            t.join()
        for t in consumidores:
            t.join()
        
        print(f"\nItems totales procesados: {self.items_procesados}")

sistema = SistemaProductorConsumidor()
sistema.ejecutar()

print("\n" + "=" * 60)
print("FIN DE LOS EJEMPLOS")
print("=" * 60)
