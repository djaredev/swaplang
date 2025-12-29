from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from swaplang.frontend import frontend
from swaplang.config import settings
from swaplang.database import init_db
from swaplang.api import router

init_db()

app = FastAPI(title=settings.API_NAME, openapi_url=None, docs_url=None, redoc_url=None)


if settings.ENVIRONMENT == "dev":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.ALLOWED_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(router, prefix="/api")
app.mount("/", frontend)
