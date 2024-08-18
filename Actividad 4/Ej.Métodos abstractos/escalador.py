from ciclista import Ciclista

class Escalador(Ciclista):
    def __init__(self, identificador, nombre, aceleracion_promedio, grado_rampa):
        super().__init__(identificador, nombre)
        self.aceleracion_promedio = aceleracion_promedio
        self.grado_rampa = grado_rampa

    def get_aceleracion_promedio(self):
        return self.aceleracion_promedio

    def set_aceleracion_promedio(self, aceleracion_promedio):
        self.aceleracion_promedio = aceleracion_promedio

    def get_grado_rampa(self):
        return self.grado_rampa

    def set_grado_rampa(self, grado_rampa):
        self.grado_rampa = grado_rampa

    def imprimir(self):
        super().imprimir()
        print(f"Aceleración promedio = {self.aceleracion_promedio}")
        print(f"Grado de rampa = {self.grado_rampa}")

    def imprimir_tipo(self):
        return "Es un escalador"
