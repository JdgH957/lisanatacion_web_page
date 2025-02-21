from fastapi import APIRouter

ROUTER = APIRouter()

@ROUTER.get("/test")
def test_endpoint():
    return {"message": "Hello, World!"}