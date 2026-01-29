# pytest_tutorial_1

Short description: How to guides of a pytest project which pretty much includes all major and mostly used features of the pytest.

## Table of Contents
- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About
Goals of the repository, what readers will learn, are to illustrate pytest's features from fundemental to advanced with detailed code examples to audience.

## Prerequisites
- Python 3.8+
- pip or uv (uv is utilized for creation of the virtual environment for this project)
- pytest
- requests

## Installation
Clone and install dependencies:
```bash
git clone <repo-url>
cd pytest_tutorial_1
python -m venv .venv
source .venv/bin/activate    # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Running Tests
Run all tests with pytest:
```bash
pytest
```
Run a single test file or verbose output:
```bash
pytest tests/test_example.py -q
pytest -k "expression" -q
```
Generate coverage report (if using pytest-cov):
```bash
pytest --cov=src
```

## Project Structure
```
pytest_tutorial_1/
├── src/
│   └── package_name/
├── tests/
│   └── test_example.py
├── requirements.txt
├── pyproject.toml / setup.cfg
└── README.md
```

## Usage
Show short examples of how to import and use library functions, or how test fixtures are organized.

## Contributing
- Fork the repo
- Create a feature branch
- Add tests for new features
- Open a PR with description

## License
Specify a license (e.g., MIT). Add NOTICE or LICENSE file.

## Contact
Maintainer: Turgay Koklu — turgay.koklu@hotmail.com

<!-- Optional: Badges, CI status, links -->