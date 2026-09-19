from crewai.tools import BaseTool


class CalculatorTool(BaseTool):
    name: str = "Calculator"
    description: str = "Useful for performing mathematical calculations."

    def _run(self, expression: str) -> str:
        try:
            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)
        except Exception:
            return "Invalid mathematical expression"