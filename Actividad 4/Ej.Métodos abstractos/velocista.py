from ciclista import Ciclista

class Velocista(Ciclista):
    def __init__(self, identificador: int, nombre: str, potencia_promedio: float, velocidad_promedio: float):
        super().__init__(identificador, nombre)
        self.potencia_promedio = potencia_promedio
        self.velocidad_promedio = velocidad_promedio

    def get_potencia_promedio(self) -> float:
        return self.potencia_promedio

    def set_potencia_promedio(self, potencia_promedio: float):
        self.potencia_promedio = potencia_promedio

    def get_velocidad_promedio(self) -> float:
        return self.velocidad_promedio

    def set_velocidad_promedio(self, velocidad_promedio: float):
        self.velocidad_promedio = velocidad_promedio

    def imprimir(self):
        super().imprimir()
        print(f"Potencia promedio = {self.potencia_promedio}")
        print(f"Velocidad promedio = {self.velocidad_promedio}")

    def imprimir_tipo(self) -> str:
        return "Es un velocista"
