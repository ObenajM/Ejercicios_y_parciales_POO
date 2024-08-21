from inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.numero_habitaciones = numero_habitaciones
        self.numero_banos = numero_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.numero_habitaciones}")
        print(f"Número de baños = {self.numero_banos}")