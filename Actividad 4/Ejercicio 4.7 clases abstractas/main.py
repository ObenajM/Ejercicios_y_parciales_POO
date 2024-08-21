from perro import Perro
from lobo import Lobo
from leon import Leon
from gato import Gato

def main():
    animales = [
        Perro(),
        Lobo(),
        Leon(),
        Gato()
    ]

    for animal in animales:
        print(f"Nombre Científico: {animal.get_nombre_cientifico()}")
        print(f"Sonido: {animal.get_sonido()}")
        print(f"Alimentos: {animal.get_alimentos()}")
        print(f"Hábitat: {animal.get_habitat()}")
        print("--------------------------")

if __name__ == "__main__":
    main()
