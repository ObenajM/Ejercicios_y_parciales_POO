import tkinter as tk
from tkinter import messagebox
from Figuras import Cilindro, Esfera, Piramide

class VentanaCilindro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cilindro")
        self.geometry("220x200")
        self.create_widgets()

    def create_widgets(self):
        self.radio_label = tk.Label(self, text="Radio (cm):")
        self.radio_label.pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        self.altura_label = tk.Label(self, text="Altura (cm):")
        self.altura_label.pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate)
        self.calculate_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.pack()
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.pack()

    def calculate(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaEsfera(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Esfera")
        self.geometry("220x200")
        self.create_widgets()

    def create_widgets(self):
        self.radio_label = tk.Label(self, text="Radio (cm):")
        self.radio_label.pack()
        self.radio_entry = tk.Entry(self)
        self.radio_entry.pack()

        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate)
        self.calculate_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.pack()
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.pack()

    def calculate(self):
        try:
            radio = float(self.radio_entry.get())
            esfera = Esfera(radio)
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")


class VentanaPiramide(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pirámide")
        self.geometry("220x200")
        self.create_widgets()

    def create_widgets(self):
        self.base_label = tk.Label(self, text="Base (cm):")
        self.base_label.pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        self.altura_label = tk.Label(self, text="Altura (cm):")
        self.altura_label.pack()
        self.altura_entry = tk.Entry(self)
        self.altura_entry.pack()

        self.apotema_label = tk.Label(self, text="Apotema (cm):")
        self.apotema_label.pack()
        self.apotema_entry = tk.Entry(self)
        self.apotema_entry.pack()

        self.calculate_button = tk.Button(self, text="Calcular", command=self.calculate)
        self.calculate_button.pack()

        self.volumen_label = tk.Label(self, text="Volumen (cm3):")
        self.volumen_label.pack()
        self.superficie_label = tk.Label(self, text="Superficie (cm2):")
        self.superficie_label.pack()

    def calculate(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            piramide = Piramide(base, altura, apotema)
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")
