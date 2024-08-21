import tkinter as tk
from tkinter import messagebox
from persona import Persona
from listaPersonas import ListaPersonas

class ventanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Paquetes swing")

        self.lista_personas = ListaPersonas()

        # Interfaz
        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.nombre_label = tk.Label(self.frame, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        self.apellidos_label = tk.Label(self.frame, text="Apellidos:")
        self.apellidos_label.grid(row=1, column=0, padx=5, pady=5)
        self.apellidos_entry = tk.Entry(self.frame)
        self.apellidos_entry.grid(row=1, column=1, padx=5, pady=5)

        self.direccion_label = tk.Label(self.frame, text="Dirección:")
        self.direccion_label.grid(row=2, column=0, padx=5, pady=5)
        self.direccion_entry = tk.Entry(self.frame)
        self.direccion_entry.grid(row=2, column=1, padx=5, pady=5)

        self.telefono_label = tk.Label(self.frame, text="Teléfono:")
        self.telefono_label.grid(row=3, column=0, padx=5, pady=5)
        self.telefono_entry = tk.Entry(self.frame)
        self.telefono_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Agregar Persona", command=self.agregar_persona)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.personas_listbox = tk.Listbox(self.frame)
        self.personas_listbox.grid(row=5, column=0, columnspan=2, pady=10, sticky="nsew")

        self.eliminar_button = tk.Button(self.frame, text="Eliminar Seleccionado", command=self.eliminar_seleccionado)
        self.eliminar_button.grid(row=6, column=0, pady=5)

        self.borrar_todo_button = tk.Button(self.frame, text="Borrar Todo", command=self.borrar_todo)
        self.borrar_todo_button.grid(row=6, column=1, pady=5)

        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(5, weight=1)

    def agregar_persona(self):
        nombre = self.nombre_entry.get()
        apellidos = self.apellidos_entry.get()
        direccion = self.direccion_entry.get()
        telefono = self.telefono_entry.get()

        if not (nombre and apellidos and direccion and telefono):
            messagebox.showwarning("Advertencia", "Todos los campos deben ser completados")
            return

        persona = Persona(nombre, apellidos, direccion, telefono)
        self.lista_personas.agregar_persona(persona)
        self.actualizar_lista()

        self.nombre_entry.delete(0, tk.END)
        self.apellidos_entry.delete(0, tk.END)
        self.direccion_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)

    def eliminar_seleccionado(self):
        selected_index = self.personas_listbox.curselection()
        if selected_index:
            self.lista_personas.eliminar_persona(selected_index[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una persona para eliminar")

    def borrar_todo(self):
        self.lista_personas.borrar_todas()
        self.actualizar_lista()

    def actualizar_lista(self):
        self.personas_listbox.delete(0, tk.END)
        for persona_str in self.lista_personas.obtener_personas():
            self.personas_listbox.insert(tk.END, persona_str)

def main():
    root = tk.Tk()
    app = ventanaPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
