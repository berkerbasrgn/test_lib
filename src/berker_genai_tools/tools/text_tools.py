def clean_text(text: str) -> str:
    return " ".join(text.strip().split())


def chunk_text(text: str, max_chars: int = 1000) -> list[str]:
    if max_chars <= 0:
        raise ValueError("max_chars must be greater than 0.")

    return [text[i : i + max_chars] for i in range(0, len(text), max_chars)]