from apartamentofamiliar import ApartamentoFamiliar
from apartaestudio import Apartaestudio

def main():
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcular_precio_venta(ApartamentoFamiliar.valor_area)
    apto1.imprimir()

    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    print("Datos apartaestudio")
    aptestudio1.calcular_precio_venta(Apartaestudio.valor_area)
    aptestudio1.imprimir()

if __name__ == "__main__":
    main()