from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente

# Cuenta de ahorros
cuenta_ahorros = CuentaAhorros(100000, 10)
cuenta_ahorros.consignar(50000)
cuenta_ahorros.retirar(70000)
cuenta_ahorros.extracto_mensual()
cuenta_ahorros.imprimir() 

