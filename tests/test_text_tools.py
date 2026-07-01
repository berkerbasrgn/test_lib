from berker_genai_tools.tools.text_tools import clean_text, chunk_text


def test_clean_text_removes_extra_spaces() -> None:
    assert clean_text(" hello    world ") == "hello world"


def test_chunk_text() -> None:
    chunks = chunk_text("abcdef", max_chars=2)
    assert chunks == ["ab", "cd", "ef"]