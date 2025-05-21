from enum import Enum
from datetime import date

class RolUsuario(str, Enum):
    ENTRENADOR = "entrenador"
    CLUB = "club"

class Usuario:
    def __init__(self, nombre, apellido, email, contra, fecha_asig, rol, contacto, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contra = contra
        self.fecha_asig = fecha_asig
        self.rol = rol
        self.contacto = contacto
        self.edad = edad
