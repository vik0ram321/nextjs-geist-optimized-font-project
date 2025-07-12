import os
import httpx
import json
from typing import List, Dict, Any, Optional

class OpenRouterClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://openrouter.ai/api/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def chat(self, messages: List[Dict[str, Any]], model: str = "mistralai/mistral-7b-instruct") -> Dict[str, Any]:
        payload = {
            "model": model,
            "messages": messages
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()

def build_text_message(role: str, text: str) -> Dict[str, Any]:
    return {
        "role": role,
        "content": [
            {"type": "text", "text": text}
        ]
    }

def build_file_message(role: str, filename: str, file_data_base64: str) -> Dict[str, Any]:
    return {
        "role": role,
        "content": [
            {"type": "text", "text": f"File: {filename}"},
            {"type": "file", "file": {"filename": filename, "file_data": file_data_base64}}
        ]
    }

# Example usage:
# import asyncio
# async def main():
#     client = OpenRouterClient(api_key=os.getenv("OPENROUTER_API_KEY"))
#     messages = [build_text_message("user", "Hello, Madhav!")]
#     response = await client.chat(messages)
#     print(response)
# asyncio.run(main())
