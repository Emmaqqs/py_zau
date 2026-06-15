from .sqlite_db import SQLiteDatabase
from .mongo_db import MongoDatabase
from .mysql_db import MySQLDatabase
from .oracle_db import OracleDatabase
from .sqlserver_db import SQLServerDatabase

class DatabaseFactory:
    @staticmethod
    def obtener_base_datos(tipo):
        tipo = tipo.lower()
        if tipo == "sqlite":
            return SQLiteDatabase()
        elif tipo == "mongo":
            return MongoDatabase()
        elif tipo == "mysql":
            return MySQLDatabase()
        elif tipo == "oracle":
            return OracleDatabase()
        elif tipo == "sqlserver":
            return SQLServerDatabase()
        else:
            raise ValueError(f"Tipo de base de datos no soportado: {tipo}")
