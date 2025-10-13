from fastapi import APIRouter
from swaplang.api.routes import auth, translate

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(translate.router)
