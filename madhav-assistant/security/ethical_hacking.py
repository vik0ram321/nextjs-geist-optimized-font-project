"""
Ethical Hacking Learning Module for Madhav Assistant

This module uses AI to analyze security logs, learn vulnerabilities,
and suggest mitigation strategies.
"""

import asyncio
from ai_model.model_integration import OpenRouterClient, build_text_message
import yaml
import os

class EthicalHackingLearner:
    def __init__(self, api_key: str):
        self.client = OpenRouterClient(api_key=api_key)

    async def analyze_logs(self, logs: str) -> str:
        prompt = f"Analyze the following security logs and identify potential vulnerabilities and mitigation steps:\n{logs}"
        messages = [build_text_message("user", prompt)]
        response = await self.client.chat(messages)
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")

# Example usage:
# async def main():
#     with open("security_logs.txt") as f:
#         logs = f.read()
#     learner = EthicalHackingLearner(api_key=os.getenv("OPENROUTER_API_KEY"))
#     analysis = await learner.analyze_logs(logs)
#     print(analysis)
