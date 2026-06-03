class salas:
    def _init_(self, id_salas, tamaño_sala):
        self.id_salas = id_salas
        self.tamaño_sala = tamaño_sala
        self.usuarios = []

    def mostrar_salas(self):
        print(f"Salas Disponibles:\n{self.id_salas}, \n{self.tamaño_sala}")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        