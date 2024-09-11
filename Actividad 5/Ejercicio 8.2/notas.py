import math

class Notas:
    def __init__(self, notas):
        self.notas = notas

    def calcular_promedio(self):
        return sum(self.notas) / len(self.notas)

    def calcular_desviacion_estandar(self):
        promedio = self.calcular_promedio()
        suma = sum((x - promedio) ** 2 for x in self.notas)
        return math.sqrt(suma / len(self.notas))

    def obtener_mayor_nota(self):
        return max(self.notas)

    def obtener_menor_nota(self):
        return min(self.notas)
