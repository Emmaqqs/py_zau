from pymongo import MongoClient
from .base import Database

class MongoDatabase(Database):
    def __init__(self, uri="mongodb://admin:mongopassword@localhost:27017/", db_name="mydb"):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None
        self.coleccion = None

    def conectar(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            self.coleccion = self.db["usuarios"]
            # Verificar conexión
            self.client.admin.command('ping')
            print("✅ Conexión a MongoDB (Docker) establecida.")
        except Exception as e:
            print(f"❌ Error conectando a MongoDB: {e}")

    def guardar_usuario(self, nombre, correo, password):
        if not self.coleccion:
            self.conectar()
        try:
            usuario = {
                "nombre": nombre,
                "correo": correo,
                "password": password
            }
            self.coleccion.insert_one(usuario)
            print(f"✅ Usuario {nombre} guardado en MongoDB.")
        except Exception as e:
            print(f"❌ Error guardando en MongoDB: {e}")

    def buscar_usuario(self, correo, password):
        if not self.coleccion:
            self.conectar()
        try:
            return self.coleccion.find_one({"correo": correo, "password": password})
        except Exception as e:
            print(f"❌ Error buscando en MongoDB: {e}")
            return None

    def cerrar(self):
        if self.client:
            self.client.close()
            print("Conexión MongoDB cerrada.")
