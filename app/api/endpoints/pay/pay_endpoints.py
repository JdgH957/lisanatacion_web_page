from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse
from app.core.auth.jwt_bearer import JwtBearer  # o el path real de tu clase
from pydantic import BaseModel

from app.services.pay_services import crear_preferencia_mp, procesar_pago

router = APIRouter()

PRODUCTOS = {
    1: {"title": "Curso de Python", "price": 25000},
    2: {"title": "Asesoría personal", "price": 60000},
}

class PagoRequest(BaseModel):
    producto_id: int

@router.post("/crear-preferencia/")
def crear_preferencia(
    data: PagoRequest,
    payload: dict = Depends(JwtBearer())  # Aquí entra el JWT decodificado
):
    # Puedes acceder al payload aquí, por ejemplo:
    user_id = payload.get("sub")  # o el campo que uses
    producto = PRODUCTOS.get(data.producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    link = crear_preferencia_mp(producto["title"], producto["price"])
    return {"link_de_pago": link}


@router.get("/postpago")
async def post_pago(request: Request, estado: str):
    query_params = dict(request.query_params)
    payment_id = query_params.get("payment_id")

    if not payment_id:
        return RedirectResponse(url="https://www.google.com?error=sin_payment_id")

    estado_final = procesar_pago(payment_id)
    return RedirectResponse(url=f"https://www.google.com?estado={estado_final}")