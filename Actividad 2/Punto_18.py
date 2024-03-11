class Empleado(object):
    def __init__(self, cod_empleado, nombre, num_horas_tra,Val_hora,porc_retencion):
        self.cod_empleado = cod_empleado
        self.nombre = nombre
        self.num_horas_tra = num_horas_tra
        self.Val_hora = Val_hora
        self.porc_retencion = porc_retencion
    
    def salario_bruto(self):
        return self.num_horas_tra * self.Val_hora
    
    def salario_neto(self):
        return self.salario_bruto() * (1 - self.porc_retencion / 100)
    
    def __str__(self):
        return "Nombre: {} -Salario Bruto: ${} -Salario Neto: ${}".format(self.nombre, self.salario_bruto(),self.salario_neto())
    
Empleado1 = Empleado("001", "Juan", 40, 15, 10)
Empleado2 = Empleado("002", "Maria", 50, 20, 5)
print(Empleado1, Empleado2)
        
        