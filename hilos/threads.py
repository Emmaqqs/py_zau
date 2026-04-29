import threading
def tarea(nombre):
    print(f"Tarea {nombre} en ejecución")
# Crear varios hilos
h1 = threading.Thread(target=tarea, args=("A",))
h2 = threading.Thread(target=tarea, args=("B",))
# Iniciar
h1.start()
h2.start()
# Esperar
h1.join()
h2.join()