from app.database import SessionLocal
from app.models.usuarios import Usuario
from datetime import date

# Crear sesión
session = SessionLocal()

try:
    # Insertar un usuario
    nuevo_usuario = Usuario(
        nombre="Danna Prada",
        contra="valenti7336",
        email="dannaprada@example.com",
        
        fecha_asig=date.today(),  # Fecha actual
        rol="deportista"
    )

    session.add(nuevo_usuario)
    session.commit()
    print("✅ Usuario agregado con éxito.")

except Exception as e:
    session.rollback()
    print("❌ Error al agregar usuario:", e)

# Consultar usuarios
usuarios = session.query(Usuario).all()
print("📌 Usuarios registrados:")
for usuario in usuarios:
    print(usuario.id, usuario.nombre,usuario.contra, usuario.email,usuario.fecha_asig, usuario.rol)

# Cerrar sesión
session.close()
