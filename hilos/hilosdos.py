import threading
def tarea_A():
    print("Tarea A en ejecución")
def tarea_B():
    print("Tarea B en ejecución")
h1 = threading.Thread(target=tarea_A)
h2 = threading.Thread(target=tarea_B)
h1.start()
h2.start()
h1.join()
h2.join()