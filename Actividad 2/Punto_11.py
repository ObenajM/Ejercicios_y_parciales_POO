class Mayor():
    def __init__(self, N1, N2, N3):
        self.N1 = N1
        self.N2 = N2
        self.N3 = N3
    def NumMayor(self):
        if (self.N1 > self.N2) and (self.N1 > self.N3):
            Mayor = self.N1
        else:
            if self.N2 > self.N3:
                Mayor = self.N2
            else:
                Mayor = self.N3
        return "Elvalor mayor entre {} , {} y {} es: {}".format(self.N1, self.N2, self.N3, Mayor)
    def __str__(self):
        return "{}".format(self.NumMayor())

N1=float(input("Ingrese el primer numero: "))
N2=float(input("Ingrese el segundo numero: "))
N3=float(input("Ingrese el tercer numero: "))
NumMayor1 = Mayor(N1, N2, N3)
print(NumMayor1)