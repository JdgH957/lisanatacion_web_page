from sqlalchemy.orm import Session
from app.infrastructure.db.DBModels.usuario_orm import UsuarioORM
from app.infrastructure.db.DBModels.entrenador_orm import EntrenadorORM
from app.infrastructure.db.DBModels.club_orm import ClubORM
from app.application.DTOS.usuario_dto import UsuarioCreateDTO

class IUsuarioRepository:
    def existe_email(self, email: str) -> bool: ...
    def crear_usuario(self, usuario: UsuarioCreateDTO): ...

class UsuarioRepository(IUsuarioRepository):
    def __init__(self, db: Session):
        self.db = db

    def existe_email(self, email: str) -> bool:
        return self.db.query(UsuarioORM).filter(UsuarioORM.email == email).first() is not None

    def crear_usuario(self, usuario: UsuarioCreateDTO):
        usuario_db = UsuarioORM(
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            email=usuario.email,
            contra=usuario.contra,
            fecha_asig=usuario.fecha_asig,
            rol=usuario.rol,
            contacto=usuario.contacto,
            edad=usuario.edad
        )
        self.db.add(usuario_db)
        self.db.commit()
        self.db.refresh(usuario_db)

        if usuario.rol == "entrenador":
            self.db.add(EntrenadorORM(
                nombre=usuario.nombre,
                apellido=usuario.apellido,
                email=usuario.email,
                fecha_asig=usuario.fecha_asig
            ))
        elif usuario.rol == "club":
            if not usuario.fecha_asig:
                raise ValueError("Se requiere fecha de creación para un club")
            self.db.add(ClubORM(
                nombre_club=usuario.nombre,
                fecha_creacion=usuario.fecha_asig,
                email=usuario.email
            ))
        self.db.commit()
        return usuario_db
