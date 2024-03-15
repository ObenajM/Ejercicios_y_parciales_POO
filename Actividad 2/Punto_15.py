class Esferas():
    def __init__(self, PesoA,PesoB,PesoC,PesoD):
        self.PesoA = PesoA
        self.PesoB = PesoB
        self.PesoC = PesoC
        self.PesoD = PesoD
    
    def PesoDiferente(self):
        if (self.PesoA == self.PesoB) and (self.PesoA == self.PesoC):
            if self.PesoD > self.PesoA:
                salida1="La esfera D es la diferente y"
            else:
                salida1="La esfera D es la diferente y"
        else:
            if (self.PesoA == self.PesoB) and (self.PesoA == self.PesoD):
                salida1="La esfera C es la diferente y"
                if self.PesoC > self.PesoA:
                    salida2="es de mayor peso."
                else:
                    salida2=" es de menor peso."
            else:
                if (self.PesoA == self.PesoC) and (self.PesoA == self.PesoD):
                    salida1="La esfera B es la diferente y"
                    if self.PesoB > self.PesoD:
                        salida2=" es de mayor peso."
                    else:
                        salida2="Y es de menor peso."
                else:
                    salida1="La esfera A es la diferente y"
                    if self.PesoA > self.PesoB:
                        salida2=" es de mayor peso."
                    else:
                        salida2=" es de menor peso."
        return salida1+salida2
    
    def __str__(self):
        return "{}".format(self.PesoDiferente())

PesoA = float(input("Ingrese el peso de la esfera A: "))
PesoB = float(input("Ingrese el peso de la esfera B: "))
PesoC = float(input("Ingrese el peso de la esfera C: "))
PesoD = float(input("Ingrese el peso de la esfera D: "))
Esferas = Esferas(PesoA,PesoB,PesoC,PesoD)
print(Esferas)


        