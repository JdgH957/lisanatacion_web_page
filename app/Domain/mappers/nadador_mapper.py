from app.Domain.models.nadador import Nadador
from app.infrastructure.db.DBModels.nadador_orm import NadadorORM


def orm_a_dominio(nadador_orm: NadadorORM) -> Nadador:
    return Nadador(
        nombre=nadador_orm.nombre,
        apellido=nadador_orm.apellido,
        email=nadador_orm.email,
        edad=nadador_orm.edad,
        peso=nadador_orm.peso,
        categorias=[cat for cat in nadador_orm.categorias],
        disciplinas=[disc for disc in nadador_orm.disciplinas],
        id_entrenador=nadador_orm.id_entrenador,
        id_club=nadador_orm.id_club,
        imagen=nadador_orm.imagen
    )