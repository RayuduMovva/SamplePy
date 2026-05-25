# SamplePy

A Python project demonstrating machine learning capabilities using scikit-learn for data analysis and model development.

## Overview

SamplePy is a modular Python application designed to provide a foundation for machine learning projects. It leverages scikit-learn for machine learning operations and follows best practices for project organization, dependency management, and code structure.

## Architecture & Design

### Design Principles

- **Modularity**: Code is organized into logical components with clear separation of concerns
- **Scalability**: Structured to accommodate growth from simple scripts to complex machine learning pipelines
- **Maintainability**: Clean code practices and consistent project structure for easy maintenance
- **Reproducibility**: Python 3.12+ requirement ensures consistent behavior across environments

### Project Structure

```
SamplePy/
├── main.py              # Application entry point
├── pyproject.toml       # Project metadata and configuration
├── requirements.txt     # Pinned dependencies
└── README.md           # Documentation
```

### Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| Language | Python | ≥3.12 |
| ML Framework | scikit-learn | 1.4.2 |
| Package Manager | pip/setuptools | Latest |

### Core Components

1. **Entry Point (main.py)**
   - Serves as the application's primary entry point
   - Orchestrates the execution flow
   - Currently demonstrates basic console output

2. **Dependencies**
   - **scikit-learn**: Industry-standard machine learning library providing:
     - Classification algorithms
     - Regression models
     - Clustering techniques
     - Dimensionality reduction
     - Model evaluation utilities

## Requirements

- **Python**: 3.12 or higher
- **Dependencies**: See [requirements.txt](requirements.txt)

## Installation

### Using UV (Recommended)

This project uses [UV](https://docs.astral.sh/uv/) for fast, reliable Python environment and dependency management.

**Environment Setup:**

1. Initialize the UV project:
   ```bash
   uv init
   ```

2. Install Python 3.12:
   ```bash
   uv python install 3.12
   ```

3. Create a virtual environment with Python 3.12:
   ```bash
   uv venv .venv --python 3.12
   ```

4. Pin Python version to 3.12:
   ```bash
   uv python pin 3.12
   ```

5. Install dependencies from requirements.txt:
   ```bash
   uv pip install -r .\requirements.txt
   ```

6. Add dependencies and update pyproject.toml:
   ```bash
   uv add -r .\requirements.txt
   ```

7. Sync the environment:
   ```bash
   uv sync
   ```

### Traditional Installation

If not using UV:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd SamplePy
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .\.venv\Scripts\Activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

## Development

### Project Configuration

The project uses `pyproject.toml` for configuration following PEP 518 standards:

```toml
[project]
name = "samplepy"
version = "0.1.0"
description = "Machine learning project foundation"
requires-python = ">=3.12"
dependencies = ["scikit-learn==1.4.2"]
```

### Adding New Dependencies

1. Update `requirements.txt` with pinned versions for reproducibility
2. Update `pyproject.toml` with dependency information
3. Reinstall: `pip install -r requirements.txt`

## Future Enhancements

- Data pipeline implementation
- Model training and evaluation workflows
- Configuration management system
- Logging framework
- Testing infrastructure
- Documentation generation

## License

Add your license information here.

## Contributing

Contributions are welcome! Please follow the project's code structure and maintain Python 3.12+ compatibility.
