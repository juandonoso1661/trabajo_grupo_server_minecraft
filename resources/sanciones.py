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
from conexion import Conexion

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
    @classmethod
    def agregar_sancion(cls):
        print("\n===================================")
        print("       APLICAR NUEVA SANCIÓN       ")
        print("===================================")
        
        # 1. Importamos localmente Usuarios para mostrar la lista y evitar importación circular
        from usuarios import Usuarios
        print("Selecciona el ID del usuario al que deseas sancionar:")
        Usuarios.ver_usuarios_detallados()
        
        id_usuario = input("\nIngrese el ID del usuario (id_usuario): ").strip()
        if not id_usuario:
            print("Operación cancelada. El ID de usuario es obligatorio.")
            return

        # 2. Menú para elegir el tipo de sanción basándonos en tus INSERTS de SQL
        print("\n--- TIPOS DE SANCIONES DISPONIBLES ---")
        print("1. Baneo de chat")
        print("2. Advertencia")
        print("3. Baneo temporal")
        print("4. Baneo permanente")
        opc_sancion = input("Seleccione el número de sanción a aplicar: ").strip()

        # Mapeamos la opción del menú al texto real que irá a la base de datos
        tipo_sancion = ""
        if opc_sancion == "1":
            tipo_sancion = "baneo de chat"
        elif opc_sancion == "2":
            tipo_sancion = "advertencia"
        elif opc_sancion == "3":
            tipo_sancion = "baneo temporal"
        elif opc_sancion == "4":
            tipo_sancion = "baneo permanente"
        else:
            print("[Error] Opción de sanción no válida. Operación cancelada.")
            return

        # 3. Solicitar la duración de la sanción (Formato TIME de SQL: HH:MM:SS)
        # Nota: Si es permanente, puedes dejarlo en 00:00:00 o lo que gustes
        duracion = input("Ingrese la duración (Ejemplo: 02:00:00 para 2 horas, o presione Enter para dejar vacío): ").strip()
        if duracion == "":
            duracion = None

        # 4. Guardar el registro en la Base de Datos
        try:
            import mysql.connector
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",        
                password="1234",
                database="pixelserver"
            )
            cursor = conexion.cursor()

            # Sentencia SQL usando las columnas exactas de tu tabla 'sanciones'
            sql = """
                INSERT INTO sanciones (tipo_sanciones, duracion, id_usuario, created_by) 
                VALUES (%s, %s, %s, %s)
            """
            valores = (tipo_sancion, duracion, id_usuario, "Consola_Admin")
            
            cursor.execute(sql, valores)
            conexion.commit() # Confirmamos la inserción
            
            print(f"\n[Éxito] Sanción de '{tipo_sancion}' aplicada correctamente al usuario con ID {id_usuario}.")
            
            cursor.close()
            conexion.close()

        except Exception as e:
            print(f"\n[Error] No se pudo registrar la sanción en la base de datos: {e}")