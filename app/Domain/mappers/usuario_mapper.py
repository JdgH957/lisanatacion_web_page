from app.Domain.models.usuario import Usuario, RolUsuario
from app.infrastructure.db.DBModels.usuario_orm import UsuarioORM
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO
from app.infrastructure.db.DBModels.usuario_orm import RolUsuarioEnum

def rol_dominio_a_orm(rol: RolUsuario) -> RolUsuarioEnum:
    return RolUsuarioEnum(rol.value)

def rol_orm_a_dominio(rol_orm: RolUsuarioEnum) -> RolUsuario:
    return RolUsuario(rol_orm.value)

def rol_dominio_a_str(rol: RolUsuario) -> str:
    return rol.value

def str_a_rol_dominio(rol_str: str) -> RolUsuario:
    return RolUsuario(rol_str)
    
def orm_a_dominio(usuario_orm: UsuarioORM) -> Usuario:
    rol_dominio = rol_orm_a_dominio(usuario_orm.rol)
    return Usuario(
        nombre=usuario_orm.nombre,
        apellido=usuario_orm.apellido,
        email=usuario_orm.email,
        contra=usuario_orm.contra,
        fecha_asig=usuario_orm.fecha_asig,
        rol=rol_dominio,
        contacto=usuario_orm.contacto,
        edad=usuario_orm.edad,
    )

def dominio_a_orm(usuario: Usuario) -> UsuarioORM:
    rol_orm = rol_dominio_a_orm(usuario.rol)
    return UsuarioORM(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        contra=usuario.contra,
        fecha_asig=usuario.fecha_asig,
        rol=rol_orm,
        contacto=usuario.contacto,
        edad=usuario.edad,
    )

def dto_update_a_dominio(dto: UsuarioCreateDTO) -> Usuario:
    rol = str_a_rol_dominio(dto.rol)
    return Usuario(
        nombre=dto.nombre,
        apellido=dto.apellido,
        email=dto.email,
        contra=dto.contra,
        fecha_asig=dto.fecha_asig,
        rol=rol,
        contacto=dto.contacto,
        edad=dto.edad
    )

def dto_create_a_dominio(dto: UsuarioCreateDTO) -> Usuario:
    rol = str_a_rol_dominio(dto.rol)
    return Usuario(
        nombre=dto.nombre,
        apellido=dto.apellido,
        email=dto.email,
        contra=dto.contra,
        fecha_asig=dto.fecha_asig,
        rol=rol,
        contacto=dto.contacto,
        edad=dto.edad
    )

def dominio_a_dto_out(usuario: Usuario, usuario_id: int) -> UsuarioOutDTO:
    rol_str = rol_dominio_a_str(usuario.rol)
    return UsuarioOutDTO(
        id=usuario_id,
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        rol=rol_str
    )