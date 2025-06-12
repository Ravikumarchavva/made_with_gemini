# Made With Gemini

A collection of tools and examples for building applications with Google's Gemini AI platform.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue.svg)](https://www.python.org/downloads/)

## Overview

This repository demonstrates how to leverage Google's Gemini AI capabilities to build practical applications. It includes examples of AI agents, document processing tools, multimodal applications, and other utilities powered by Gemini.

## Prerequisites

- Python 3.13 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- Google API Key or Vertex AI credentials

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/username/made_with_gemini.git
   cd made_with_gemini
   ```

2. Set up your environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```

3. Install dependencies using uv:
   ```bash
   uv sync
   ```

## Features

- 🤖 AI agent examples with Gemini
- 🔄 Seamless integration with Google's Gemini API
- 🧩 Sample applications showcasing multimodal capabilities
- 🛠️ Utility functions for common Gemini operations

## Usage

```python
from made_with_gemini import some_module

# Example code will be added as features are developed
```

## Project Structure

```
made_with_gemini/
├── .github/               # GitHub specific files (workflows, issue templates)
├── direct_api/            # Direct API examples
│   ├── image_based/       # Image-based examples
│   ├── text_based/        # Text-based examples
│   └── video_based/       # Video-based examples
├── gcp_powered/           # GCP-powered examples
│   ├── image_based/       # Image-based examples
│   │   └── renovation_helper/ # Renovation helper application
│   ├── text_based/        # Text-based examples
│   └── video_based/       # Video-based examples
├── tests/                 # Unit and integration tests
├── CODE_OF_CONDUCT.md     # Code of conduct
├── CONTRIBUTING.md        # Contributing guidelines
├── LICENSE                # MIT License
├── README.md              # This file
├── main.py                # Entry point for the application
├── pyproject.toml         # Project configuration
└── uv.lock                # UV package manager lock file
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- Ravi Kumar Chavva - [ravikumarchavva@outlook.com](mailto:ravikumarchavva@outlook.com)
