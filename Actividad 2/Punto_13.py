class Promocion():
    def __init__(self, VaCompra, CoBolita):
        self.VaCompra = VaCompra
        self.CoBolita = CoBolita
    def Descuento(self):
        if self.CoBolita=="Blanco" or self.CoBolita=="blanco" or self.CoBolita=="BLANCO":
            PDescuento = 0
        elif self.CoBolita=="Verde" or self.CoBolita=="verde" or self.CoBolita=="VERDE":
                PDescuento = 10
        elif self.CoBolita=="Amarillo" or self.CoBolita=="amarillo" or self.CoBolita=="AMARILLO":
                    PDescuento = 25
        elif self.CoBolita=="Azul" or self.CoBolita=="azul" or self.CoBolita=="AZUL":
                PDescuento = 50
        else: 
            PDescuento = 100
        VaPagar=self.VaCompra*(1-PDescuento/100)
        return "El cliente debe pagar: $ {}".format(VaPagar)
    def __str__(self):
        return "{}".format(self.Descuento())

VaCompra = float(input("Ingrese el valor de la compra: "))
CoBolita = input("Ingrese el color de la bolita: ")
Compra = Promocion(VaCompra,CoBolita)
print(Compra)