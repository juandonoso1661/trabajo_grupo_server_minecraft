from conexion import Conexion

class Usuarios:
    """
    Representa la gestión de usuarios, roles y salas del servidor.
    """

    def __init__(self, username=None, email=None, contrasena=None, id_rol=None, id_salas=None, created_by="Consola_Admin"):
        self.username = username
        self.email = email
        self.password = contrasena  
        self.id_rol = id_rol
        self.id_salas = id_salas
        self.created_by = created_by

    # ===================================================
    # 1. LISTAR JUGADORES (Opción 1 del Menú)
    # ===================================================
    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """
        SELECT u.id_usuario, u.username, u.email, IFNULL(r.tipo_rol, 'Sin Rol') AS rol
        FROM usuarios u LEFT JOIN rol r ON u.id_rol = r.id_rol
        WHERE u.deleted = 0 ORDER BY u.username ASC
        """
        cursor.execute(sql)
        lista_usuarios = cursor.fetchall()
        print("\n===== JUGADORES DEL SERVIDOR =====\n")
        for usuario in lista_usuarios:
            print(f"ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]} | Rol: {usuario[3]}")
        cursor.close()
        conexion.close()

    ver_usuarios_detallados = listar

    # ===================================================
    # 3. VER CANTIDAD POR ROL (Opción 3 del Menú)
    # ===================================================
    @staticmethod
    def ver_cantidad_por_rol():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """
        SELECT r.tipo_rol, COUNT(u.id_usuario) AS total_jugadores
        FROM usuarios u INNER JOIN rol r ON u.id_rol = r.id_rol
        WHERE u.deleted = 0 AND r.deleted = 0
        GROUP BY r.id_rol, r.tipo_rol ORDER BY total_jugadores DESC
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        print("\n===== CANTIDAD DE JUGADORES POR ROL =====")
        for fila in resultados:
            print(f"Rol: {fila[0]} → Cantidad: {fila[1]} usuarios")
        cursor.close()
        conexion.close()

    # ===================================================
    # 4. LISTAR ROLES (Opción 4 del Menú)
    # ===================================================
    @staticmethod
    def listar_roles():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "SELECT id_rol, tipo_rol FROM rol WHERE deleted = 0 ORDER BY id_rol ASC"
        cursor.execute(sql)
        lista_roles = cursor.fetchall()
        print("\n===== ROLES DISPONIBLES EN EL SERVIDOR =====\n")
        for rol in lista_roles:
            print(f"ID: {rol[0]} | Rol: {rol[1]}")
        cursor.close()
        conexion.close()

    # ===================================================
    # 2. AGREGAR / GUARDAR JUGADOR (Opción 2 del Menú)
    # ===================================================
    def agregar(self):
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = """
        INSERT INTO usuarios (username, email, contrasena, id_rol, id_salas, created_by) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (self.username, self.email, self.password, self.id_rol, self.id_salas, self.created_by)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"\nUsuario '{self.username}' agregado correctamente.")
        cursor.close()
        conexion.close()

    guardar = agregar

    # ===================================================
    # MODIFICAR USUARIO
    # ===================================================
    @staticmethod
    def actualizar():
        id_usuario = input("Ingrese ID del usuario a modificar: ").strip()
        nuevo_rol = input("Ingrese la ID del nuevo rol (1: Casual, 2: Cheater, 3: Admin): ").strip()
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE usuarios SET id_rol = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_rol, id_usuario))
        conexion.commit()
        print("\nRol del usuario actualizado correctamente.")
        cursor.close()
        conexion.close()

    # ===================================================
    # 6. BUSCAR SALAS POR CAPACIDAD (BETWEEN)
    # ===================================================
    @staticmethod
    def buscar_salas_por_capacidad():
        min_capacidad = int(input("Capacidad mínima de la sala (ej. 10): "))
        max_capacidad = int(input("Capacidad máxima de la sala (ej. 30): "))

        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT id_salas, tamaño_salas 
        FROM salas 
        WHERE tamaño_salas BETWEEN %s AND %s AND deleted = 0 
        ORDER BY tamaño_salas DESC
        """
        cursor.execute(sql, (min_capacidad, max_capacidad))
        resultados = cursor.fetchall()

        print("\n===== SALAS DISPONIBLES EN EL RANGO =====")
        if not resultados:
            print("No se encontraron salas registradas con ese tamaño.")
        else:
            for fila in resultados:
                print(f"Sala ID: {fila[0]} | Espacio Máximo: {fila[1]} jugadores")

        cursor.close()
        conexion.close()



