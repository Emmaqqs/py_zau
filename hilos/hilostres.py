import threading
import time
# Tarea 1
def contar_numeros():
    for i in range(1, 7):
        print(f"Número: {i}")
        time.sleep(1)
# Tarea 2
def contar_letras():
    for letra in ["A", "B", "C", "D", "E"]:
        print(f"Letra: {letra}")
        time.sleep(1)
# Crear hilos
hilo1 = threading.Thread(target=contar_numeros)
hilo2 = threading.Thread(target=contar_letras)
# Iniciar hilos
hilo1.start()
hilo2.start()
# Esperar a que terminen
hilo1.join()
hilo2.join()
print("Programa terminado")