import os
import requests
from typing import Optional

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:latest")


def query_qwen(prompt: str, max_tokens: int = 256, temperature: float = 0.3) -> Optional[str]:
    if not prompt:
        return None

    try:
        payload = {
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stop": None
        }
        url = f"{OLLAMA_URL}/v1/completions"
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        text = None
        if "choices" in data and len(data["choices"]) > 0:
            text = data["choices"][0].get("text")
        elif "output" in data and len(data["output"]) > 0:
            text = data["output"][0]

        return text

    except Exception as exc:
        return f"OLLAMA error: {exc}"
