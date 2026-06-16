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
    # 1. LISTAR JUGADORES (Con contador del 1 al total)
    # ===================================================
    @staticmethod
    def listar():
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        
        sql = """
        SELECT u.id_usuario, u.username, u.email, IFNULL(r.tipo_rol, 'Sin Rol') AS rol
        FROM usuarios u LEFT JOIN rol r ON u.id_rol = r.id_rol
        WHERE u.deleted = 0 
        ORDER BY u.id_usuario ASC
        """
        cursor.execute(sql)
        lista_usuarios = cursor.fetchall()
        
        print("\n===== JUGADORES DEL SERVIDOR =====")
        
       
        contador = 1
        
        for usuario in lista_usuarios:
            
            print(f"{contador}.ID: {usuario[0]} | Usuario: {usuario[1]} | Correo: {usuario[2]} | Rol: {usuario[3]}")
            
            
            contador += 1
            
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
        INSERT INTO usuarios (username, email, contraseña, id_rol, id_salas, created_by) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        id_sala_final = self.id_salas if self.id_salas else None

        valores = (self.username, self.email, self.password, self.id_rol, id_sala_final, self.created_by)
    
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
    # 6. BUSCAR SALAS POR CAPACIDAD
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

# ===================================================
    # MODIFICAR USUARIO (Campos Dinámicos)
    # ===================================================
    # ===================================================
    # MODIFICAR USUARIO (Versión de Diagnóstico)
    # ===================================================
    @staticmethod
    def actualizar():
        print("\n--- MODIFICAR DATOS DE JUGADOR ---")
        id_usuario = input("Ingrese ID del usuario a modificar: ").strip()
        
        conexion = Conexion.conectar()
        cursor = conexion.cursor()
        
        
        try:
            cursor.execute("DESCRIBE usuarios")
            columnas_reales = [fila[0] for fila in cursor.fetchall()]
            print(f"\n[DIAGNÓSTICO] Columnas encontradas en tu BD: {columnas_reales}")
        except Exception as e:
            print(f"[DIAGNÓSTICO] No se pudo leer la estructura: {e}")

        
        sql_buscar = "SELECT username, email, id_rol, id_salas FROM usuarios WHERE id_usuario = %s AND deleted = 0"
        cursor.execute(sql_buscar, (id_usuario,))
        usuario_actual = cursor.fetchone()
        
        if not usuario_actual:
            print("\n[Error] No se encontró ningún usuario activo con ese ID.")
            cursor.close()
            conexion.close()
            return

        username_act, email_act, id_rol_act, id_sala_act = usuario_actual
        
        print(f"\nDatos actuales -> Username: {username_act} | Email: {email_act}")
        print("(Presione [Enter] para mantener el valor actual)\n")
        
        nuevo_username = input(f"Nuevo Username [{username_act}]: ").strip()
        nuevo_email = input(f"Nuevo Correo [{email_act}]: ").strip()
        nueva_contra = input("Nueva Contraseña [Omitir]: ").strip()
        
        Usuarios.listar_roles()
        nuevo_rol = input(f"Nuevo ID de Rol [{id_rol_act}]: ").strip()
        nuevo_sala = input(f"Nuevo ID de Sala [{id_sala_act}] (Escribe 'NULL' para quitar): ").strip()

        
        final_username = nuevo_username if nuevo_username != "" else username_act
        final_email = nuevo_email if nuevo_email != "" else email_act
        final_rol = nuevo_rol if nuevo_rol != "" else id_rol_act
        
        if nuevo_sala == "":
            final_sala = id_sala_act
        elif nuevo_sala.upper() == "NULL":
            final_sala = None
        else:
            final_sala = nuevo_sala

        
        nombre_columna_password = "contraseña" if "contraseña" in columnas_reales else "contrasena"

        if nueva_contra != "":
            sql_update = f"""
            UPDATE usuarios 
            SET username = %s, email = %s, {nombre_columna_password} = %s, id_rol = %s, id_salas = %s 
            WHERE id_usuario = %s
            """
            valores = (final_username, final_email, nueva_contra, final_rol, final_sala, id_usuario)
        else:
            sql_update = """
            UPDATE usuarios 
            SET username = %s, email = %s, id_rol = %s, id_salas = %s 
            WHERE id_usuario = %s
            """
            valores = (final_username, final_email, final_rol, final_sala, id_usuario)

        
        try:
            cursor.execute(sql_update, valores)
            conexion.commit()
            print(f"\n ¡Usuario con ID {id_usuario} actualizado correctamente!")
        except Exception as e:
            print(f"\n[Error] No se pudo actualizar el usuario: {e}")
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()
    @classmethod
    def eliminar(cls):
        print("\n===================================")
        print("        ELIMINAR JUGADOR           ")
        print("===================================")
        
        cls.ver_usuarios_detallados()
        
        id_user = input("\nIngrese el ID del usuario que desea eliminar (id_usuario): ").strip()
        
        if not id_user:
            print("Operación cancelada. El ID no puede estar vacío.")
            return

        confirmacion = input(f"¿Está seguro de que desea eliminar al usuario con ID {id_user}? (s/n): ").strip().lower()
        
        if confirmacion == 's':
            try:
                import mysql.connector 
                conexion = mysql.connector.connect(
                    host="localhost",
                    user="root",        
                    password="1234",
                    database="pixelserver"
                )
                cursor = conexion.cursor()
                
                sql = "UPDATE usuarios SET deleted = 1, update_by = 'Consola_Admin' WHERE id_usuario = %s AND deleted = 0"
                cursor.execute(sql, (id_user,))
                
                if cursor.rowcount > 0:
                    conexion.commit()  
                    print(f"\n[Éxito] El usuario con ID {id_user} ha sido eliminado correctamente del sistema.")
                else:
                    print(f"\n[Aviso] No se encontró ningún usuario activo con el ID {id_user}.")
                
                cursor.close()
                conexion.close()
                
            except Exception as e:
                print(f"\n[Error] No se pudo procesar la eliminación: {e}")
        else:
            print("\nOperación cancelada. El usuario no sufrió cambios.")