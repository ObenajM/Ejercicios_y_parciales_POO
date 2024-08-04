import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def clasificar_triangulo(self):
        if ((self.base == self.altura) and 
            (self.base == self.calcular_hipotenusa()) and 
            (self.altura == self.calcular_hipotenusa())):
            return "Es un triángulo equilátero"
        elif ((self.base != self.altura) and 
              (self.base != self.calcular_hipotenusa()) and 
              (self.altura != self.calcular_hipotenusa())):
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"

def calcular_circulo():
    try:
        radio = float(entry_radio.get())
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        perimetro = circulo.calcular_perimetro()
        result_text_circulo.config(state=tk.NORMAL)
        result_text_circulo.delete(1.0, tk.END)
        result_text_circulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_text_circulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el radio.")

def calcular_cuadrado():
    try:
        lado = float(entry_lado_cuadrado.get())
        cuadrado = Cuadrado(lado)
        area = cuadrado.calcular_area()
        perimetro = cuadrado.calcular_perimetro()
        result_text_cuadrado.config(state=tk.NORMAL)
        result_text_cuadrado.delete(1.0, tk.END)
        result_text_cuadrado.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_text_cuadrado.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el lado.")

def calcular_rectangulo():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.calcular_area()
        perimetro = rectangulo.calcular_perimetro()
        result_text_rectangulo.config(state=tk.NORMAL)
        result_text_rectangulo.delete(1.0, tk.END)
        result_text_rectangulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_text_rectangulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para la base y la altura.")

def calcular_triangulo():
    try:
        base = float(entry_base_triangulo.get())
        altura = float(entry_altura_triangulo.get())
        triangulo = TrianguloRectangulo(base, altura)
        area = triangulo.calcular_area()
        perimetro = triangulo.calcular_perimetro()
        clasificacion = triangulo.clasificar_triangulo()
        result_text_triangulo.config(state=tk.NORMAL)
        result_text_triangulo.delete(1.0, tk.END)
        result_text_triangulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}\nClasificación: {clasificacion}")
        result_text_triangulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para la base y la altura.")

def limpiar_campos():
    entry_radio.delete(0, tk.END)
    entry_lado_cuadrado.delete(0, tk.END)
    entry_base_rectangulo.delete(0, tk.END)
    entry_altura_rectangulo.delete(0, tk.END)
    entry_base_triangulo.delete(0, tk.END)
    entry_altura_triangulo.delete(0, tk.END)
    result_text_circulo.config(state=tk.NORMAL)
    result_text_circulo.delete(1.0, tk.END)
    result_text_circulo.config(state=tk.DISABLED)
    result_text_cuadrado.config(state=tk.NORMAL)
    result_text_cuadrado.delete(1.0, tk.END)
    result_text_cuadrado.config(state=tk.DISABLED)
    result_text_rectangulo.config(state=tk.NORMAL)
    result_text_rectangulo.delete(1.0, tk.END)
    result_text_rectangulo.config(state=tk.DISABLED)
    result_text_triangulo.config(state=tk.NORMAL)
    result_text_triangulo.delete(1.0, tk.END)
    result_text_triangulo.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")
root.geometry("600x450")

# Circulo
frame_circulo = tk.LabelFrame(root, text="Círculo", padx=10, pady=10)
frame_circulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame_circulo, text="Radio").grid(row=0, column=0)
entry_radio = tk.Entry(frame_circulo)
entry_radio.grid(row=0, column=1)
tk.Button(frame_circulo, text="Calcular", command=calcular_circulo).grid(row=1, column=0, columnspan=2)
result_text_circulo = tk.Text(frame_circulo, height=5, width=30, state=tk.DISABLED)
result_text_circulo.grid(row=2, column=0, columnspan=2)

# Cuadrado
frame_cuadrado = tk.LabelFrame(root, text="Cuadrado", padx=10, pady=10)
frame_cuadrado.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
tk.Label(frame_cuadrado, text="Lado").grid(row=0, column=0)
entry_lado_cuadrado = tk.Entry(frame_cuadrado)
entry_lado_cuadrado.grid(row=0, column=1)
tk.Button(frame_cuadrado, text="Calcular", command=calcular_cuadrado).grid(row=1, column=0, columnspan=2)
result_text_cuadrado = tk.Text(frame_cuadrado, height=5, width=30, state=tk.DISABLED)
result_text_cuadrado.grid(row=2, column=0, columnspan=2)

# Rectangulo
frame_rectangulo = tk.LabelFrame(root, text="Rectángulo", padx=10, pady=10)
frame_rectangulo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame_rectangulo, text="Base").grid(row=0, column=0)
entry_base_rectangulo = tk.Entry(frame_rectangulo)
entry_base_rectangulo.grid(row=0, column=1)
tk.Label(frame_rectangulo, text="Altura").grid(row=1, column=0)
entry_altura_rectangulo = tk.Entry(frame_rectangulo)
entry_altura_rectangulo.grid(row=1, column=1)
tk.Button(frame_rectangulo, text="Calcular", command=calcular_rectangulo).grid(row=2, column=0, columnspan=2)
result_text_rectangulo = tk.Text(frame_rectangulo, height=5, width=30, state=tk.DISABLED)
result_text_rectangulo.grid(row=3, column=0, columnspan=2)

# Triangulo Rectangulo
frame_triangulo = tk.LabelFrame(root, text="Triángulo Rectángulo", padx=10, pady=10)
frame_triangulo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
tk.Label(frame_triangulo, text="Base").grid(row=0, column=0)
entry_base_triangulo = tk.Entry(frame_triangulo)
entry_base_triangulo.grid(row=0, column=1)
tk.Label(frame_triangulo, text="Altura").grid(row=1, column=0)
entry_altura_triangulo = tk.Entry(frame_triangulo)
entry_altura_triangulo.grid(row=1, column=1)
tk.Button(frame_triangulo, text="Calcular", command=calcular_triangulo).grid(row=2, column=0, columnspan=2)
result_text_triangulo = tk.Text(frame_triangulo, height=5, width=30, state=tk.DISABLED)
result_text_triangulo.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Limpiar Campos", command=limpiar_campos).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
