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

class DiaSemanaEnum(str, Enum):
    lunes = "lunes"
    martes = "martes"
    miercoles = "miércoles"
    jueves = "jueves"
    viernes = "viernes"
    sabado = "sábado"
    domingo = "domingo"

class MesEnum(str, Enum):
    enero = "enero"
    febrero = "febrero"
    marzo = "marzo"
    abril = "abril"
    mayo = "mayo"
    junio = "junio"
    julio = "julio"
    agosto = "agosto"
    septiembre = "septiembre"
    octubre = "octubre"
    noviembre = "noviembre"
    diciembre = "diciembre"
