# Importamos las clases desde sus respectivos archivos independientes
from usuarios import Usuarios
from sanciones import Sanciones
from reglas import Reglas  # <- Agregamos la importación del nuevo archivo

# =====================================
# MENÚ PRINCIPAL
# =====================================

while True:
    print("\n===================================")
    print("   SISTEMA SERVIDOR DE MINECRAFT   ")
    print("===================================")
    print("1. Lista de usuarios detallada")
    print("2. Agregar nuevo usuario")
    print("3. Ver cantidad de jugadores por rol")
    print("4. Ver lista de roles disponibles")
    print("5. Consultar sanciones de un usuario")
    print("6. Buscar salas por capacidad")
    print("7. Mostrar reglas de server")
    print("8. Modificar usuario por completo")
    print("9. Eliminar usuario de forma permanente")
    print("10. Aplicar sanción a un usuario")
    print("0. Salir")
    print("===================================")

    opcion = input("Selecciona una opción: ").strip()

    # 1. Lista de usuarios
    if opcion == "1":
        Usuarios.ver_usuarios_detallados()

    # 2. Agregar usuario
    elif opcion == "2":
        print("\n--- REGISTRAR NUEVO JUGADOR ---")
        username = input("Username de Minecraft: ").strip()
        email = input("Correo electrónico: ").strip()
        contrasena = input("Contraseña: ").strip()
        
        Usuarios.listar_roles()
        id_rol = input("Ingrese el ID del rol para este usuario: ").strip()
        
        id_salas = input("Ingrese el ID de la sala (Presione Enter para dejar vacío): ").strip()
        if id_salas == "":
            id_salas = None

        nuevo_usuario = Usuarios(
            username=username,
            email=email,
            contrasena=contrasena,
            id_rol=id_rol,
            id_salas=id_salas,
            created_by="Consola_Admin"
        )
        nuevo_usuario.guardar()

    # 3. Ver cantidad por rol
    elif opcion == "3":
        Usuarios.ver_cantidad_por_rol()

    # 4. Lista de roles
    elif opcion == "4":
        Usuarios.listar_roles()

    # 5. Consultar Sanciones
    elif opcion == "5":
        Sanciones.ver_sanciones_usuario()

    # 6. Buscar salas por capacidad
    elif opcion == "6":
        Usuarios.buscar_salas_por_capacidad()

    # 7. Mostrar reglas del servidor
    elif opcion == "7":
        Reglas.mostrar_reglas_server()

    # 8. Modificar usuario
    elif opcion == "8":
        Usuarios.actualizar()

    # 9. Eliminar usuario 
    elif opcion == "9":
        Usuarios.eliminar()

    # 10. Aplicar Sanción 
    elif opcion == "10":
        Sanciones.agregar_sancion()

    # 0. Salir
    elif opcion == "0":
        print("\n ¡Saliendo del sistema del servidor! Buen viaje.")
        break

    # Validación general de opciones
    else:
        print("\n Opción no válida. Por favor, selecciona una opción correcta del menú.")