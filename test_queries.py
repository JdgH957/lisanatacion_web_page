from database import SessionLocal
from models import Usuario

# Crear sesión
session = SessionLocal()

# Insertar un usuario
nuevo_usuario = Usuario(nombre="Juan Pérez", email="juan@example.com", rol="deportista")
session.add(nuevo_usuario)
session.commit()
print("✅ Usuario agregado")

# Consultar usuarios
usuarios = session.query(Usuario).all()
print("📌 Usuarios registrados:")
for usuario in usuarios:
    print(usuario.id, usuario.nombre, usuario.email, usuario.rol)

# Cerrar sesión
session.close()
