nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_por_hora = float(input("Ingrese el salario por hora del empleado: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en el mes: "))

salario_mensual = salario_por_hora * horas_trabajadas
if salario_mensual > 450000:
    print(nombre_empleado, ":", salario_mensual)
else:
    print(nombre_empleado)
