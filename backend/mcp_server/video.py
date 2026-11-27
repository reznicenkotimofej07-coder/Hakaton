import subprocess
from pathlib import Path


def generate_video(
    image_path: str,
    output_path: str,
    duration: int = 5
) -> str:

    Path(output_path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-t", str(duration),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-an",
        "-movflags", "+faststart",
        output_path
    ]

    subprocess.run(command, check=True)

    return output_path