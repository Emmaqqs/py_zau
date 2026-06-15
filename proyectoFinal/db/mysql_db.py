import mysql.connector
from .base import Database

class MySQLDatabase(Database):
    def __init__(self, host="localhost", user="dbuser", password="dbpassword", database="mydb"):
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database
        }
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = mysql.connector.connect(**self.config)
            cursor = self.conexion.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                correo VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL
            )
            """)
            self.conexion.commit()
            print("✅ Conexión a MySQL (Docker) establecida.")
        except Exception as e:
            print(f"❌ Error conectando a MySQL: {e}")

    def guardar_usuario(self, nombre, correo, password):
        if not self.conexion:
            self.conectar()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios(nombre, correo, password) VALUES(%s, %s, %s)",
                (nombre, correo, password)
            )
            self.conexion.commit()
            print(f"✅ Usuario {nombre} guardado en MySQL.")
        except Exception as e:
            print(f"❌ Error guardando en MySQL: {e}")

    def buscar_usuario(self, correo, password):
        if not self.conexion:
            self.conectar()
        try:
            cursor = self.conexion.cursor()
            cursor.execute(
                "SELECT * FROM usuarios WHERE correo = %s AND password = %s",
                (correo, password)
            )
            return cursor.fetchone()
        except Exception as e:
            print(f"❌ Error buscando en MySQL: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión MySQL cerrada.")
