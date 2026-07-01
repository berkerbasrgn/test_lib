def summarize_prompt(text: str) -> str:
    return f"""
Summarize the following text clearly and concisely.

Text:
{text}
""".strip()


def extract_claims_prompt(text: str) -> str:
    return f"""
Extract product claims from the following packaging text.

Return only a JSON list of claims.

Text:
{text}
""".strip()