from mcp.server.fastmcp import FastMCP

from backend.mcp_server.stt import transcribe_audio
from backend.mcp_server.image import generate_image
from backend.mcp_server.video import generate_video


mcp = FastMCP(
    "LectureAI Tools",
    host="127.0.0.1",
    port=8001
)


@mcp.tool()
def speech_to_text(audio_path: str) -> str:
    """Преобразование аудио в текст."""
    return transcribe_audio(audio_path)


@mcp.tool()
def create_image(
    values: list[int],
    title: str,
    highlight: list[int],
    output_path: str
) -> str:
    """Создание изображения массива."""
    return generate_image(
        values, title, highlight, output_path
    )


@mcp.tool()
def create_video(
    image_path: str,
    output_path: str
) -> str:
    """Создание беззвучного видео."""
    return generate_video(image_path, output_path)


if __name__ == "__main__":
    mcp.run(transport="streamable-http")