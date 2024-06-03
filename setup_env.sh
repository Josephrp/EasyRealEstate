#!/bin/bash

# Python version to use
PYTHON_VERSION="3.11"

# Check if Python $PYTHON_VERSION is installed
if ! python$PYTHON_VERSION --version > /dev/null 2>&1; then
    echo "Python $PYTHON_VERSION is not installed. Please install Python $PYTHON_VERSION and try again."
    exit 1
fi

# Create virtual environment with Python $PYTHON_VERSION
python$PYTHON_VERSION -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

echo "Virtual environment setup complete."