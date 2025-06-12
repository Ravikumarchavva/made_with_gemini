# Tests

This directory contains tests for the Made With Gemini package.

## Running Tests

You can run the tests using pytest:

```bash
# Run all tests
uv run pytest
```

## Test Structure

- `test_basic.py` - Basic tests for the package

## Adding New Tests

When adding new functionality to the project, please add corresponding tests to ensure the code works as expected. Tests should:

1. Be placed in the appropriate file or a new file if needed
2. Have clear function names describing what is being tested
3. Use pytest fixtures where appropriate
4. Cover both expected and error cases

## CI Integration

Tests are automatically run in the GitHub CI pipeline for all pull requests and pushes to the main branch.
