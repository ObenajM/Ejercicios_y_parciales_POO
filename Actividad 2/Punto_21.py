import math
class triangulo():
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
    
    def perimetro(self):
        return self.l1 + self.l2 + self.l3
    
    def semipremetro(self):
        return self.perimetro()/2
    
    def area(self):
        return math.sqrt(self.semipremetro()*(self.semipremetro()-self.l1)*(self.semipremetro()-self.l2)*(self.semipremetro()-self.l3))
    
    def __str__(self):
        return "El perimetro del triangulo es {}, el semiperimetro es {} y el area es {}".format(self.perimetro(),self.semipremetro(),self.area())

lado1 = float(input("Ingrese el lado 1 del triangulo: "))
lado2 = float(input("Ingrese el lado 2 del triangulo: "))
lado3 = float(input("Ingrese el lado 3 del triangulo: "))

triangulo1 = triangulo(5,4,7)
print(triangulo1)



