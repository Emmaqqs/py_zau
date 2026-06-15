import pymssql
from .base import Database

class SQLServerDatabase(Database):
    def __init__(self, server="localhost", user="sa", password="SqlPassword123!", database="master"):
        self.server = server
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def conectar(self):
        try:
            self.conexion = pymssql.connect(
                server=self.server,
                user=self.user,
                password=self.password,
                database=self.database
            )
            cursor = self.conexion.cursor()
            # Crear tabla si no existe
            cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'usuarios')
            BEGIN
                CREATE TABLE usuarios (
                    id INT IDENTITY(1,1) PRIMARY KEY,
                    nombre NVARCHAR(255) NOT NULL,
                    correo NVARCHAR(255) UNIQUE NOT NULL,
                    password NVARCHAR(255) NOT NULL
                )
            END
            """)
            self.conexion.commit()
            print("✅ Conexión a SQL Server (Docker) establecida.")
        except Exception as e:
            print(f"❌ Error conectando a SQL Server: {e}")

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
            print(f"✅ Usuario {nombre} guardado en SQL Server.")
        except Exception as e:
            print(f"❌ Error guardando en SQL Server: {e}")

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
            print(f"❌ Error buscando en SQL Server: {e}")
            return None

    def cerrar(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión SQL Server cerrada.")
