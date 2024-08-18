from Cuenta import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._sobregiro = 0.0

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            super().retirar(cantidad)
        else:
            sobregiro_necesario = cantidad - self._saldo
            self._sobregiro += sobregiro_necesario
            self._saldo = 0
            self._num_retiros += 1

    def consignar(self, cantidad):
        if self._sobregiro > 0:
            if cantidad >= self._sobregiro:
                cantidad -= self._sobregiro
                self._sobregiro = 0
            else:
                self._sobregiro -= cantidad
                cantidad = 0
        super().consignar(cantidad)

    def extracto_mensual(self):
        super().extracto_mensual()

    def imprimir(self):
        super().imprimir()
        print(f"Valor de sobregiro: {self._sobregiro}")
        print(f"Transacciones totales: {self._num_consignaciones + self._num_retiros}")
