class Esfera:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

def main():
    peso_A = float(input("Ingrese el peso de la esfera A: "))
    peso_B = float(input("Ingrese el peso de la esfera B: "))
    peso_C = float(input("Ingrese el peso de la esfera C: "))

    esfera_A = Esfera('A', peso_A)
    esfera_B = Esfera('B', peso_B)
    esfera_C = Esfera('C', peso_C)

    if esfera_A.peso > esfera_B.peso and esfera_A.peso > esfera_C.peso:
        print("La esfera de mayor peso es la", esfera_A.nombre)
    elif esfera_B.peso > esfera_A.peso and esfera_B.peso > esfera_C.peso:
        print("La esfera de mayor peso es la", esfera_B.nombre)
    elif esfera_C.peso > esfera_A.peso and esfera_C.peso > esfera_B.peso:
        print("La esfera de mayor peso es la", esfera_C.nombre)

if __name__ == "__main__":
    main()
