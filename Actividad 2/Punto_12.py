class SalTrbajador():
    def __init__(self, Nombres, Horas, Valor):
        self.Nombres = Nombres
        self.Horas = Horas
        self.Valor = Valor
    
    def Salario(self):
        if self.Horas > 40:
            Het= self.Horas-40
            if Het>8:
                Hees=Het-8
                Salario=40*self.Valor+16*self.Valor+Hees*3*self.Valor
            else:
                Salario=40*self.Valor+Het*2*self.Valor
        else:
            Salario=self.Horas*self.Valor
        return "El trabajador {} devengo {}".format(self.Nombres,Salario)
    
    def __str__(self):
        return "{}".format(self.Salario())

Nombres = input("Ingrese el nombre del trabajador: ")
Horas = int(input("Ingrese el número de horas trabajadas: "))
Valor = float(input("Ingrese el valor de la hora: "))
Trabajador = SalTrbajador(Nombres,Horas,Valor)
print(Trabajador)


