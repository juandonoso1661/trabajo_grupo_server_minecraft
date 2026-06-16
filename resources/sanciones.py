class Sanciones:
    def __init__(self, id_usuario, tipo_sanciones, duracion):
        self.id_usuario = id_usuario
        self.tipo_sanciones = tipo_sanciones
        self.duracion = duracion

    def verificar_regla(self, usuario, regla_infringida):
        if regla_infringida == "NO USAR HACKS":
            return Sanciones(usuario.id_usuario,
            "Ban",
            "por 3 semanas"
            )
        
        elif regla_infringida == "NO INSULTOS EN EL CHAT":
            return Sanciones(usuario.id_usuario,
            "Mute", 
            "por 2 dias"
            )
        
        elif regla_infringida == "NO HACER SPAM":
            return Sanciones(usuario.id_usuario,
            "Mute",
            "por 1 dia"
            )
        
        elif regla_infringida == "NO SOBREEXPLOTAR MODS":
            return Sanciones(usuario.id_usuario,
            "Ban",
            "por 3 dias"
            )
        return None

    def mostrar_sancion(self):
        print(
            f"Este usuario/os ha sido baneado\n:"
            f"ID usuario: {self.id_usuario}\n"
            f"Sanción: {self.tipo_sanciones}\n"
            f"Duración: {self.duracion}"
            )
        

# Importamos la clase Conexion para la base de datos
from resources.conexion import Conexion

class Sanciones:
    """
    Representa la gestión de sanciones en el servidor de Minecraft.
    """

    @staticmethod
    def ver_sanciones_usuario():
        """
        Muestra el historial de sanciones buscando por el username del jugador.
        """
        username_buscar = input("\nIngrese el Username del jugador a consultar sanciones: ").strip()
        
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT u.username, s.tipo_sanciones, s.duracion, s.created_at
        FROM sanciones s
        INNER JOIN usuarios u ON s.id_usuario = u.id_usuario
        WHERE u.username = %s AND s.deleted = 0 AND u.deleted = 0
        ORDER BY s.created_at DESC
        """
        cursor.execute(sql, (username_buscar,))
        resultados = cursor.fetchall()

        print(f"\n===== HISTORIAL DE SANCIONES: {username_buscar.upper()} =====")
        if not resultados:
            print("El jugador no registra ninguna sanción activa en el sistema.")
        else:
            for fila in resultados:
                print(f"Infracción: {fila[1]} | Duración: {fila[2]} | Aplicada el: {fila[3]}")

        cursor.close()
        conexion.close()