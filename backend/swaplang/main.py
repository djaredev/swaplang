from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from swaplang.frontend import frontend
from swaplang.config import settings
from swaplang.api import router
from swaplang.scripts import prestart
from swaplang.utils.logger import logger

app = FastAPI(
    title=settings.API_NAME,
    openapi_url=settings.OPENAPI_URL,
    docs_url=None,
    redoc_url=None,
)


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


def run_server():
    import uvicorn

    prestart()

    logger.info("Starting server...")
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)
