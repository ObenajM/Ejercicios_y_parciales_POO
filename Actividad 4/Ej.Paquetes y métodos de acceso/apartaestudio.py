from apartamento import Apartamento

class Apartaestudio(Apartamento):
    valor_area = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion):
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)
