"""
Stable Diffusion Trainer Module for Madhav Assistant

This module integrates with Stability AI's Stable Diffusion API for image generation and training.
"""

import httpx
import os
import base64

class StableDiffusionTrainer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.endpoint = "https://api.stability.ai/v1/generation/stable-diffusion-v1-5/text-to-image"

    async def generate_image(self, prompt: str, width: int = 512, height: int = 512) -> bytes:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text_prompts": [{"text": prompt}],
            "cfg_scale": 7,
            "clip_guidance_preset": "FAST_BLUE",
            "height": height,
            "width": width,
            "samples": 1,
            "steps": 30,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            # Extract base64 image data
            image_base64 = data['artifacts'][0]['base64']
            return base64.b64decode(image_base64)

# Example usage:
# import asyncio
# async def main():
#     trainer = StableDiffusionTrainer(api_key=os.getenv("STABILITY_AI_API_KEY"))
#     image_bytes = await trainer.generate_image("A futuristic cityscape at sunset")
#     with open("output.png", "wb") as f:
#         f.write(image_bytes)
# asyncio.run(main())
