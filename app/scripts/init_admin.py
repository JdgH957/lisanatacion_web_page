# app/scripts/init_admin.py
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.usuarios import Usuario
from app.auth import hash_password
import datetime 

def crear_admin():
    db: Session = SessionLocal()

    admin_existente = db.query(Usuario).filter(Usuario.email == "admin@admin.com").first()
    if admin_existente:
        print("El admin ya existe.")
        return

    usuario_admin = Usuario(
        nombre = "felipe",
        apellido = "olivar",
        email="admin@admin.com",
        contra=hash_password("admin123"),
        fecha_asig = datetime.date.today(),
        rol="admin"

    )
    db.add(usuario_admin)
    db.commit()
    db.close()
    print("Admin creado correctamente.")

if __name__ == "__main__":
    crear_admin()
