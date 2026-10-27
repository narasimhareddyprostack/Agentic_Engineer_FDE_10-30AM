import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
# Connect Python to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

for model in client.models.list().data:
    pricing = model.pricing or {}
    architecture = model.architecture or {}

    is_free = (
        float(pricing.get("prompt", -1)) == 0
        and float(pricing.get("completion", -1)) == 0
    )
    is_text_to_text = (
        architecture.get("input_modalities") == ["text"]
        and architecture.get("output_modalities") == ["text"]
    )

    if is_free and is_text_to_text:
        print(model.id)