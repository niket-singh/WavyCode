# WavyCode

## Description
WavyCode is an innovative tool that transforms source code into musical compositions, creating a unique auditory representation of code quality and structure. By analyzing various code metrics and patterns, it generates melodic sequences that help developers "hear" their code, providing a novel way to identify code complexity, patterns, and potential issues through audio feedback.

### Key Features
- Source code to music conversion using advanced code metrics
- Multi-layered musical composition based on:
  - Code complexity (cyclomatic, cognitive, Halstead metrics)
  - Design patterns and code structure
  - Nesting levels and function relationships
- Real-time code analysis and music generation
- Support for multiple output formats (WAV, MP3)
- Customizable musical parameters
- Detailed analysis reports

### Technologies Used
- Python 3.8+
- AST (Abstract Syntax Tree) for code analysis
- NumPy for numerical computations
- SciPy for audio signal processing
- Custom implementations of:
  - Code metrics calculators
  - Pattern detection algorithms
  - Music generation systems

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Audio output device

### Installation

1. Clone the repository:
```bash
git clone https://github.com/niket-singh/WavyCode.git
cd WavyCode
```
2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Usage

Basic Command: 
```bash
python main.py --source <source_file.py> --output <output_file.wav>
```

Advanced Options:
```bash
python main.py --source example.py \
               --output melody.wav \
               --tempo 120 \
               --scale minor \
               --complexity-weight 0.7
```

### Parameters
--source: Path to source code file
--output: Output audio file path
--tempo: Beats per minute (default: 120)
--scale: Musical scale (major/minor)
--complexity-weight: Weight of complexity in melody generation (0-1)

### Project Structure

WavyCode/
│
├── src/
│   ├── code_analyzer.py        # Code analysis implementation
│   ├── melody_gen.py     # Music generation logic
│   ├── pattern_detect.py     # Code pattern detection
│   ├── sound_map.py         # Maps code metrics to sound
│   ├── complexity_calculate.py # Complexity metrics
│   └── audio_compose.py       # Audio composition and output
│
├── tests/
│   ├── test_code_analyzer.py
│   ├── test_melody_generator.py
│   └── test_pattern_detector.py
│
├── examples/
│   ├── simple.py
│   ├── complex.py
│   └── patterns.py
│
├── requirements.txt
└── main.py
