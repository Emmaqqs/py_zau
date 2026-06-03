"""
Interfaz gráfica Tkinter para el CRUD de alumnos (MongoDB).

Uso: ejecutar este archivo y utilizar los botones para Crear/Listar/Buscar/Actualizar/Eliminar.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient
from bson import ObjectId
import sys

MONGO_URI = "mongodb://admin:mongopassword@localhost:27017/"


def conectar_mongodb():
    try:
        cliente = MongoClient(MONGO_URI)
        cliente.admin.command('ping')
        db = cliente["tesi"]
        coleccion = db["alumnos"]
        return coleccion
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar a MongoDB:\n{e}")
        sys.exit(1)


class TesiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD TESI - Interfaz")
        self.geometry("1600x400")

        self.coleccion = conectar_mongodb()

        self.tree = ttk.Treeview(self, columns=("id", "nombre", "carrera", "semestre", "promedio", "materias"), show='headings')
        self.tree.heading('id', text='ID')
        self.tree.heading('nombre', text='Nombre')
        self.tree.heading('carrera', text='Carrera')
        self.tree.heading('semestre', text='Semestre')
        self.tree.heading('promedio', text='Promedio')
        self.tree.heading('materias', text='Materias')
        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        btn_frame = tk.Frame(self)
        btn_frame.pack(fill=tk.X, padx=8)

        tk.Button(btn_frame, text="Crear", command=self.crear_dialog).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Actualizar", command=self.actualizar_selected).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Eliminar", command=self.eliminar_selected).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Buscar por ID", command=self.buscar_por_id_dialog).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Refrescar", command=self.cargar_alumnos).pack(side=tk.LEFT, padx=4)
        tk.Button(btn_frame, text="Salir", command=self.quit).pack(side=tk.RIGHT, padx=4)

        self.cargar_alumnos()

    def cargar_alumnos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        try:
            for alumno in self.coleccion.find():
                materias = ', '.join(alumno.get('materias', []))
                self.tree.insert('', tk.END, iid=str(alumno['_id']), values=(str(alumno.get('_id','')), alumno.get('nombre',''), alumno.get('carrera',''), alumno.get('semestre',''), alumno.get('promedio',''), materias))
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer alumnos:\n{e}")

    def crear_dialog(self):
        DialogAlumno(self, self.crear_alumno)

    def crear_alumno(self, datos):
        try:
            alumno = {
                'nombre': datos['nombre'],
                'carrera': datos['carrera'],
                'semestre': int(datos['semestre']),
                'promedio': float(datos['promedio']),
                'materias': [m.strip() for m in datos['materias'].split(',') if m.strip()]
            }
            resultado = self.coleccion.insert_one(alumno)
            messagebox.showinfo("Éxito", f"Alumno creado con ID: {resultado.inserted_id}")
            self.cargar_alumnos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear alumno:\n{e}")

    def actualizar_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un alumno para actualizar")
            return
        alumno_id = sel[0]
        try:
            alumno = self.coleccion.find_one({'_id': ObjectId(alumno_id)})
            if not alumno:
                messagebox.showerror("Error", "Alumno no encontrado")
                return
            DialogAlumno(self, lambda datos: self.actualizar_alumno(alumno_id, datos), alumno)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener alumno:\n{e}")

    def actualizar_alumno(self, alumno_id, datos):
        actualizacion = {}
        if datos['nombre']:
            actualizacion['nombre'] = datos['nombre']
        if datos['carrera']:
            actualizacion['carrera'] = datos['carrera']
        if datos['semestre']:
            try:
                actualizacion['semestre'] = int(datos['semestre'])
            except:
                pass
        if datos['promedio']:
            try:
                actualizacion['promedio'] = float(datos['promedio'])
            except:
                pass
        if datos['materias']:
            actualizacion['materias'] = [m.strip() for m in datos['materias'].split(',') if m.strip()]

        if not actualizacion:
            messagebox.showinfo("Sin cambios", "No se detectaron cambios")
            return

        try:
            self.coleccion.update_one({'_id': ObjectId(alumno_id)}, {'$set': actualizacion})
            messagebox.showinfo("Éxito", "Alumno actualizado")
            self.cargar_alumnos()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar:\n{e}")

    def eliminar_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un alumno para eliminar")
            return
        alumno_id = sel[0]
        if not messagebox.askyesno("Confirmar", "¿Eliminar alumno seleccionado?"):
            return
        try:
            res = self.coleccion.delete_one({'_id': ObjectId(alumno_id)})
            if res.deleted_count > 0:
                messagebox.showinfo("Éxito", "Alumno eliminado")
                self.cargar_alumnos()
            else:
                messagebox.showerror("Error", "Alumno no encontrado")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar:\n{e}")

    def buscar_por_id_dialog(self):
        def on_ok():
            id_str = entry.get().strip()
            top.destroy()
            if not ObjectId.is_valid(id_str):
                messagebox.showerror("Error", "ID inválido")
                return
            try:
                alumno = self.coleccion.find_one({'_id': ObjectId(id_str)})
                if alumno:
                    for i in self.tree.get_children():
                        self.tree.delete(i)
                    materias = ', '.join(alumno.get('materias', []))
                    self.tree.insert('', tk.END, iid=str(alumno['_id']), values=(str(alumno.get('_id','')), alumno.get('nombre',''), alumno.get('carrera',''), alumno.get('semestre',''), alumno.get('promedio',''), materias))
                else:
                    messagebox.showinfo("Resultado", "Alumno no encontrado")
            except Exception as e:
                messagebox.showerror("Error", f"Error en búsqueda:\n{e}")

        top = tk.Toplevel(self)
        top.title("Buscar por ID")
        tk.Label(top, text="ID:").pack(side=tk.LEFT, padx=6, pady=6)
        entry = tk.Entry(top, width=50)
        entry.pack(side=tk.LEFT, padx=6, pady=6)
        tk.Button(top, text="Buscar", command=on_ok).pack(side=tk.LEFT, padx=6)


class DialogAlumno(tk.Toplevel):
    def __init__(self, parent, callback, alumno=None):
        super().__init__(parent)
        self.callback = callback
        self.title("Alumno")

        tk.Label(self, text="Nombre").grid(row=0, column=0, sticky=tk.W, padx=6, pady=4)
        self.e_nombre = tk.Entry(self, width=50)
        self.e_nombre.grid(row=0, column=1, padx=6, pady=4)

        tk.Label(self, text="Carrera").grid(row=1, column=0, sticky=tk.W, padx=6, pady=4)
        self.e_carrera = tk.Entry(self, width=50)
        self.e_carrera.grid(row=1, column=1, padx=6, pady=4)

        tk.Label(self, text="Semestre").grid(row=2, column=0, sticky=tk.W, padx=6, pady=4)
        self.e_semestre = tk.Entry(self, width=20)
        self.e_semestre.grid(row=2, column=1, sticky=tk.W, padx=6, pady=4)

        tk.Label(self, text="Promedio").grid(row=3, column=0, sticky=tk.W, padx=6, pady=4)
        self.e_promedio = tk.Entry(self, width=20)
        self.e_promedio.grid(row=3, column=1, sticky=tk.W, padx=6, pady=4)

        tk.Label(self, text="Materias (comma)").grid(row=4, column=0, sticky=tk.W, padx=6, pady=4)
        self.e_materias = tk.Entry(self, width=50)
        self.e_materias.grid(row=4, column=1, padx=6, pady=4)

        btn = tk.Button(self, text="Guardar", command=self.on_guardar)
        btn.grid(row=5, column=0, columnspan=2, pady=8)

        if alumno:
            self.e_nombre.insert(0, alumno.get('nombre',''))
            self.e_carrera.insert(0, alumno.get('carrera',''))
            self.e_semestre.insert(0, str(alumno.get('semestre','')))
            self.e_promedio.insert(0, str(alumno.get('promedio','')))
            self.e_materias.insert(0, ', '.join(alumno.get('materias', [])))

    def on_guardar(self):
        datos = {
            'nombre': self.e_nombre.get().strip(),
            'carrera': self.e_carrera.get().strip(),
            'semestre': self.e_semestre.get().strip(),
            'promedio': self.e_promedio.get().strip(),
            'materias': self.e_materias.get().strip(),
        }
        self.callback(datos)
        self.destroy()


if __name__ == '__main__':
    app = TesiApp()
    app.mainloop()
