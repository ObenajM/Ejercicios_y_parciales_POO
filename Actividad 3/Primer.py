import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Interfaz Gráfica")

# Función que se ejecutará al hacer clic en el botón
def on_button_click():
    label.config(text="¡Botón presionado!")

# Crear un botón
button = tk.Button(root, text="Haz clic en mí", command=on_button_click)
button.pack(pady=20)

# Crear una etiqueta para mostrar un mensaje
label = tk.Label(root, text="Presiona el botón")
label.pack(pady=20)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
