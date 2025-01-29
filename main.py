from src.code_analyzer import CodeAnalyzer
from src.melody_gen import MelodyGenerator
from src.audio_compose import AudioComposer
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert source code to melody')
    parser.add_argument('--source', required=True, help='Source code file path')
    parser.add_argument('--output', required=True, help='Output audio file path')
    args = parser.parse_args()

    analyzer = CodeAnalyzer(args.source)
    code_metrics = analyzer.analyze()
    
    melody_gen = MelodyGenerator(code_metrics)
    melody = melody_gen.generate()
    
    composer = AudioComposer()
    composer.compose(melody, args.output)

if __name__ == "__main__":
    main()