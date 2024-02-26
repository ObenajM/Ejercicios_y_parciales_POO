import math
Radio=float(input("Ingrese el radio del circulo: "))
Area,Circunferencia=round((math.pi)*pow(Radio,2),10),round(2*(math.pi)*Radio,10)
print("El area del circulo es {} y la circunferencia es {}".format(Area,Circunferencia))