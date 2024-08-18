from ciclista import Ciclista

class Velocista(Ciclista):
    def __init__(self, identificador, nombre, potencia_promedio, velocidad_promedio):
        super().__init__(identificador, nombre)
        self.potencia_promedio = potencia_promedio
        self.velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self):
        return self.potencia_promedio

    def set_potencia_promedio(self, potencia_promedio):
        self.potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self):
        return self.velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio):
        self.velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio = {self.potencia_promedio}")
        print(f"Velocidad promedio = {self.velocidad_promedio}")

    def imprimir_tipo(self):
        return "Es un velocista"
