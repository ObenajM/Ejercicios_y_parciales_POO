import math

class FiguraGeométrica:
    def __init__(self):
        self._volumen = 0
        self._superficie = 0

    def set_volumen(self, volumen):
        self._volumen = volumen

    def set_superficie(self, superficie):
        self._superficie = superficie

    def get_volumen(self):
        return self._volumen

    def get_superficie(self):
        return self._superficie


class Cilindro(FiguraGeométrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return math.pi * self.altura * self.radio ** 2

    def calcular_superficie(self):
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_base = 2 * math.pi * self.radio ** 2
        return area_lateral + area_base


class Esfera(FiguraGeométrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (4/3) * math.pi * self.radio ** 3

    def calcular_superficie(self):
        return 4 * math.pi * self.radio ** 2


class Piramide(FiguraGeométrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema
        self.set_volumen(self.calcular_volumen())
        self.set_superficie(self.calcular_superficie())

    def calcular_volumen(self):
        return (self.base ** 2 * self.altura) / 3

    def calcular_superficie(self):
        area_base = self.base ** 2
        area_lado = 4 * self.base * self.apotema / 2
        return area_base + area_lado
