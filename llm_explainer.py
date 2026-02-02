import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"

def explain_result(result: dict, question: str) -> str:
    prompt = f"""
A user asked: "{question}"

The following result was computed from a CSV file using code:
- Operation: {result['operation']}
- Column: {result['column']}
- Value: {result['value']}

Explain this result clearly in one short paragraph.
Do NOT perform calculations.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,   # ✅ THIS IS THE KEY
            "options": {"temperature": 0.3}
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["message"]["content"]
