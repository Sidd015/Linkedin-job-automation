#!/bin/bash

# Job Application Sender - Quick Start Script
# This script helps you run the application locally for testing

echo "================================================"
echo "  Job Application Sender - Quick Start"
echo "================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✓ Python found: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed!"
    echo "Please install pip"
    exit 1
fi

echo "✓ pip found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "✓ Dependencies installed successfully"
echo ""

# Create uploads folder if it doesn't exist
mkdir -p uploads

echo "================================================"
echo "  Starting the application..."
echo "================================================"
echo ""
echo "Backend will run on: http://localhost:5000"
echo "Frontend: Open index.html in your browser"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the Flask app
python3 app.py
