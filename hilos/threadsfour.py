import threading
import time
# Función que simula una descarga
def descargar(nombre, tiempo):
    print(f"Iniciando descarga de {nombre}...")
    time.sleep(tiempo)
    print(f"Descarga completa: {nombre}")
# Crear hilos (tareas concurrentes)
hilo1 = threading.Thread(target=descargar, args=("Archivo 1", 3))
hilo2 = threading.Thread(target=descargar, args=("Archivo 2", 5))
hilo3 = threading.Thread(target=descargar, args=("Archivo 3", 2))
# Iniciar hilos
hilo1.start()
hilo2.start()
hilo3.start()
# Esperar a que todos terminen
hilo1.join()
hilo2.join()
hilo3.join()
print("Todas las descargas han finalizado.")