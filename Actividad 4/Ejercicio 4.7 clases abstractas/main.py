from perro import Perro
from lobo import Lobo
from leon import Leon
from gato import Gato

def main():
    # Crear una lista de animales
    animales = [
        Perro(),
        Lobo(),
        Leon(),
        Gato()
    ]

    # Imprimir los atributos de cada animal
    for animal in animales:
        print(f"Nombre Científico: {animal.get_nombre_cientifico()}")
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print("--------------------------")

if __name__ == "__main__":
    main()
