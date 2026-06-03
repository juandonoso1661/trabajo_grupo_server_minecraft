class sanciones:
    def __init__(self, id_usuario, tipo_sanciones, duracion):
        self.id_usuario = id_usuario
        self.tipo_sanciones = tipo_sanciones
        self.duracion = duracion

    def verificar_regla(self, usuario, regla_infringida):
        if regla_infringida == "NO USAR HACKS":
            return sanciones(usuario.id_usuario,
            "Ban"
            "por 3 semanas"
            )
        
        elif regla_infringida == "NO INSULTOS EN EL CHAT":
            return sanciones(usuario.id_usuario,
            "Mute" 
            "por 2 dias"
            )
        
        elif regla_infringida == "NO HACER SPAM":
            return sanciones(usuario.id_usuario,
            "Mute"
            "por 1 dia"
            )
        
        elif regla_infringida == "NO SOBREEXPLOTAR MODS":
            return sanciones(usuario.id_usuario,
            "Ban"
            "por 3 dias"
            )

    def mostrar_sancion(self):
        print(
            f"Este usuario/os ha sido baneado:"
            f"ID usuario: {self.id_usuario}"
            f"Sanción: {self.tipo_sanciones}"
            f"Duración: {self.duracion}")
       