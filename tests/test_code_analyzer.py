import unittest
from src.code_analyzer import CodeAnalyzer

class TestCodeAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CodeAnalyzer("test_samples/sample_code.py")

    def test_complexity_analysis(self):
        metrics = self.analyzer.analyze()
        self.assertIn('complexity', metrics)
        self.assertIsInstance(metrics['complexity'], dict)

    def test_pattern_detection(self):
        metrics = self.analyzer.analyze()
        self.assertIn('patterns', metrics)
        self.assertIsInstance(metrics['patterns'], dict)

    def test_structure_analysis(self):
        metrics = self.analyzer.analyze()
        self.assertIn('structure', metrics)