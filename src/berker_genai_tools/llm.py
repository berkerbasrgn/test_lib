from openai import OpenAI

from .config import settings


class LLMClient:
    def __init__(self, model: str | None = None):
        if not settings.openai_api_key:
            raise ValueError("OPENAI_API_KEY is missing. Add it to your .env file.")

        self.client = OpenAI(api_key=settings.openai_api_key)
        self.model = model or settings.default_model

    def complete(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text