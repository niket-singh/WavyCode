import unittest
import ast
from src.pattern_detect import PatternDetector

class TestPatternDetector(unittest.TestCase):
    def setUp(self):
        self.detector = PatternDetector()

    def test_loop_detection(self):
        code = """
        for i in range(10):
            print(i)
        """
        tree = ast.parse(code)
        patterns = self.detector.detect(tree)
        self.assertEqual(patterns['loops'], 1)

    def test_conditional_detection(self):
        code = """
        if x > 0:
            print('positive')
        """
        tree = ast.parse(code)
        patterns = self.detector.detect(tree)
        self.assertEqual(patterns['conditionals'], 1)