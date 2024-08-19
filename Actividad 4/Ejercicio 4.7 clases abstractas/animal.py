from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, sonido, alimentos, habitat, nombre_cientifico):
        self._sonido = sonido
        self._alimentos = alimentos
        self._habitat = habitat
        self._nombre_cientifico = nombre_cientifico

    @abstractmethod
    def get_nombre_cientifico(self):
        pass

    @abstractmethod
    def get_sonido(self):
        pass

    @abstractmethod
    def get_alimentos(self):
        pass

    @abstractmethod
    def get_habitat(self):
        pass