import os
from pathlib import Path
import mercadopago
from dotenv import load_dotenv
import json
import urllib.parse
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.application.DTOS.horario_dto import ReservaHorariosCursoNuevoRequest
from app.application.DTOS.miembro_dto import InscripcionMiembroRequest
from app.infrastructure.db.DBModels.curso_orm import CursoORM
from app.infrastructure.db.DBModels.horario_orm import HorarioORM

load_dotenv()

ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")
FRONTEND_URL = os.getenv("FRONTEND_URL")
BACKEND_URL = "https://3de1-186-144-112-247.ngrok-free.app"
print(f"🔗 BACKEND_URL cargado: {BACKEND_URL}")
sdk = mercadopago.SDK(ACCESS_TOKEN)


def crear_preferencia_mp(title: str, price: float) -> str:
    preference_data = {
        "items": [
            {
                "title": title,
                "quantity": 1,
                "unit_price": price,
                "currency_id": "COP"
            }
        ],
        "back_urls": {
            "success": f"{BACKEND_URL}/postpago?estado=success",
            "failure": f"{BACKEND_URL}/postpago?estado=failure",
            "pending": f"{BACKEND_URL}/postpago?estado=pending"
        },
        "auto_return": "approved"
    }

    preference = sdk.preference().create(preference_data)
    return preference["response"]["init_point"]


def procesar_pago(payment_id: str) -> str:
    """
    Consulta Mercado Pago y procesa el resultado del pago.
    Devuelve una cadena con el estado: 'exito', 'pendiente' o 'fallo'
    """
    result = sdk.payment().get(payment_id)
    pago_info = result["response"]

    if pago_info["status"] == "approved":
        # Aquí simulas registrar la compra en la base de datos
        # Ejemplo: guardar user_id, producto_id, monto, etc.
        print("✅ Pago aprobado. Guardando en base de datos...")
        return "exito"

    elif pago_info["status"] == "in_process":
        return "pendiente"

    else:
        return "fallo"


def crear_link_de_pago_reserva(data: ReservaHorariosCursoNuevoRequest, db: Session) -> str:
    horarios = db.query(HorarioORM).filter(
        HorarioORM.id_horario.in_(data.horario_ids)
    ).all()

    if len(horarios) != len(data.horario_ids):
        raise HTTPException(status_code=404, detail="Uno o más horarios no existen")

    piscina_id = horarios[0].piscina_id

    items = [
        {
            "title": f"{h.dia} - {h.hora_inicio}",
            "quantity": 1,
            "unit_price": h.precio,
            "currency_id": "COP"
        }
        for h in horarios
    ]

    back_urls = {
        "success": f"{BACKEND_URL}/cursos/postpago?estado=success",
        "failure": f"{BACKEND_URL}/cursos/postpago?estado=failure",
        "pending": f"{BACKEND_URL}/cursos/postpago?estado=pending"
    }

    preference_data = {
        "items": items,
        "back_urls": back_urls,
        "auto_return": "approved",
        "external_reference": json.dumps({
            "piscina_id": piscina_id,
            "horario_ids": data.horario_ids,
            "id_entrenador": data.id_entrenador,
            "categoria": data.categoria,
            "max_cupos": data.max_cupos,
            "disciplina": data.disciplina,
            "precio_mes": data.precio_mes,
            "precio_prueba": data.precio_prueba,
            "descripcion": data.descripcion
        })
    }

    preference = sdk.preference().create(preference_data)
    return preference["response"]["init_point"]


def procesar_postpago_curso(payment_id: str, external_reference: str, db: Session) -> str:
    """result = sdk.payment().get(payment_id)
    pago = result["response"]

    if pago["status"] != "approved":
        return "fallido"""

    try:
        # ✅ Decodificar correctamente el external_reference desde URL
        decoded_reference = urllib.parse.unquote(external_reference)
        external_data = json.loads(decoded_reference)

        piscina_id = external_data["piscina_id"]
        horario_ids = external_data["horario_ids"]
        id_entrenador = external_data["id_entrenador"]
        categoria = external_data["categoria"]
        max_cupos = external_data["max_cupos"]
        disciplina = external_data["disciplina"]
        precio_mes = external_data["precio_mes"]
        precio_prueba = external_data["precio_prueba"]
        descripcion = external_data.get("descripcion")

    except Exception:
        raise HTTPException(status_code=400, detail="Error en los datos del pago (external_reference inválido)")

    nuevo_curso = CursoORM(
        piscina_id=piscina_id,
        entrenador_id=id_entrenador,
        categoria=categoria,
        max_cupos=max_cupos,
        cantidad_miembros=0,
        disciplina=disciplina,
        precio_mes=precio_mes,
        precio_prueba=precio_prueba,
        descripcion=descripcion
    )

    db.add(nuevo_curso)
    db.commit()
    db.refresh(nuevo_curso)

    db.query(HorarioORM).filter(HorarioORM.id_horario.in_(horario_ids)).update(
        {
            HorarioORM.disponible: False,
            HorarioORM.curso_id: nuevo_curso.id_curso
        },
        synchronize_session=False
    )

    db.commit()
    return "exito"




# app/services/pay_services.py (añadir)

def crear_link_pago_miembro(data: InscripcionMiembroRequest, db: Session) -> str:
    curso = db.query(CursoORM).filter(CursoORM.id_curso == data.curso_id).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso no encontrado")

    # Determinar el precio según tipo_miembro
    if data.tipo_miembro == "prueba":
        precio = curso.precio_prueba
        descripcion = "Inscripción prueba"
    elif data.tipo_miembro == "mensual":
        precio = curso.precio_mes
        descripcion = "Inscripción mensual"
    else:
        raise HTTPException(status_code=400, detail="Tipo de miembro inválido")

    item = {
        "title": f"{descripcion} - {data.nombre}",
        "quantity": 1,
        "unit_price": precio,
        "currency_id": "COP"
    }

    preference_data = {
        "items": [item],
        "back_urls": {
            "success": f"{BACKEND_URL}/miembros/postpago?estado=success",
            "failure": f"{BACKEND_URL}/miembros/postpago?estado=failure",
            "pending": f"{BACKEND_URL}/miembros/postpago?estado=pending"
        },
        "auto_return": "approved",
        "external_reference": json.dumps(data.dict())  # Guardamos todo para postpago
    }

    preference = sdk.preference().create(preference_data)
    return preference["response"]["init_point"]
