from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from change_lang.translator.translate import translate

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/changelang")
async def change_lang(text: str, source_language: str, target_language: str):
    translation = translate(
        text=text, source_language=source_language, target_language=target_language
    )
    return {"translation": translation}
