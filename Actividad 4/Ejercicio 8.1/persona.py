class Persona:
    def __init__(self, nombre, apellidos, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.direccion} - {self.telefono}"
