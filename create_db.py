from app.database import engine, Base
from app.Domain.models.usuario import Usuario

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)
print("✅ Base de datos creada correctamente")

