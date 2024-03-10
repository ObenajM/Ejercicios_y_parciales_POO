import math
a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
c = float(input("Ingrese el coeficiente 'c': "))

discriminante = math.pow(b,2) - 4*a*c

if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    print("X_1 = ",raiz1," X_2 = ",raiz2) 
elif discriminante == 0:
    raiz = -b / (2*a)
    print("La única solución es: ",raiz) 
else:
    print("No hay soluciones reales")