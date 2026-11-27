from faster_whisper import WhisperModel
from functools import lru_cache


@lru_cache(maxsize=1)
def get_model():
    return WhisperModel(
        "base",
        device="cpu",
        compute_type="int8"
    )


def transcribe_audio(audio_path: str) -> str:
    segments, info = get_model().transcribe(
        audio_path,
        language="ru"
    )

    return " ".join(
        segment.text.strip()
        for segment in segments
    )