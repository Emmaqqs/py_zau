class Actividad:

    def __init__(self, descripcion, fecha):

        self.descripcion = descripcion
        self.fecha = fecha

    def mostrar(self):

        return f"{self.descripcion} {self.fecha}"
