

class Nadador:
    def __init__(self, nombre, apellido, edad, peso, categorias: list[str], disciplinas: list[str], id_entrenador=None, id_club=None, imagen=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.peso = peso
        self.rol = "Nadador"
        self.categorias = categorias
        self.disciplinas = disciplinas
        self.id_entrenador = id_entrenador
        self.id_club = id_club
        self.imagen = imagen
