import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()
combo = ttk.Combobox(ventana, values=["México",
"USA", "Canadá","Chalco"])
combo.pack()
combo.current(0)
ventana.mainloop()