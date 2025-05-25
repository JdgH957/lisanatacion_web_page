from app.database import engine, Base
import subprocess
from sqlalchemy import text

def reset_db():
    with engine.connect() as conn:
        conn.execute(text("DROP SCHEMA public CASCADE;"))
        conn.execute(text("CREATE SCHEMA public;"))
        conn.commit()
    print("✅ Esquema público reiniciado")

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente")

def run_alembic_upgrade():
    subprocess.run(["alembic", "upgrade", "head"])
    print("✅ Migraciones aplicadas")

if __name__ == "__main__":
    reset_db()
    create_tables()
    run_alembic_upgrade()

