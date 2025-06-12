# Renovation Helper

A renovation helper application that uses Gemini AI to analyze room images and provide renovation recommendations.

## Features

- Room type identification
- Furniture and fixture detection
- Style classification
- Renovation recommendations
- Cost estimation

## How It Works

1. Upload an image of a room
2. The application uses Gemini Pro Vision to analyze the image
3. Get detailed renovation recommendations based on the analysis
4. View estimated costs and material suggestions

## Setup

1. Set up GCP credentials as described in the main README
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   python main.py
   ```

## Requirements

- Google Cloud Storage bucket (for storing images)
- Gemini Pro Vision API access
- Python 3.13 or higher
