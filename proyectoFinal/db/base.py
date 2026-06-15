from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def conectar(self):
        pass

    @abstractmethod
    def guardar_usuario(self, nombre, correo, password):
        pass

    @abstractmethod
    def buscar_usuario(self, correo, password):
        pass

    @abstractmethod
    def cerrar(self):
        pass
