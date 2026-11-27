def generate_scene(text: str, context: str) -> dict:
    # В дальнейшем здесь будет вызов LLM

    return {
        "topic": "Пузырьковая сортировка",
        "type": "algorithm",
        "frames": [
            {
                "title": "Исходный массив",
                "description": "Сравниваем 5 и 3",
                "values": [5, 3, 8, 2],
                "highlight": [0, 1],
                "duration": 3
            },
            {
                "title": "Перестановка",
                "description": "Меняем элементы местами",
                "values": [3, 5, 8, 2],
                "highlight": [0, 1],
                "duration": 3
            }
        ]
    }