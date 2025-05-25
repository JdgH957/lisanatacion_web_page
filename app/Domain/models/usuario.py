from app.application.common.enums import RolUsuario


class Usuario:
    def __init__(self, nombre, apellido, email, contra, fecha_asig, rol : RolUsuario, contacto, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contra = contra
        self.fecha_asig = fecha_asig
        self.rol = rol
        self.contacto = contacto
        self.edad = edad
