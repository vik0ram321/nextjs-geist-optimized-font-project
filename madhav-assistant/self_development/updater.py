"""
Updater Module for Madhav Assistant

This module orchestrates self-upgrade process: generate → test → deploy.
"""

import asyncio
from code_generator import CodeGenerator
from code_tester import CodeTester
from deployment_manager import DeploymentManager
import os

class Updater:
    def __init__(self, api_key: str, project_dir: str = "."):
        self.generator = CodeGenerator(api_key=api_key)
        self.tester = CodeTester()
        self.deployer = DeploymentManager(project_dir=project_dir)

    async def self_upgrade(self, prompt: str) -> bool:
        # Generate new code
        new_code = await self.generator.generate_code(prompt)
        # Save new code to file (example: self update script)
        with open("madhav_assistant_update.py", "w") as f:
            f.write(new_code)

        # Run tests
        tests_passed = self.tester.run_tests()
        if not tests_passed:
            print("Tests failed. Aborting deployment.")
            return False

        # Deploy updated code
        deployed = self.deployer.deploy()
        return deployed

# Example usage:
# async def main():
#     updater = Updater(api_key=os.getenv("OPENROUTER_API_KEY"), project_dir="madhav-assistant/docker")
#     prompt = "Update the main.py to add a new feature X."
#     success = await updater.self_upgrade(prompt)
#     if success:
#         print("Self upgrade completed successfully.")
#     else:
#         print("Self upgrade failed.")
