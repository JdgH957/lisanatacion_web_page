from sqlalchemy.orm import Session
from typing import List, Optional
from app.Domain.models.usuario import Usuario
from app.infrastructure.db.DBModels.usuario_orm import UsuarioORM
from app.Domain.Irepos.Iusuario_repo import IUsuarioRepository
from app.Domain.mappers.usuario_mapper import orm_a_dominio


class UsuarioRepository(IUsuarioRepository):

    def __init__(self, db: Session):
        self.db = db

    def existe_email(self, email: str) -> bool:
        return self.db.query(UsuarioORM).filter(UsuarioORM.email == email).first() is not None

    def crear_usuario(self, usuario: Usuario):
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
        return orm_a_dominio(usuario_db), usuario_db.id
    
    def get_usuarios(self) -> List[Usuario]:
        usuario_orm = self.db.query(UsuarioORM).all()
        return [orm_a_dominio(u) for u in usuario_orm]

    def get_usuario_by_id(self, usuario_id: int) -> Optional[Usuario]:
        usuario_orm = self.db.query(UsuarioORM).filter(UsuarioORM.id == usuario_id).first()
        if not usuario_orm:
            return None
        return orm_a_dominio(usuario_orm)

    def eliminar_usuario(self, usuario_id: int) -> None:
        self.db.query(UsuarioORM).filter(UsuarioORM.id == usuario_id).delete()
        self.db.commit()
    
    def actualizar_usuario(self, usuario_id: int, usuario: Usuario) -> Usuario:
        usuario_orm = self.db.query(UsuarioORM).filter(UsuarioORM.id == usuario_id).first()
        if not usuario_orm:
            raise ValueError("Usuario no encontrado")

        usuario_orm.nombre = usuario.nombre
        usuario_orm.apellido = usuario.apellido
        usuario_orm.email = usuario.email
        usuario_orm.contra = usuario.contra
        # Puedes añadir campos adicionales si los tienes

        self.db.commit()
        self.db.refresh(usuario_orm)
        return orm_a_dominio(usuario_orm)
