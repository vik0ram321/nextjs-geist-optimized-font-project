"""
Code Generator Module for Madhav Assistant

This module uses AI to generate or update Madhav's own source code.
"""

import asyncio
from ai_model.model_integration import OpenRouterClient, build_text_message
import yaml
import os

class CodeGenerator:
    def __init__(self, api_key: str):
        self.client = OpenRouterClient(api_key=api_key)

    async def generate_code(self, prompt: str) -> str:
        messages = [build_text_message("user", prompt)]
        response = await self.client.chat(messages)
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")

# Example usage:
# async def main():
#     prompt = "Generate a Python function to reverse a string."
#     generator = CodeGenerator(api_key=os.getenv("OPENROUTER_API_KEY"))
#     code = await generator.generate_code(prompt)
#     print(code)
