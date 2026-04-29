import threading
import time
def descargar1():
    print("Iniciando descarga de Archivo 1...")
    time.sleep(3)
    print("Descarga completa: Archivo 1")
def descargar2():
    print("Iniciando descarga de Archivo 2...")
    time.sleep(5)
    print("Descarga completa: Archivo 2")
def descargar3():
    print("Iniciando descarga de Archivo 3...")
    time.sleep(2)
    print("Descarga completa: Archivo 3")
hilo1 = threading.Thread(target=descargar1)
hilo2 = threading.Thread(target=descargar2)
hilo3 = threading.Thread(target=descargar3)
hilo1.start()
hilo2.start()
hilo3.start()
hilo1.join()
hilo2.join()
hilo3.join()
print("Todas las descargas han finalizado.")