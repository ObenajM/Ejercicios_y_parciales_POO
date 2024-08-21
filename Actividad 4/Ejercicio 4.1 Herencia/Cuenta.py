class Cuenta:
    def __init__(self, saldo, tasa_anual):
        self._saldo = saldo
        self._num_consignaciones = 0
        self._num_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = 0.0

    def consignar(self, cantidad):
        self._saldo += cantidad
        self._num_consignaciones += 1

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            self._num_retiros += 1
        else:
            print("Saldo insuficiente")

    def calcular_interes_mensual(self):
        interes_mensual = (self._tasa_anual / 12) / 100 * self._saldo
        self._saldo += interes_mensual

    def extracto_mensual(self):
        self._saldo -= self._comision_mensual
        self.calcular_interes_mensual()
        self._comision_mensual = 0.0 

    def imprimir(self):
        print(f"Saldo: {self._saldo}")
        print(f"Comisión mensual: {self._comision_mensual}")
        print(f"Número de consignaciones: {self._num_consignaciones}")
        print(f"Número de retiros: {self._num_retiros}")
        print(f"Tasa anual: {self._tasa_anual}")
        
