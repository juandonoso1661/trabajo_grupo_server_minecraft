class reglas:
    def __init__(self, id_reglas, nombre_reglas, tipo_reglas):
        self.id_regla = id_reglas
        self.nombre_reglas = nombre_reglas
        self.tipo_de_reglas = tipo_reglas

    def mostrar_regla(self):
        print(f"ID: {self.id_regla}")
        print(f"Nombre: {self.nombre_reglas}")
        print(f"Tipo de regla: {self.tipo_de_reglas}")

regla1 = reglas(1, "NO USAR HACKS", "seguridad")
regla2 = reglas(2, "NO INSULTOS EN EL CHAT", "convivencia")
regla3 = reglas(3, "NO SOBREEXPLOTAR MODS", "seguridad")
regla4 = reglas(4, "NO HACER SPAM", "chat")