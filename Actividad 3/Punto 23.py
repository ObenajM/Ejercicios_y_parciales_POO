import tkinter as tk
from tkinter import messagebox
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_discriminante(self):
        return math.pow(self.b, 2) - 4 * self.a * self.c

    def calcular_raices(self):
        discriminante = self.calcular_discriminante()
        if discriminante > 0:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"X_1 = {raiz1}, X_2 = {raiz2}"
        elif discriminante == 0:
            if self.b == 0:
                raiz = 0
            else:
                raiz = -self.b / (2 * self.a)
            return f"La única solución es: {raiz}"
        else:
            return "No hay solución en los números reales"

def calcular_raices():
    try:
        A = float(entry_a.get())
        B = float(entry_b.get())
        C = float(entry_c.get())
        
        ecuacion = EcuacionCuadratica(A, B, C)
        resultado = ecuacion.calcular_raices()
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para los coeficientes.")

def limpiar_campos():
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Calculadora de Ecuación Cuadrática")
root.geometry("400x400")

tk.Label(root, text="Coeficiente A").pack(pady=5)
entry_a = tk.Entry(root)
entry_a.pack(pady=5)

tk.Label(root, text="Coeficiente B").pack(pady=5)
entry_b = tk.Entry(root)
entry_b.pack(pady=5)

tk.Label(root, text="Coeficiente C").pack(pady=5)
entry_c = tk.Entry(root)
entry_c.pack(pady=5)

tk.Button(root, text="Calcular Raíces", command=calcular_raices).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

root.mainloop()
