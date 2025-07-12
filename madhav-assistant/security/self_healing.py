"""
Self Healing Module for Madhav Assistant

This module detects attacks or anomalies and generates self-healing scripts or patches.
"""

import asyncio
from ai_model.model_integration import OpenRouterClient, build_text_message
import yaml
import os

class SelfHealingAgent:
    def __init__(self, api_key: str):
        self.client = OpenRouterClient(api_key=api_key)

    async def analyze_attack(self, attack_data: str) -> str:
        prompt = f"Analyze the following attack or anomaly data and generate self-healing scripts or patches to mitigate it:\n{attack_data}"
        messages = [build_text_message("user", prompt)]
        response = await self.client.chat(messages)
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")

# Example usage:
# async def main():
#     with open("attack_data.txt") as f:
#         data = f.read()
#     agent = SelfHealingAgent(api_key=os.getenv("OPENROUTER_API_KEY"))
#     healing_script = await agent.analyze_attack(data)
#     print(healing_script)
