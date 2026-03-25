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
            "stream": False,
            "options": {
                "temperature": temperature,
                "num_predict": max_tokens
            }
        }
        url = f"{OLLAMA_URL}/api/generate"
        resp = requests.post(url, json=payload, timeout=45)
        resp.raise_for_status()
        data = resp.json()

        return data.get("response")

    except Exception as exc:
        return f"OLLAMA error: {exc}"
