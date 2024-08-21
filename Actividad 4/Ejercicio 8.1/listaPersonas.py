from persona import Persona

class ListaPersonas:
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

    def eliminar_persona(self, index):
        if 0 <= index < len(self.personas):
            del self.personas[index]

    def borrar_todas(self):
        self.personas.clear()

    def obtener_personas(self):
        return [str(persona) for persona in self.personas]
