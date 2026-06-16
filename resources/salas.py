from usuarios import usuario1, usuario2, usuario3, usuario4, usuario5

class Salas:
    def __init__(self, id_salas, tamaño_sala, tipo_sala):
        self.id_salas = id_salas
        self.tamaño_sala = tamaño_sala
        self.tipo_sala = tipo_sala
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)


