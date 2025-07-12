"""
Code Tester Module for Madhav Assistant

This module automates unit and integration testing of generated code.
"""

import subprocess
import os

class CodeTester:
    def __init__(self, test_dir: str = "tests"):
        self.test_dir = test_dir

    def run_tests(self) -> bool:
        """
        Run tests using pytest in the specified test directory.
        Returns True if tests pass, False otherwise.
        """
        try:
            result = subprocess.run(
                ["pytest", self.test_dir],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=True
            )
            print(result.stdout)
            return True
        except subprocess.CalledProcessError as e:
            print("Tests failed:")
            print(e.stdout)
            print(e.stderr)
            return False

# Example usage:
# tester = CodeTester()
# success = tester.run_tests()
# if success:
#     print("All tests passed.")
# else:
#     print("Some tests failed.")
