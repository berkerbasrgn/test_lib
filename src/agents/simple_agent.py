from ..llm import LLMClient
from ..prompts import summarize_prompt


class SimpleSummarizerAgent:
    def __init__(self, model: str | None = None):
        self.llm = LLMClient(model=model)

    def run(self, text: str) -> str:
        prompt = summarize_prompt(text)
        return self.llm.complete(prompt)