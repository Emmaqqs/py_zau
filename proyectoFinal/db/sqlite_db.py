import sqlite3
from .base import Database

class SQLiteDatabase(Database):
    def __init__(self, db_path="usuarios_final.db"):
        self.db_path = db_path
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.db_path)
            cursor = self.conexion.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                correo TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """)
            self.conexion.commit()
            print("✅ Conexión a SQLite establecida.")
        except Exception as e:
            print(f"❌ Error conectando a SQLite: {e}")

    def guardar_usuario(self, nombre, correo, password):
        if not self.conexion:
            self.conectar()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios(nombre, correo, password) VALUES(?, ?, ?)",
                (nombre, correo, password)
            )
            self.conexion.commit()
            print(f"✅ Usuario {nombre} guardado en SQLite.")
        except Exception as e:
            print(f"❌ Error guardando en SQLite: {e}")

    def buscar_usuario(self, correo, password):
        if not self.conexion:
            self.conectar()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE correo = ? AND password = ?",
                (correo, password)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Error buscando en SQLite: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión SQLite cerrada.")
