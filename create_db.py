from app.database import engine, Base
from app.models.usuarios import Usuario

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
print("✅ Base de datos creada correctamente")

