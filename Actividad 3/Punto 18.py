import tkinter as tk
from tkinter import messagebox

class Empleado(object):
    def __init__(self, cod_empleado, nombre, num_horas_tra, val_hora, porc_retencion):
        self.cod_empleado = cod_empleado
        self.nombre = nombre
        self.num_horas_tra = num_horas_tra
        self.val_hora = val_hora
        self.porc_retencion = porc_retencion
    
    def salario_bruto(self):
        return self.num_horas_tra * self.val_hora
    
    def salario_neto(self):
        return self.salario_bruto() * (1 - self.porc_retencion / 100)
    
    def __str__(self):
        return "Código: {} - Nombre: {} - Salario Bruto: ${:.2f} - Salario Neto: ${:.2f}".format(
            self.cod_empleado, self.nombre, self.salario_bruto(), self.salario_neto())

def calcular_salario():
    try:
        cod_empleado = entry_cod_empleado.get()
        nombre = entry_nombre.get()
        num_horas_tra = float(entry_num_horas_tra.get())
        val_hora = float(entry_val_hora.get())
        porc_retencion = float(entry_porc_retencion.get())
        
        empleado = Empleado(cod_empleado, nombre, num_horas_tra, val_hora, porc_retencion)
        result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        result_text.insert(tk.END, str(empleado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para horas trabajadas, valor de la hora y porcentaje de retención.")

def limpiar_campos():
    entry_cod_empleado.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_num_horas_tra.delete(0, tk.END)
    entry_val_hora.delete(0, tk.END)
    entry_porc_retencion.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Calculadora de Salario de Empleado")
root.geometry("400x550")  # Ancho x Alto

tk.Label(root, text="Código del Empleado").pack(pady=5)
entry_cod_empleado = tk.Entry(root)
entry_cod_empleado.pack(pady=5)

tk.Label(root, text="Nombre del Empleado").pack(pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.pack(pady=5)

tk.Label(root, text="Número de Horas Trabajadas").pack(pady=5)
entry_num_horas_tra = tk.Entry(root)
entry_num_horas_tra.pack(pady=5)

tk.Label(root, text="Valor de la Hora").pack(pady=5)
entry_val_hora = tk.Entry(root)
entry_val_hora.pack(pady=5)

tk.Label(root, text="Porcentaje de Retención").pack(pady=5)
entry_porc_retencion = tk.Entry(root)
entry_porc_retencion.pack(pady=5)

tk.Button(root, text="Calcular Salario", command=calcular_salario).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

root.mainloop()
