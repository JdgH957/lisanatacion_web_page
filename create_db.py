from database import engine, Base
from models import Usuario
from models import Club

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
print("✅ Base de datos creada correctamente")
