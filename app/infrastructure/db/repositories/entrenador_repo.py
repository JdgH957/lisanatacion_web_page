from sqlalchemy.orm import Session
from app.Domain.Irepos.Ientrenador_repo import IEntrenadorRepository
from app.Domain.models.entrenador import Entrenador
from app.infrastructure.db.DBModels.entrenador_orm import EntrenadorORM
from app.Domain.mappers.entrenador_mapper import orm_a_dominio


class EntrenadorRepository(IEntrenadorRepository):
    def __init__(self, db: Session):
        self.db = db
    def crear_entrenador(self, entrenador: Entrenador) -> Entrenador:
        entrenador_db = EntrenadorORM(
            nombre=entrenador.nombre,
            apellido=entrenador.apellido,
            email=entrenador.email,
            rol=entrenador.rol,
            contacto=entrenador.contacto,
            edad=entrenador.edad,
            disciplinas=entrenador.disciplinas,
            categorias=entrenador.categorias,
            id_club=entrenador.id_club,
            experiencia=entrenador.experiencia,
            imagen=entrenador.imagen,
        )
        self.db.add(entrenador_db)
        self.db.commit()
        self.db.refresh(entrenador_db)
        return orm_a_dominio(entrenador_db)


    def get_entrenador_by_id(self, entrenador_id: int) -> Entrenador:
        entrenador_orm = self.db.query(EntrenadorORM).filter(EntrenadorORM.id == entrenador_id).first()
        if not entrenador_orm:
            return None
        return orm_a_dominio(entrenador_orm)

    def eliminar_entrenador(self, entrenador_id: int) -> None:
        self.db.query(EntrenadorORM).filter(EntrenadorORM.id == entrenador_id).delete()
        self.db.commit()

    def actualizar_entrenador(self, entrenador_id: int, entrenador: Entrenador) -> Entrenador:
        entrenador_orm = self.db.query(EntrenadorORM).filter(EntrenadorORM.id == entrenador_id).first()
        if not entrenador_orm:
            raise ValueError("Entrenador no encontrado")
        
        # Actualizar los campos del entrenador
        entrenador_orm.nombre = entrenador.nombre
        entrenador_orm.apellido = entrenador.apellido
        entrenador_orm.email = entrenador.email
        entrenador_orm.contacto = entrenador.contacto
        entrenador_orm.edad = entrenador.edad
        entrenador_orm.disciplinas = entrenador.disciplinas
        entrenador_orm.categorias = entrenador.categorias
        entrenador_orm.id_club = entrenador.id_club
        entrenador_orm.experiencia = entrenador.experiencia
        entrenador_orm.imagen = entrenador.imagen

        self.db.commit()
        self.db.refresh(entrenador_orm)
        return orm_a_dominio(entrenador_orm)

    def get_entrenadores(self) -> list[Entrenador]:
        entrenadores_orm = self.db.query(EntrenadorORM).all()
        return [orm_a_dominio(e) for e in entrenadores_orm]
    
    def agregar_nadador(self, entrenador_id: int, nadador_id: int) -> Entrenador:
        entrenador = self.db.query(EntrenadorORM).filter(EntrenadorORM.id == entrenador_id).first()
        if not entrenador:
            raise ValueError("Entrenador no encontrado")
        
        # Aquí se debería agregar la lógica para agregar un nadador al entrenador
        # Esto depende de cómo esté estructurada la relación entre Entrenador y Nadador
        # Por ejemplo, si hay una relación muchos a muchos, se podría hacer algo como:
        # entrenador.nadadores.append(nadador)
        
        self.db.commit()
        self.db.refresh(entrenador)
        return entrenador