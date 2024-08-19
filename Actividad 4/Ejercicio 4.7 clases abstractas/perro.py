from canido import Canido

class Perro(Canido):
    def __init__(self):
        super().__init__("Ladrido", "Carnívoro", "Doméstico", "Canis lupus familiaris")

    def get_nombre_cientifico(self):
        return self._nombre_cientifico

    def get_sonido(self):
        return self._sonido

    def get_alimentos(self):
        return self._alimentos

    def get_habitat(self):
        return self._habitat
