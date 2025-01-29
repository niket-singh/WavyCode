import unittest
from src.melody_gen import MelodyGenerator

class TestMelodyGenerator(unittest.TestCase):
    def setUp(self):
        self.test_metrics = {
            'complexity': {'cyclomatic': 5, 'cognitive': 8},
            'patterns': {'loops': 2, 'conditionals': 3},
            'structure': {'depth': 3, 'functions': 4}
        }
        self.generator = MelodyGenerator(self.test_metrics)

    def test_melody_generation(self):
        melody = self.generator.generate()
        self.assertIsInstance(melody, list)
        self.assertTrue(len(melody) > 0)

    def test_rhythm_generation(self):
        rhythm = self.generator._complexity_to_rhythm()
        self.assertIsInstance(rhythm, list)