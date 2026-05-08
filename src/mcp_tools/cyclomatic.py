from radon.complexity import cc_visit
from typing import Dict, Any

class ComplexityAnalyzer:
    """
    Measures Cyclomatic Complexity to quantify Technical Debt (D).
    Calculates the successful reduction of technical debt (ΔD) as defined in the formal model.
    """

    @staticmethod
    def calculate_total_complexity(code: str) -> int:
        """
        Parses the code block and calculates the total cyclomatic complexity.
        Returns -1 if the code contains syntax errors and cannot be parsed.
        """
        try:
            blocks = cc_visit(code)
            total_complexity = sum([block.complexity for block in blocks])
            return total_complexity if total_complexity > 0 else 1
        except SyntaxError:
            return -1
        except Exception:
            return -1

    @staticmethod
    def evaluate_debt_reduction(original_code: str, refactored_code: str) -> Dict[str, Any]:
        """
        Calculates ΔD = C_orig - C_refact
        A valid refactoring cycle must result in ΔD > 0.
        """
        c_orig = ComplexityAnalyzer.calculate_total_complexity(original_code)
        c_refact = ComplexityAnalyzer.calculate_total_complexity(refactored_code)

        if c_orig == -1 or c_refact == -1:
            return {
                "success": False,
                "error": "SyntaxError: Cannot calculate complexity. The refactored code might be broken."
            }

        delta_d = c_orig - c_refact

        return {
            "success": True,
            "original_complexity": c_orig,
            "refactored_complexity": c_refact,
            "delta_d": delta_d,
            "is_improved": delta_d > 0
        }

if __name__ == "__main__":
    spaghetti_code = """
def process_data(data):
    if data:
        if len(data) > 0:
            for item in data:
                if item == 1:
                    print("One")
                elif item == 2:
                    print("Two")
                else:
                    print("Other")
    """

    clean_code = """
def process_data(data):
    if not data: return
    
    mapping = {1: "One", 2: "Two"}
    for item in data:
        print(mapping.get(item, "Other"))
    """

    print("--- Complexity Test ---")
    result = ComplexityAnalyzer.evaluate_debt_reduction(spaghetti_code, clean_code)
    print(f"Original Code Complexity (C_orig): {result.get('original_complexity')}")
    print(f"Refactored Code Complexity (C_refact): {result.get('refactored_complexity')}")
    print(f"Technical Debt Reduction (ΔD): {result.get('delta_d')}")
    print(f"Is Code Improved?: {result.get('is_improved')}")