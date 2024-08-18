import tkinter as tk
from tkinter import messagebox

class NumMayor:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def mayor(self):
        if self.num1 > self.num2:
            return "{} es mayor que {}".format(self.num1, self.num2)
        elif self.num1 == self.num2:
            return "{} es igual a {}".format(self.num1, self.num2)
        else:
            return "{} es mayor que {}".format(self.num2, self.num1)
    
    def __str__(self):
        return "{}".format(self.mayor())

def determinar_mayor():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        num_mayor = NumMayor(num1, num2)
        result_text.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        result_text.insert(tk.END, str(num_mayor))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def limpiar_campos():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

root = tk.Tk()
root.title("Determinar Número Mayor")
root.geometry("400x300")  # Ancho x Alto

tk.Label(root, text="Primer Número").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Segundo Número").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

tk.Button(root, text="Determinar Mayor", command=determinar_mayor).pack(pady=10)
tk.Button(root, text="Limpiar Campos", command=limpiar_campos).pack(pady=10)

result_text = tk.Text(root, height=5, width=40)
result_text.pack(pady=20)

root.mainloop()
