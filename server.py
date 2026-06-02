class Usuarios:
    def __init__(self ,username, userID, email, password, tipo_usuario):
        self.usuario = username
        self.id_usuario = userID
        self.correo = email
        self.contrasena = password
        self.tipo_usuario = tipo_usuario

    def mostrar_usuarios(self):
        print(f"Estan conectados: {self.usuario}n\{self.id_usuario}n\{self.correo}n\{self.contrasena}")


class salas:
    def _init_(self, id_salas, tamaño_sala):
        self.id_salas = id_salas
        self.tamaño_sala = tamaño_sala
        self.usuarios = []

    def mostrar_salas(self):
        print(f"Salas Disponibles: {self.id_salas}, {self.ttamaño_sala}")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

class sanciones:
    def _init_(self, id_usuario, tipo_sanciones, duracion):
        self.id_sanciones = id_usuario
        self.tipo_sanciones = tipo_sanciones
        self.duracion = duracion


class Roles:
    def _init_(self, nombre_rol, tipo_rol):
        self.nombre_rol = nombre_rol
        self.tipo_rol = tipo_rol


class reglas:
    def __init__(self, id_reglas, nombre_reglas, tipo_reglas):
        self.id_regla = id_reglas
        self.nombre_reglass = nombre_reglas
        self.tipo_de_reglas = tipo_reglas
        
        
usuario1 = Usuarios("Benjamin", 1, "araelanabalon@liceovvh.cl")
usuario2 = Usuarios("Juan", 2, "juandonoso@liceovvh.cl")
usuario3 = Usuarios("Jonathan", 3, "jonathanalquinta@liceovvh.cl")
usuario4 = Usuarios("Alexander", 4, "alexanderpino@liceovvh.cl")

