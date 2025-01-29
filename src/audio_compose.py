import numpy as np
from scipy.io import wavfile
from typing import List

class AudioComposer:
    def __init__(self, sample_rate: int = 44100):
        self.sample_rate = sample_rate

    def compose(self, melody: List[dict], output_path: str):
        signal = self._generate_audio_signal(melody)
        signal = self._apply_effects(signal)
        signal = self._normalize(signal)
        wavfile.write(output_path, self.sample_rate, signal)

    def _generate_audio_signal(self, melody: List[dict]) -> np.ndarray:
        pass

    def _apply_effects(self, signal: np.ndarray) -> np.ndarray:
        pass

    def _normalize(self, signal: np.ndarray) -> np.ndarray:
        pass
