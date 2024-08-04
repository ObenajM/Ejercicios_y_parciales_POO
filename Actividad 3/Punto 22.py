import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

    def comentario_salario(self):
        salario_mensual = self.calcular_salario_mensual()
        if salario_mensual > 450000:
            return "{}: ${:.2f}".format(self.nombre, salario_mensual)
        else:
            return self.nombre

def calcular_salario():
    try:
        nombre = entry_nombre.get()
        salario_por_hora = float(entry_salario_por_hora.get())
        horas_trabajadas = float(entry_horas_trabajadas.get())
        
        empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
        resultado = empleado.comentario_salario()
        
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para salario por hora y horas trabajadas.")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_salario_por_hora.delete(0, tk.END)
    entry_horas_trabajadas.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Calculadora de Salario de Empleado")
root.geometry("400x400")

tk.Label(root, text="Nombre del Empleado").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

tk.Label(root, text="Salario por Hora").pack(pady=5)
entry_salario_por_hora = tk.Entry(root)
entry_salario_por_hora.pack(pady=5)

tk.Label(root, text="Horas Trabajadas en el Mes").pack(pady=5)
entry_horas_trabajadas = tk.Entry(root)
entry_horas_trabajadas.pack(pady=5)

tk.Button(root, text="Calcular Salario", command=calcular_salario).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

root.mainloop()
