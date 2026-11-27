COMMANDS = {
    "стоп": "stop",
    "далее": "next",
    "обобщи": "summarize",
    "повтори": "repeat",
    "пример": "example",
    "детализируй": "detail",
    "выбрось": "discard",
    "чепуха": "regenerate"
}


def detect_command(text: str) -> str | None:
    text = text.lower().strip(" .!?")

    if text.startswith("ассистент "):
        text = text.removeprefix("ассистент ")

    return COMMANDS.get(text)