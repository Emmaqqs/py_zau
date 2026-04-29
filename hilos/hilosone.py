import threading
def tarea():
    print("Hola desde un hilo")
# Crear hilo
hilo = threading.Thread(target=tarea)
# Iniciar hilo
hilo.start()
# Esperar a que termine
hilo.join()
print("Programa terminado")