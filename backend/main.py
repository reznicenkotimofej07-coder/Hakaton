from fastapi import FastAPI
from backend.config import settings
from backend.api.audio import router as audio_router


app = FastAPI(
    title=settings.app_name,
    version="0.1.0"
)

app.include_router(audio_router)


@app.get("/")
async def root():
    return {"message": "LectureAI API"}


@app.get("/health")
async def health():
    return {"status": "ok"}
from fastapi.staticfiles import StaticFiles
from backend.config import BASE_DIR

app.mount(
    "/ui",
    StaticFiles(
        directory=BASE_DIR / "frontend",
        html=True
    ),
    name="frontend"
)