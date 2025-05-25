from app.Domain.models.club import Club
from app.infrastructure.db.DBModels.club_orm import ClubORM


def orm_a_dominio(club_orm: ClubORM) -> Club:
    return Club(
        nombre=club_orm.nombre,
        descripcion=club_orm.descripcion,
        email=club_orm.email,
        fecha_fundacion=club_orm.fecha_fundacion,
        pais=club_orm.pais,
        ciudad=club_orm.ciudad,
        imagen=club_orm.imagen,
    )