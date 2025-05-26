from sqlalchemy.orm import Session
from app.Domain.mappers.club_mapper import orm_a_dominio
from app.Domain.models.club import Club
from app.Domain.Irepos.Iclub_repo import IclubRepository
from app.infrastructure.db.DBModels.club_orm import ClubORM


class ClubRepository(IclubRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_club(self, club: Club) -> Club:
        # Convertir el objeto Club a un objeto ORM
        club_orm = ClubORM(
            nombre=club.nombre,
            descripcion=club.descripcion,
            email=club.email,
            fecha_fundacion=club.fecha_fundacion,
            pais=club.pais,
            ciudad=club.ciudad,
            imagen=club.imagen,
        )
        self.db.add(club_orm)
        self.db.commit()
        self.db.refresh(club_orm)
        return orm_a_dominio(club_orm)

    def get_clubes(self) -> list[Club]:
        return [orm_a_dominio(club) for club in self.db.query(ClubORM).all()]

    def get_club_by_id(self, club_id: int) -> Club:
        club_orm = self.db.query(ClubORM).filter(ClubORM.id == club_id).first()
        if club_orm is None:
            return None
        return orm_a_dominio(club_orm)

    def actualizar_club(self, club: Club) -> Club:
        # Asumiendo que club ya tiene el id y los datos actualizados
        db_club = self.db.query(ClubORM).filter(ClubORM.id == club.id).first()
        if not db_club:
            return None
        db_club.nombre = club.nombre
        db_club.descripcion = club.descripcion
        db_club.fecha_fundacion = club.fecha_fundacion
        db_club.pais = club.pais
        db_club.ciudad = club.ciudad
        db_club.imagen = club.imagen
        self.db.commit()
        self.db.refresh(db_club)
        return orm_a_dominio(db_club)

    def eliminar_club(self, club_id: int) -> None:
        db_club = self.db.query(ClubORM).filter(ClubORM.id == club_id).first()
        if db_club:
            self.db.delete(db_club)
            self.db.commit()
