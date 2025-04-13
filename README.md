# D&D Adventure System

A text-based D&D-style adventure game system that needs improvements and new features.

## Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

## Running Tests with Coverage

```bash
pytest --cov=dndgame
```

## Type Checking

```bash
mypy .
```

## Code Formatting

```bash
black .
```