class Usuarios:
    ROLES_DISPONIBLES = {
        1: "Jugador",
        2: "Hacker",
        3: "Administrador"
    }

    def __init__(self ,username, userID, email, password, id_rol):
        self.usuario = username
        self.id_usuario = userID
        self.correo = email
        self.contrasena = password
        self.tipo_usuario = self.ROLES_DISPONIBLES.get(id_rol, "Invitado")

    def cambiar_rol_por_id(self, id_rol):
        if id_rol in self.ROLES_DISPONIBLES:
            self.tipo_usuario = self.ROLES_DISPONIBLES[id_rol]
            print(f"¡Rol de {self.usuario} actualizado con éxito a: {self.tipo_usuario}!")
        else:
            print("Error: El ID de rol introducido no es válido.")

    def mostrar_usuarios(self):
        print(
            f"Usuario: {self.usuario}\n"
            f"ID: {self.id_usuario}\n"
            f"E-mail: {self.correo}\n"
            f"Rol: {self.tipo_usuario}"
        )

"""Datos de jugadores"""
usuario1 = Usuarios("Benjamin", 1, "araelanabalon@liceovvh.cl", "Benja123", 1)
usuario2 = Usuarios("Juan", 2, "juandonoso@liceovvh.cl", "Juan456", 1)
usuario3 = Usuarios("Jonathan", 3, "jonathanalquinta@liceovvh.cl", "jonathan222", 2)
usuario4 = Usuarios("Alexander", 4, "alexanderpino@liceovvh.cl", "ale566", 2)
usuario5 = Usuarios("Luis", 5, "luisecheverria@liceovvh.cl", "Luis890", 3)




