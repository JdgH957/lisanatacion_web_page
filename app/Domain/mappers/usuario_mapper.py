from app.Domain.models.usuario import Usuario, RolUsuario
from app.infrastructure.db.DBModels.usuario_orm import UsuarioORM
from app.application.DTOS.usuario_dto import UsuarioCreateDTO, UsuarioOutDTO, UsuarioUpdateDTO
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

def dominio_a_dto_out(usuario: Usuario) -> UsuarioOutDTO:
    rol_str = rol_dominio_a_str(usuario.rol)
    return UsuarioOutDTO(
        nombre=usuario.nombre,
        apellido=usuario.apellido,
        email=usuario.email,
        rol=rol_str
    )

def actualizar_usuario_con_dto(usuario: Usuario, dto: UsuarioUpdateDTO) -> Usuario:
    if dto.nombre is not None:
        usuario.nombre = dto.nombre
    if dto.apellido is not None:
        usuario.apellido = dto.apellido
    if dto.email is not None:
        usuario.email = dto.email
    if dto.fecha_asig is not None:
        usuario.fecha_asig = dto.fecha_asig
    if dto.rol is not None:
        usuario.rol = dto.rol
    if dto.contacto is not None:
        usuario.contacto = dto.contacto
    if dto.edad is not None:
        usuario.edad = dto.edad
    return usuario