import ast
from typing import Dict

class ComplexityCalculator:
    def __init__(self):
        self.metrics = {
            'cyclomatic': 0,
            'cognitive': 0,
            'halstead': 0
        }

    def calculate(self, tree: ast.AST) -> Dict[str, float]:
        self.metrics = {
            'cyclomatic': self._calculate_cyclomatic_complexity(tree),
            'cognitive': self._calculate_cognitive_complexity(tree),
            'halstead': self._calculate_halstead_metrics(tree)
        }
        return self.metrics

    def _calculate_cyclomatic_complexity(self, tree: ast.AST) -> float:
        pass

    def _calculate_cognitive_complexity(self, tree: ast.AST) -> float:
        pass

    def _calculate_halstead_metrics(self, tree: ast.AST) -> float:
        pass
