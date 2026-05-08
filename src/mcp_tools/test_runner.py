import subprocess
import os
from typing import Dict, Any

class TestRunner:
    """
    Executes parameterized unit tests via MCP.
    Acts as the primary ground truth for the Verification Agent to detect Semantic Drift.
    Ensures safe execution bounded to the designated operational directory.
    """

    def __init__(self, project_root: str = "."):
        self.project_root = os.path.abspath(project_root)

    def run_tests(self, test_path: str) -> Dict[str, Any]:
        """
        Safely executes pytest on the specified directory or file.
        Returns a dictionary containing the pass/fail status and terminal outputs.
        """
        full_test_path = os.path.abspath(os.path.join(self.project_root, test_path))
        
        # 1. SECURITY CHECK: Unsafe Action (Formal Definition)
        if not full_test_path.startswith(self.project_root):
            return {
                "success": False,
                "passed": False,
                "output": "Unsafe Action: Attempted to execute tests outside the operational directory.",
                "error": "Path traversal detected."
            }

        try:
            # 2. TEST EXECUTION: Run pytest as a sandboxed subprocess
            result = subprocess.run(
                ["pytest", full_test_path, "-v", "--tb=short"],
                capture_output=True,
                text=True,
                cwd=self.project_root
            )

            passed = result.returncode == 0

            return {
                "success": True,
                "passed": passed,
                "output": result.stdout,
                "error": result.stderr if not passed else None
            }
        
        except FileNotFoundError:
            return {
                "success": False,
                "passed": False,
                "output": "Pytest is not installed or not found in the environment.",
                "error": "FileNotFoundError"
            }
        except Exception as e:
            return {
                "success": False,
                "passed": False,
                "output": "",
                "error": str(e)
            }

if __name__ == "__main__":
    print("--- Test Runner Execution ---")
    runner = TestRunner()
    
    result = runner.run_tests("src/")
    
    print(f"Did Tool Run Successfully?: {result.get('success')}")
    print(f"Did Tests Pass?: {result.get('passed')}")
    
    if result.get('output'):
        print("\nOutput Summary (Last 3 Lines):")
        print('\n'.join(result.get('output').splitlines()[-3:]))