from app.infrastructure.db.DBModels.entrenador_orm import EntrenadorORM
from app.application.DTOS.entrenador_dto import EntrenadorCreateDTO, EntrenadorOutDTO, EntrenadorUpdateDTO
from app.Domain.models.entrenador import Entrenador
from app.application.DTOS.nadador_dto import NadadorOutDTO  # Asegúrate de tenerlo bien definido


def dto_a_dominio(dto: EntrenadorCreateDTO) -> Entrenador:
    return Entrenador(
        nombre=dto.nombre,
        apellido=dto.apellido,
        email=dto.email,
        contacto=dto.contacto,
        edad=dto.edad,
        disciplinas=[d.name for d in dto.disciplinas],
        categorias=[c.name for c in dto.categorias],
        id_club=dto.id_club,
        experiencia=dto.experiencia,
        imagen=dto.imagen,
        rol="entrenador"  # Fijamos directamente el rol
    )


def dominio_a_orm(entrenador: Entrenador) -> EntrenadorORM:
    return EntrenadorORM(
        nombre=entrenador.nombre,
        apellido=entrenador.apellido,
        email=entrenador.email,
        rol=entrenador.rol,  # ← Aquí usamos directamente el string "entrenador"
        contacto=entrenador.contacto,
        edad=entrenador.edad,
        disciplinas=entrenador.disciplinas,
        categorias=entrenador.categorias,
        id_club=entrenador.id_club,
        experiencia=entrenador.experiencia,
        imagen=entrenador.imagen
    )


def orm_a_dominio(entrenador_orm: EntrenadorORM) -> Entrenador:
    return Entrenador(
        nombre=entrenador_orm.nombre,
        apellido=entrenador_orm.apellido,
        email=entrenador_orm.email,
        rol=entrenador_orm.rol,
        contacto=entrenador_orm.contacto,
        edad=entrenador_orm.edad,
        disciplinas=entrenador_orm.disciplinas,
        categorias=entrenador_orm.categorias,
        id_club=entrenador_orm.id_club,
        experiencia=entrenador_orm.experiencia,
        imagen=entrenador_orm.imagen,
        nadadores=entrenador_orm.nadadores  # Si ya vienen como lista de dominio o instancias ORM
    )


def dominio_a_dto_out(entrenador: Entrenador) -> EntrenadorOutDTO:
    return EntrenadorOutDTO(
        nombre=entrenador.nombre,
        apellido=entrenador.apellido,
        email=entrenador.email,
        disciplinas=entrenador.disciplinas,
        categorias=entrenador.categorias,
        experiencia=entrenador.experiencia,
        imagen=entrenador.imagen,
        nadadores=[
            NadadorOutDTO(
                nombre=n.nombre,
                apellido=n.apellido,
                email=n.email,
            ) for n in entrenador.nadadores
        ]
    )


def orm_a_dto_out(entrenador_orm: EntrenadorORM) -> EntrenadorOutDTO:
    return EntrenadorOutDTO(
        id=entrenador_orm.id,
        nombre=entrenador_orm.nombre,
        apellido=entrenador_orm.apellido,
        email=entrenador_orm.email,
        disciplinas=entrenador_orm.disciplinas,
        categorias=entrenador_orm.categorias,
        experiencia=entrenador_orm.experiencia,
        imagen=entrenador_orm.imagen,
        nadadores=[
            NadadorOutDTO(
                id=n.id,
                nombre=n.nombre,
                apellido=n.apellido,
                email=n.email
            ) for n in entrenador_orm.nadadores
        ]
    )



def dto_update_a_dominio(dto: EntrenadorUpdateDTO) -> Entrenador:
    return Entrenador(
        nombre=dto.nombre,
        apellido=dto.apellido,
        email=dto.email,
        contacto=dto.contacto,
        edad=dto.edad,
        disciplinas=[d.name for d in dto.disciplinas],
        categorias=[c.name for c in dto.categorias],
        id_club=dto.id_club,
        experiencia=dto.experiencia,
        imagen=dto.imagen
    )


def actualizar_entrenador_con_dto(entrenador: Entrenador, dto: EntrenadorUpdateDTO) -> Entrenador:
    if dto.nombre is not None:
        entrenador.nombre = dto.nombre
    if dto.apellido is not None:
        entrenador.apellido = dto.apellido
    if dto.email is not None:
        entrenador.email = dto.email
    if dto.contacto is not None:
        entrenador.contacto = dto.contacto
    if dto.edad is not None:
        entrenador.edad = dto.edad
    if dto.disciplinas is not None:
        entrenador.disciplinas = [d.name for d in dto.disciplinas]
    if dto.categorias is not None:
        entrenador.categorias = [c.name for c in dto.categorias]
    if dto.id_club is not None:
        entrenador.id_club = dto.id_club
    if dto.experiencia is not None:
        entrenador.experiencia = dto.experiencia
    if dto.imagen is not None:
        entrenador.imagen = dto.imagen
    return entrenador
