import tkinter as tk
from tkinter import messagebox

class TrianguloEquilatero(object):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return (self.lado ** 2) * (3 ** 0.5) / 4

    def perimetro(self):
        return self.lado * 3
    
    def altura(self):
        return (self.lado * (3 ** 0.5)) / 2
    
    def __str__(self):
        return "Lado: {} - Area: {:.2f} - Perimetro: {:.2f} - Altura: {:.2f}".format(
            self.lado, self.area(), self.perimetro(), self.altura())

# Función que se ejecutará al hacer clic en el botón "Calcular Propiedades"
def calcular_propiedades():
    try:
        lado = float(entry_lado.get())
        
        triangulo = TrianguloEquilatero(lado)
        result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        result_text.insert(tk.END, str(triangulo))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el lado.")

# Función que se ejecutará al hacer clic en el botón "Limpiar"
def limpiar_campos():
    entry_lado.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Propiedades de Triángulo Equilátero")
root.geometry("400x300")  # Ancho x Alto

# Crear y colocar widgets
tk.Label(root, text="Lado del Triángulo").pack(pady=5)
entry_lado = tk.Entry(root)
entry_lado.pack(pady=5)

tk.Button(root, text="Calcular Propiedades", command=calcular_propiedades).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

# Crear cuadro de texto para mostrar el resultado
result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

# Ejecutar el bucle principal
root.mainloop()
