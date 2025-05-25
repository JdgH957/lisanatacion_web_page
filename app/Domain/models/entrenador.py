
class Entrenador:
    def __init__(self,nombre, apellido, email, contacto, edad, categorias: list[str], disciplinas: list[str], id_club=None, experiencia=None, imagen=None, nadadores=None):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.rol = "entrenador"
        self.contacto = contacto
        self.edad = edad
        self.disciplinas = disciplinas
        self.categorias = categorias
        self.id_club = id_club
        self.experiencia = experiencia
        self.imagen = imagen
        self.nadadores = nadadores if nadadores is not None else []
