from enum import Enum

class RolUsuario(str, Enum):
    ENTRENADOR = "entrenador"
    CLUB = "club"
    ADMIN = "admin"


class Categorias(str, Enum):
    INFANTIL = "infantil"
    JUVENIL = "juvenil"
    ADULTO = "adulto"
    SENIOR = "senior"
    MASTER = "master"
    VETERANO = "veterano"
    SUPER_VETERANO = "super_veterano"

class Disciplinas(str, Enum):
    NATACION = "natacion"
    WATERPOLO = "waterpolo"
    SALTOS = "saltos"
    MARIPOSA = "mariposa"
    LIBRE = "libre"
    ESPALDA = "espalda"
    BRAZA = "braza"