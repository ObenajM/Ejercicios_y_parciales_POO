from cuenta_ahorros import CuentaAhorros
from cuenta_corriente import CuentaCorriente

# Crear una cuenta de ahorros
cuenta_ahorros = CuentaAhorros(15000, 5.0)
cuenta_ahorros.consignar(5000)
cuenta_ahorros.retirar(3000)
cuenta_ahorros.extracto_mensual()
cuenta_ahorros.imprimir()

print("\n---\n")

# Crear una cuenta corriente
cuenta_corriente = CuentaCorriente(2000, 4.0)
cuenta_corriente.retirar(5000)  # Sobregiro
cuenta_corriente.consignar(3000)
cuenta_corriente.extracto_mensual()
cuenta_corriente.imprimir()
