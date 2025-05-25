from sqlalchemy.orm import Session
from app.Domain.models.nadador import Nadador
from app.Domain.Irepos.Inadador_repo import INadadorRepository
from app.Domain.mappers.nadador_mapper import orm_a_dominio
from app.infrastructure.db.DBModels.nadador_orm import NadadorORM

class NadadorRepository(INadadorRepository):
    def __init__(self, db: Session):
        self.db = db

    def crear_nadador(self, nadador: Nadador) -> Nadador:
        nadador_orm = NadadorORM(
            nombre=nadador.nombre,
            apellido=nadador.apellido,
            email=nadador.email,
            edad=nadador.edad,
            peso=nadador.peso,
            categorias=nadador.categorias,
            disciplinas=nadador.disciplinas,
            id_entrenador=nadador.id_entrenador,
            id_club=nadador.id_club,
            imagen=nadador.imagen
        )
        self.db.add(nadador_orm)
        self.db.commit()
        self.db.refresh(nadador_orm)
        return orm_a_dominio(nadador_orm)
    
    def get_nadador_by_id(self, nadador_id: int) -> Nadador:
        nadador_orm = self.db.query(NadadorORM).filter(NadadorORM.id == nadador_id).first()
        if nadador_orm:
            return orm_a_dominio(nadador_orm)
        return None
    
    def get_nadadores(self) -> list[Nadador]:
        nadadores_orm = self.db.query(NadadorORM).all()
        return [orm_a_dominio(nadador) for nadador in nadadores_orm]
    
    def eliminar_nadador(self, nadador_id: int) -> None:
        nadador_orm = self.db.query(NadadorORM).filter(NadadorORM.id == nadador_id).first()
        if nadador_orm:
            self.db.delete(nadador_orm)
            self.db.commit()

    def actualizar_nadador(self, nadador: Nadador) -> Nadador:
        nadador_orm = self.db.query(NadadorORM).filter(NadadorORM.id == nadador.id).first()
        if nadador_orm:
            nadador_orm.nombre = nadador.nombre
            nadador_orm.apellido = nadador.apellido
            nadador_orm.email = nadador.email
            nadador_orm.edad = nadador.edad
            nadador_orm.peso = nadador.peso
            nadador_orm.categorias = nadador.categorias
            nadador_orm.disciplinas = nadador.disciplinas
            nadador_orm.id_entrenador = nadador.id_entrenador
            nadador_orm.id_club = nadador.id_club
            nadador_orm.imagen = nadador.imagen
            
            self.db.commit()
            self.db.refresh(nadador_orm)
            return orm_a_dominio(nadador_orm)
        return None