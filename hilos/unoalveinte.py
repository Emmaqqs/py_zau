import threading
import time
def tarea_A():
    for i in range(1, 21):
        print(f"Número asc: {i}")
        time.sleep(0.8)
def tarea_B():
    for i in range(20, 0, -1):
        print(f"Número desc: {i}")
        time.sleep(0.8)
h1 = threading.Thread(target=tarea_A)
h2 = threading.Thread(target=tarea_B)
h1.start()
h2.start()
h1.join()
h2.join()