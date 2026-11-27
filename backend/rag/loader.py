from pathlib import Path

import pymupdf
from docx import Document
from bs4 import BeautifulSoup


def load_document(path: Path) -> str:
    extension = path.suffix.lower()

    if extension == ".txt":
        return path.read_text(encoding="utf-8")

    if extension == ".pdf":
        with pymupdf.open(path) as document:
            return "\n".join(
                page.get_text() for page in document
            )

    if extension == ".docx":
        document = Document(path)

        return "\n".join(
            p.text for p in document.paragraphs
        )

    if extension == ".html":
        soup = BeautifulSoup(
            path.read_text(encoding="utf-8"),
            "html.parser"
        )

        return soup.get_text(separator="\n")

    raise ValueError(f"Unsupported format: {extension}")
def split_text(
    text: str,
    size: int = 500,
    overlap: int = 100
) -> list[str]:

    if not 0 <= overlap < size:
        raise ValueError("Invalid overlap")

    chunks = []
    step = size - overlap

    for i in range(0, len(text), step):
        chunks.append(text[i:i + size])

        if i + size >= len(text):
            break

    return chunks