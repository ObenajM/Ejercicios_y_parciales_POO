from ciclista import Ciclista

class Contrarrelojista(Ciclista):
    def __init__(self, identificador, nombre, velocidad_maxima):
        super().__init__(identificador, nombre)
        self.velocidad_maxima = velocidad_maxima

    def get_velocidad_maxima(self):
        return self.velocidad_maxima

    def set_velocidad_maxima(self, velocidad_maxima):
        self.velocidad_maxima = velocidad_maxima

    def imprimir(self):
        super().imprimir()
        print(f"Velocidad máxima = {self.velocidad_maxima}")

    def imprimir_tipo(self):
        return "Es un contrarrelojista"
