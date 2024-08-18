from Cuenta import Cuenta

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self._activa = saldo >= 10000

    def consignar(self, cantidad):
        if self._activa:
            super().consignar(cantidad)
        self._activa = self._saldo >= 10000

    def retirar(self, cantidad):
        if self._activa:
            super().retirar(cantidad)
            self._activa = self._saldo >= 10000
        else:
            print("La cuenta está inactiva")

    def extracto_mensual(self):
        if self._num_retiros > 4:
            self._comision_mensual += (self._num_retiros - 4) * 1000
        super().extracto_mensual()
        self._activa = self._saldo >= 10000

    def imprimir(self):
        super().imprimir()
        print(f"Cuenta activa: {self._activa}")
        print(f"Transacciones totales: {self._num_consignaciones + self._num_retiros}")
