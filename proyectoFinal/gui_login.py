import tkinter as tk
from tkinter import ttk, messagebox
from db.factory import DatabaseFactory

class Dashboard(tk.Toplevel):
    def __init__(self, parent, usuario_data):
        super().__init__(parent)
        self.title("Panel Principal")
        self.geometry("600x400")
        self.configure(bg="white")
        
        # Centrar ventana
        self.transient(parent)
        self.grab_set()
        
        tk.Label(self, text=f"¡Bienvenido, {usuario_data}!", font=("Arial", 18, "bold"), bg="white").pack(pady=50)
        tk.Label(self, text="Has iniciado sesión correctamente.", font=("Arial", 12), bg="white").pack(pady=10)
        
        ttk.Button(self, text="Cerrar Sesión", command=self.destroy).pack(pady=30)

class LoginGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Multi-DB - Autenticación")
        self.geometry("400x550")
        self.resizable(False, False)
        self.configure(bg="#f0f0f0")
        
        self.modo_registro = False # Por defecto iniciamos en modo Login
        
        self.create_widgets()

    def create_widgets(self):
        # Título dinámico
        self.lbl_titulo = tk.Label(self, text="Inicio de Sesión", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333")
        self.lbl_titulo.pack(pady=20)

        # Frame para el formulario
        self.form_frame = tk.Frame(self, bg="#f0f0f0")
        self.form_frame.pack(padx=20, fill=tk.X)

        # Campo Nombre (solo para registro)
        self.lbl_nombre = ttk.Label(self.form_frame, text="Nombre Completo:")
        self.ent_nombre = ttk.Entry(self.form_frame)
        
        # Correo (siempre visible)
        ttk.Label(self.form_frame, text="Correo Electrónico:").pack(anchor=tk.W, pady=(10, 0))
        self.ent_correo = ttk.Entry(self.form_frame)
        self.ent_correo.pack(fill=tk.X, pady=5)

        # Password (siempre visible)
        ttk.Label(self.form_frame, text="Contraseña:").pack(anchor=tk.W, pady=(10, 0))
        self.ent_password = ttk.Entry(self.form_frame, show="*")
        self.ent_password.pack(fill=tk.X, pady=5)

        # Selector de Base de Datos
        ttk.Label(self.form_frame, text="Seleccionar Base de Datos:").pack(anchor=tk.W, pady=(20, 0))
        self.db_options = ["SQLite", "Mongo", "MySQL", "Oracle", "SQLServer"]
        self.cmb_db = ttk.Combobox(self.form_frame, values=self.db_options, state="readonly")
        self.cmb_db.set("SQLite")
        self.cmb_db.pack(fill=tk.X, pady=5)

        # Botón Principal
        self.btn_accion = ttk.Button(self, text="INICIAR SESIÓN", command=self.ejecutar_accion)
        self.btn_accion.pack(pady=20, padx=50, fill=tk.X)

        # Botón para cambiar de modo
        self.btn_switch = tk.Button(self, text="¿No tienes cuenta? Regístrate aquí", 
                                   font=("Arial", 9, "underline"), bg="#f0f0f0", fg="blue", 
                                   border=0, cursor="hand2", command=self.switch_mode)
        self.btn_switch.pack(pady=5)

        # Pie de página
        tk.Label(self, text="Docker Databases Ready 🐳", font=("Arial", 8, "italic"), bg="#f0f0f0", fg="#666").pack(side=tk.BOTTOM, pady=10)

        # Ajustar vista inicial (Login)
        self.update_ui()

    def switch_mode(self):
        self.modo_registro = not self.modo_registro
        self.update_ui()

    def update_ui(self):
        # Limpiar el frame para reordenar
        for widget in self.form_frame.winfo_children():
            widget.pack_forget()

        if self.modo_registro:
            self.lbl_titulo.config(text="Registro de Usuario")
            self.btn_accion.config(text="REGISTRAR USUARIO")
            self.btn_switch.config(text="¿Ya tienes cuenta? Inicia sesión")
            
            # Orden para Registro: Nombre, Correo, Password, DB
            self.lbl_nombre.pack(anchor=tk.W, pady=(10, 0))
            self.ent_nombre.pack(fill=tk.X, pady=5)
        else:
            self.lbl_titulo.config(text="Inicio de Sesión")
            self.btn_accion.config(text="INICIAR SESIÓN")
            self.btn_switch.config(text="¿No tienes cuenta? Regístrate aquí")
            
            # Orden para Login: Correo, Password, DB (Nombre oculto)

        # Campos comunes siempre al final del orden actual
        ttk.Label(self.form_frame, text="Correo Electrónico:").pack(anchor=tk.W, pady=(10, 0))
        self.ent_correo.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.form_frame, text="Contraseña:").pack(anchor=tk.W, pady=(10, 0))
        self.ent_password.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.form_frame, text="Seleccionar Base de Datos:").pack(anchor=tk.W, pady=(20, 0))
        self.cmb_db.pack(fill=tk.X, pady=5)

    def ejecutar_accion(self):
        correo = self.ent_correo.get().strip()
        password = self.ent_password.get().strip()
        tipo_db = self.cmb_db.get().lower()

        if not correo or not password:
            messagebox.showwarning("Campos Requeridos", "Por favor completa correo y contraseña.")
            return

        try:
            db = DatabaseFactory.obtener_base_datos(tipo_db)
            db.conectar()

            if self.modo_registro:
                nombre = self.ent_nombre.get().strip()
                if not nombre:
                    messagebox.showwarning("Campos Requeridos", "El nombre es obligatorio para el registro.")
                    return
                db.guardar_usuario(nombre, correo, password)
                messagebox.showinfo("Éxito", f"Usuario {nombre} registrado correctamente en {tipo_db.upper()}.")
                self.switch_mode() # Cambiar a login tras registrarse
            else:
                usuario = db.buscar_usuario(correo, password)
                if usuario:
                    messagebox.showinfo("Éxito", "Login correcto.")
                    # Si es Mongo (dict) o SQL (tuple) tratamos de sacar el nombre
                    nombre_user = usuario.get('nombre') if isinstance(usuario, dict) else (usuario[1] if len(usuario) > 1 else correo)
                    self.abrir_dashboard(nombre_user)
                else:
                    messagebox.showerror("Error", "Credenciales incorrectas o usuario no encontrado.")
            
            db.cerrar()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error en la operación: {e}")

    def abrir_dashboard(self, nombre):
        self.withdraw() # Ocultar ventana login
        dash = Dashboard(self, nombre)
        self.wait_window(dash)
        self.deiconify() # Volver a mostrar login al cerrar dashboard

    def limpiar_campos(self):
        self.ent_nombre.delete(0, tk.END)
        self.ent_correo.delete(0, tk.END)
        self.ent_password.delete(0, tk.END)

if __name__ == "__main__":
    app = LoginGUI()
    app.mainloop()
