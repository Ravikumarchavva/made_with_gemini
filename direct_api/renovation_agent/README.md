# Renovation Agent

A renovation agent that uses Gemini AI to analyze room images and provide detailed renovation recommendations with cost estimates.

## Features

- Room type identification
- Furniture and fixture detection
- Style classification
- Comprehensive renovation recommendations
- Detailed cost estimation for materials and labor
- Styling suggestions based on current trends

## How It Works

1. The agent analyzes an image of a room using Gemini Pro Vision
2. It identifies the current style, features, and potential areas for improvement
3. It generates a detailed renovation plan with step-by-step recommendations
4. Cost estimates are provided for each renovation component
5. A sample renovation plan can be found in `rennovate.md`

## Usage

```bash
uv run adk web
```

## Requirements

- Google API Key (set in `.env` file)
- Python 3.13 or higher
- Gemini Pro Vision API access

## Requirements

- Google Cloud Storage bucket (for storing images)
- Gemini Pro Vision API access
- Python 3.13 or higher
