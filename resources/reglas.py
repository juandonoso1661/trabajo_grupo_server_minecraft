class Reglas:
    def __init__(self, id_reglas, nombre_reglas, tipo_reglas):
        self.id_regla = id_reglas
        self.nombre_reglas = nombre_reglas
        self.tipo_de_reglas = tipo_reglas

    def mostrar_regla(self):
        print(f"ID: {self.id_regla}")
        print(f"Nombre: {self.nombre_reglas}")
        print(f"Tipo de regla: {self.tipo_de_reglas}")

regla1 = Reglas(1, "NO USAR HACKS", "seguridad")
regla2 = Reglas(2, "NO INSULTOS EN EL CHAT", "convivencia")
regla3 = Reglas(3, "NO SOBREEXPLOTAR MODS", "seguridad")
regla4 = Reglas(4, "NO HACER SPAM", "chat")


from conexion import Conexion

class Reglas:
    """
    Representa la gestión de reglas del servidor de Minecraft.
    """

    @staticmethod
    def mostrar_reglas_server():
        """
        Muestra todas las reglas activas del servidor de forma general.
        """
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        
        sql = """
        SELECT 
            id_reglas,
            nombre_reglas,
            tipo_reglas
        FROM reglas
        WHERE deleted = 0
        ORDER BY id_reglas ASC
        """

        cursor.execute(sql)
        lista_reglas = cursor.fetchall()

        print("\n===== REGLAS DEL SERVIDOR PIXELSERVER =====")
        if not lista_reglas:
            print("No hay reglas registradas en el servidor actualmente.")
        else:
            for regla in lista_reglas:
                print(
                    f"ID: {regla[0]} | "
                    f"Norma: {regla[1]} | "
                    f"Categoría: {regla[2]}"
                )
        
        cursor.close()
        conexion.close()