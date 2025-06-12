# Contributing to Made With Gemini

Thank you for your interest in contributing to Made With Gemini! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with the following information:

- A clear, descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Any additional context (screenshots, error messages, etc.)

### Suggesting Features

Feature suggestions are welcome! Please create an issue with:

- A clear, descriptive title
- Detailed description of the proposed feature
- Any relevant examples or use cases

### Pull Requests

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests if applicable
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Development Setup

1. Clone your fork of the repository
2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

## Style Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Write docstrings for all functions, classes, and modules
- Include comments for complex logic
- Write clear commit messages

## Testing

- Add tests for new features
- Ensure all tests pass before submitting a pull request

## License

By contributing to this project, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).
