from conexion import Conexion

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
        self.tipo_usuario = self.ROLES_DISPONIBLES.get(id_rol, "Jugador")
        self.nuevo_rol = self.ROLES_DISPONIBLES

    @staticmethod
    def listar():
        """
        Muestra todos los usuarios activos.

        Se utiliza un método estático porque
        no necesitamos crear un objeto para
        realizar una consulta general.
        """
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        SELECT
            id_usuario,
            username,
            email,
            id_rol
        FROM usuarios
        WHERE deleted = 0
        ORDER BY username ASC
        """

        cursor.execute(sql)
        Usuarios = cursor.fetchall()
        print("\n===== USUARIOS =====\n")
        for usuario in Usuarios:
            print(
                f"ID: {usuario[0]} | "
                f"Nombre: {usuario[1]} | "
                f"Correo: {usuario[2]}"
                f"Tipo de usuario: {usuario[3]}"
            )

        cursor.close()
        conexion.close()



    def agregar(self):
         """
        Inserta un nuevo usuario en
        la base de datos utilizando los
        atributos almacenados en el objeto.
         """
         conexion = Conexion.conectar()
         cursor = conexion.cursor()

         sql = """
            INSERT INTO usuarios
            (
                username,
                email,
                contrasena,
                id_rol,
                id_salas
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """

         valores = (
            self.usuario,
            self.id_usuario,
            self.correo,
            self.contrasena
            )

         cursor.execute(sql, valores)

            # Guarda los cambios realizados
         conexion.commit()
         print("\nUsuario agregado correctamente.")
         cursor.close()
         conexion.close()



    @staticmethod
    def actualizar():
        """
        Permite modificar el rol
        de un usuario.
        """

        id_usuario = input("Ingrese ID del usuario: ")
        nuevo_rol = input("Ingrese nuevo rol: ")
        conexion = Conexion.conectar()
        cursor = conexion.cursor()

        sql = """
        UPDATE usuarios
        SET curso = %s
        WHERE id_usuario = %s
        """

        valores = (nuevo_rol,id_usuario)
        cursor.execute(sql, valores)
        conexion.commit()
        print("\nRol actualizado correctamente.")

        cursor.close()
        conexion.close()




