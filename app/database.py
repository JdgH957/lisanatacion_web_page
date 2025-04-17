from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Datos de conexión
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "liga_natacion"

# Crear el motor de base de datos
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# ✅ Aquí defines la función get_db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()