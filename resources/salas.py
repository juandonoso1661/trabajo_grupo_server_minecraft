from usuarios import usuario1, usuario2, usuario3, usuario4, usuario5

class Salas:
    def __init__(self, id_salas, tamaño_sala, tipo_sala):
        self.id_salas = id_salas
        self.tamaño_sala = tamaño_sala
        self.tipo_sala = tipo_sala
        self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_salas(self):
        print(f"Sala ID: {self.id_salas}\n"
              f"Tamaño sala: {self.tamaño_sala}\n"
              f"Tipo: {self.tipo_sala}" 
              )
        
        print("Usuarios conectados:")
        for usuario in self.usuarios:
            print(f"- {usuario.usuario}")

sala1 = Salas(1, 20, "Survival")

sala1.agregar_usuario(usuario1)
sala1.agregar_usuario(usuario2)
sala1.agregar_usuario(usuario3)
sala1.agregar_usuario(usuario4)
sala1.agregar_usuario(usuario5)

sala1.mostrar_salas()

