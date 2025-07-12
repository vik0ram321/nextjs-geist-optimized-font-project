"""
Deployment Manager Module for Madhav Assistant

This module automates deployment of updated code to production environment.
"""

import subprocess
import os

class DeploymentManager:
    def __init__(self, project_dir: str = "."):
        self.project_dir = project_dir

    def deploy(self) -> bool:
        """
        Deploy the updated code.
        This example uses Docker Compose to restart the container.
        Returns True if deployment succeeds, False otherwise.
        """
        try:
            subprocess.run(
                ["docker-compose", "down"],
                cwd=self.project_dir,
                check=True
            )
            subprocess.run(
                ["docker-compose", "up", "-d", "--build"],
                cwd=self.project_dir,
                check=True
            )
            print("Deployment successful.")
            return True
        except subprocess.CalledProcessError as e:
            print("Deployment failed:", e)
            return False

# Example usage:
# manager = DeploymentManager(project_dir="madhav-assistant/docker")
# success = manager.deploy()
# if success:
#     print("Deployed successfully.")
# else:
#     print("Deployment failed.")
