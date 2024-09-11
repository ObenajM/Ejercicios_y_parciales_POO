import tkinter as tk
from tkinter import messagebox
from notas import Notas

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ingreso de Notas")
        
        # Dimensiones de la ventana más grandes
        self.root.geometry("400x500")  # Ancho x Alto
        
        # Crear un marco (Frame) para mejor organización del contenido
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill="both")
        
        self.notas = []
        
        # Espaciado más amplio y etiquetas más grandes
        self.entradas_notas = []
        for i in range(5):
            label = tk.Label(frame, text=f"Nota {i+1}:", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")
            entrada = tk.Entry(frame, font=("Arial", 12), width=10)
            entrada.grid(row=i, column=1, padx=10, pady=10)
            self.entradas_notas.append(entrada)
        
        # Botones más grandes
        self.boton_calcular = tk.Button(frame, text="Calcular", font=("Arial", 12), command=self.calcular, width=15)
        self.boton_calcular.grid(row=6, column=0, pady=20)
        
        self.boton_limpiar = tk.Button(frame, text="Limpiar Datos", font=("Arial", 12), command=self.limpiar, width=15)
        self.boton_limpiar.grid(row=6, column=1, pady=20)
        
        # Resultados con etiquetas más grandes y mejor espaciado
        self.resultado_promedio = tk.Label(frame, text="Promedio: ", font=("Arial", 12))
        self.resultado_promedio.grid(row=7, column=0, columnspan=2, pady=5)
        
        self.resultado_desviacion = tk.Label(frame, text="Desviación Estándar: ", font=("Arial", 12))
        self.resultado_desviacion.grid(row=8, column=0, columnspan=2, pady=5)
        
        self.resultado_mayor = tk.Label(frame, text="Mayor Nota: ", font=("Arial", 12))
        self.resultado_mayor.grid(row=9, column=0, columnspan=2, pady=5)
        
        self.resultado_menor = tk.Label(frame, text="Menor Nota: ", font=("Arial", 12))
        self.resultado_menor.grid(row=10, column=0, columnspan=2, pady=5)
    
    def calcular(self):
        try:
            self.notas = [float(entrada.get()) for entrada in self.entradas_notas]
            estadisticas = Notas(self.notas)

            promedio = estadisticas.calcular_promedio()
            desviacion_estandar = estadisticas.calcular_desviacion_estandar()
            mayor = estadisticas.obtener_mayor_nota()
            menor = estadisticas.obtener_menor_nota()

            self.resultado_promedio.config(text=f"Promedio: {promedio:.2f}")
            self.resultado_desviacion.config(text=f"Desviación Estándar: {desviacion_estandar:.2f}")
            self.resultado_mayor.config(text=f"Mayor Nota: {mayor:.2f}")
            self.resultado_menor.config(text=f"Menor Nota: {menor:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese números válidos.")

    def limpiar(self):
        # Limpiar las entradas de notas
        for entrada in self.entradas_notas:
            entrada.delete(0, tk.END)
        
        # Limpiar los resultados
        self.resultado_promedio.config(text="Promedio: ")
        self.resultado_desviacion.config(text="Desviación Estándar: ")
        self.resultado_mayor.config(text="Mayor Nota: ")
        self.resultado_menor.config(text="Menor Nota: ")
