class Usuario:

    def __init__(self, nombre, correo, password, id_rol):

        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.id_rol = id_rol

    def mostrar(self):

        return f"{self.nombre} - {self.correo}"
