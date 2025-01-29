import ast

class PatternDetector:
    def __init__(self):
        self.patterns = {
            'loops': 0,
            'conditionals': 0,
            'function_calls': 0,
            'recursion': 0
        }

    def detect(self, tree):
        self.visit_node(tree)
        return self.patterns

    def visit_node(self, node):
        if isinstance(node, ast.For) or isinstance(node, ast.While):
            self.patterns['loops'] += 1
        elif isinstance(node, ast.If):
            self.patterns['conditionals'] += 1
        elif isinstance(node, ast.Call):
            self.patterns['function_calls'] += 1
            
        # Check for recursion
        if isinstance(node, ast.FunctionDef):
            if self._has_recursion(node):
                self.patterns['recursion'] += 1

        for child in ast.iter_child_nodes(node):
            self.visit_node(child)

    def _has_recursion(self, node):
        # Detect recursive function calls
        pass