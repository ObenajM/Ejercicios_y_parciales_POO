class Equipo:

    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.lista_ciclistas = [] # Lista de ciclistas
        self.total_tiempo = 0.0
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_pais(self):
        return self.pais

    def set_pais(self, pais):
        self.pais = pais

    def añadir_ciclista(self, ciclista):
        self.lista_ciclistas.append(ciclista)

    def listar_equipo(self):
        for ciclista in self.lista_ciclistas:
            print(ciclista.get_nombre())

    def buscar_ciclista(self):
        nombre_ciclista = input("Ingrese el nombre del ciclista: ")
        for ciclista in self.lista_ciclistas:
            if ciclista.get_nombre() == nombre_ciclista:
                print(ciclista.get_nombre())

    def calcular_total_tiempo(self):
        self.total_tiempo = sum(ciclista.get_tiempo_acumulado() for ciclista in self.lista_ciclistas)

    def imprimir(self):
        print(f"Nombre del equipo = {self.nombre}")
        print(f"País = {self.pais}")
        print(f"Total tiempo del equipo = {self.total_tiempo}")
