from berker_genai_tools import LLMClient, clean_text


def main() -> None:
    text = "   This is a messy text.   "
    cleaned = clean_text(text)

    llm = LLMClient()
    response = llm.complete(f"Explain this text: {cleaned}")

    print(response)


if __name__ == "__main__":
    main()