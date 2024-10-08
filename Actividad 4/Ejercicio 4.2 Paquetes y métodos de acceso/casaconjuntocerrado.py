from casaurbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    valor_area = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos, valor_administracion, tiene_piscina, tiene_campos_deportivos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self.valor_administracion}")
        print(f"Tiene piscina? = {self.tiene_piscina}")
        print(f"Tiene campos deportivos? = {self.tiene_campos_deportivos}")
        print()
