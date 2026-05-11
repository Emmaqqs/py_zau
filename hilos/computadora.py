#una computadora simula la ejecucion de varios programas de manera concurrente 1. apertura docs del 1 al 15 2.ventanas abiertas en el navegador (5 al 1)3. reproducir una playlist de musica (canciones del 1 al 20 array)
import threading
import time

def abrir_documentos():
    for i in range(1, 16):
        print(f"Abriendo documento {i}")
        time.sleep(0.5)

def abrir_navegador():
    for i in range(5, 0, -1):
        print(f"Abriendo ventana navegador {i}")
        time.sleep(0.7)

def reproducir_musica():
     for i in range(1, 21):
        print(f"Reproduciendo cancion {i}")
        time.sleep(0.6)

hilo1 = threading.Thread(target=abrir_documentos)
hilo2 = threading.Thread(target=abrir_navegador)
hilo3 = threading.Thread(target=reproducir_musica)

print("Simulacion EzauPC\n")
hilo1.start()
hilo2.start()
hilo3.start()

hilo1.join()
hilo2.join()
hilo3.join()
