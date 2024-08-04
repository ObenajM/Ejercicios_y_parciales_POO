import tkinter as tk
from tkinter import messagebox

class PagoMatricula:
    def __init__(self, Ni, Nombres, Patrimonio, Estrato):
        self.Ni = Ni
        self.Nombres = Nombres
        self.Patrimonio = Patrimonio
        self.Estrato = Estrato
    
    def Matricula(self):
        PagMat = 50000
        if self.Patrimonio > 2000000 and self.Estrato > 3:
            PagMat = PagMat + 0.03 * self.Patrimonio
        return "El estudiante con número de inscripción {} y nombres {} debe pagar ${:.2f}".format(
            self.Ni, self.Nombres, PagMat)
    
    def __str__(self):
        return "{}".format(self.Matricula())

def calcular_matricula():
    try:
        Ni = entry_ni.get()
        Nombres = entry_nombres.get()
        Patrimonio = float(entry_patrimonio.get())
        Estrato = int(entry_estrato.get())
        
        estudiante = PagoMatricula(Ni, Nombres, Patrimonio, Estrato)
        result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        result_text.insert(tk.END, str(estudiante))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para Patrimonio y Estrato.")

def limpiar_campos():
    entry_ni.delete(0, tk.END)
    entry_nombres.delete(0, tk.END)
    entry_patrimonio.delete(0, tk.END)
    entry_estrato.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Cálculo de Pago de Matrícula")
root.geometry("400x450")  # Ancho x Alto

tk.Label(root, text="Número de Inscripción").pack(pady=5)
entry_ni = tk.Entry(root)
entry_ni.pack(pady=5)

tk.Label(root, text="Nombres del Estudiante").pack(pady=5)
entry_nombres = tk.Entry(root)
entry_nombres.pack(pady=5)

tk.Label(root, text="Patrimonio del Estudiante").pack(pady=5)
entry_patrimonio = tk.Entry(root)
entry_patrimonio.pack(pady=5)

tk.Label(root, text="Estrato del Estudiante").pack(pady=5)
entry_estrato = tk.Entry(root)
entry_estrato.pack(pady=5)

tk.Button(root, text="Calcular Matrícula", command=calcular_matricula).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

root.mainloop()
