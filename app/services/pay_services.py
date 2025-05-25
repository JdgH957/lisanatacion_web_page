import os
import mercadopago
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("MP_ACCESS_TOKEN")
FRONTEND_URL = os.getenv("FRONTEND_URL")
BACKEND_URL = os.getenv("BACKEND_URL")
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
