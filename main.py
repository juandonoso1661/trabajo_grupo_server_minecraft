# Importamos las clases del proyecto
from usuarios import Usuarios

# =====================================
# MENÚ PRINCIPAL

while True:

    print("\n")
    print("===================================")
    print("  SISTEMA SERVIDOR DE MINECRAFT ")
    print("===================================")

    print("1. Lista de usuarios")
    print("2. Agregar usuario")
    print("3. Modificar usuario")
    print("4. lista de reglas")
    print("5. Baneo de usuario")
    print("6. ")
    print("10. Salir")

    opcion = input("Selecciona una opción (1-4): ").strip()

    if opcion == "1":
        # Llama al método estático directamente desde la clase
        Usuarios.listar()
    else:
        print("\n❌ Opción no válida. Por favor, selecciona una opción del 1-4.")