class Usuario:
    def __init__(self ,username, userID, email):
        self.usuario = username
        self.id_usuario = userID
        self.correo = email

    def mostrar_usuarios(self):
        print(f"Estan conectados: ")

class Server:
    def __init__(self, nombre_server):
        self.servername = nombre_server
        self.usuarios = []

