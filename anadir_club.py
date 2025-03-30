from database import SessionLocal
from models import Usuario, Club

# Crear sesión
session = SessionLocal()

# Crear un nuevo club
nuevo_club = Club(nombre="Club Delfines")

# Buscar entrenadores en la BD
entrenadores = session.query(Usuario).filter(Usuario.rol == "entrenador").all()

# Asignar entrenadores al club
nuevo_club.entrenadores = entrenadores

# Guardar en la BD
session.add(nuevo_club)
session.commit()

print(f"✅ Club '{nuevo_club.nombre}' creado con {len(entrenadores)} entrenadores.")

# Cerrar sesión
session.close()
