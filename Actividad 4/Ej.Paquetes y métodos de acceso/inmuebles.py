from inmueble import Inmueble
from inmueble_vivienda import InmuebleVivienda
from apartamento import Apartamento
from casa_rural import CasaRural
from casa_urbana import CasaUrbana
from apartamento_familiar import ApartamentoFamiliar
from apartaestudio import Apartaestudio
from casa_conjunto_cerrado import CasaConjuntoCerrado
from casa_independiente import CasaIndependiente
from local import Local
from local_comercial import LocalComercial
from oficina import Oficina

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
