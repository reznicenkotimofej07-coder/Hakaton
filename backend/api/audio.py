from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.config import settings
from pathlib import Path
from uuid import uuid4


router = APIRouter(prefix="/api/audio", tags=["Audio"])

MAX_SIZE = 20 * 1024 * 1024


@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    suffix = Path(file.filename or "").suffix.lower()

    if suffix not in {".wav", ".mp3", ".webm", ".ogg", ".m4a"}:
        raise HTTPException(400, "Unsupported audio format")

    content = await file.read(MAX_SIZE + 1)

    if len(content) > MAX_SIZE:
        raise HTTPException(413, "File is too large")

    audio_dir = settings.storage_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{uuid4()}{suffix}"
    path = audio_dir / filename
    path.write_bytes(content)

    return {
        "status": "uploaded",
        "audio_id": filename
    }