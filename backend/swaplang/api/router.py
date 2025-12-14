from fastapi import APIRouter
from swaplang.api.routes import auth, translate, settings

api_router = APIRouter()

api_router.include_router(auth.router)
api_router.include_router(translate.router)
api_router.include_router(settings.router)
