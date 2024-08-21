from inmueble import Inmueble

class Local(Inmueble):
    INTERNO = 'INTERNO'
    CALLE = 'CALLE'

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipo_local}")