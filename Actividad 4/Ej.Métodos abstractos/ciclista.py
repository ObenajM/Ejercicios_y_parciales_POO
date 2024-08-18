from abc import ABC, abstractmethod

class Ciclista(ABC):
    def __init__(self, identificador: int, nombre: str):
        self.identificador = identificador
        self.nombre = nombre
        self.tiempo_acumulado = 0

    @abstractmethod
    def imprimir_tipo(self) -> str:
        pass

    def get_identificador(self) -> int:
        return self.identificador

    def set_identificador(self, identificador: int):
        self.identificador = identificador

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_tiempo_acumulado(self) -> int:
        return self.tiempo_acumulado

    def set_tiempo_acumulado(self, tiempo_acumulado: int):
        self.tiempo_acumulado = tiempo_acumulado

    def imprimir(self):
        print(f"Identificador = {self.identificador}")
        print(f"Nombre = {self.nombre}")
        print(f"Tiempo Acumulado = {self.tiempo_acumulado}")
