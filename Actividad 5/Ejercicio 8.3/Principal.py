import tkinter as tk
from Ventanas import VentanaCilindro, VentanaEsfera, VentanaPiramide

class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras")
        self.geometry("220x100")
        self.create_widgets()

    def create_widgets(self):
        self.cilindro_button = tk.Button(self, text="Cilindro", command=self.open_cilindro)
        self.cilindro_button.pack(pady=10, padx=10, side=tk.LEFT)

        self.esfera_button = tk.Button(self, text="Esfera", command=self.open_esfera)
        self.esfera_button.pack(pady=10, padx=10, side=tk.LEFT)

        self.piramide_button = tk.Button(self, text="Pirámide", command=self.open_piramide)
        self.piramide_button.pack(pady=10, padx=10, side=tk.LEFT)

    def open_cilindro(self):
        ventana_cilindro = VentanaCilindro()
        ventana_cilindro.mainloop()

    def open_esfera(self):
        ventana_esfera = VentanaEsfera()
        ventana_esfera.mainloop()

    def open_piramide(self):
        ventana_piramide = VentanaPiramide()
        ventana_piramide.mainloop()

if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
