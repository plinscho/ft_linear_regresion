#!/bin/bash

# Exit on any error
set -e

echo "Upgrading pip..."
python3 -m pip install --user --upgrade pip

echo "Creating virtual environment..."
python3 -m venv ./virtual_env

echo "Virtual environment created successfully!"
echo "To activate it and install requirements, run:"
echo "  source ./virtual_env/bin/activate"
echo "  pip install -r srcs/requirements.txt"
echo ""
echo "To deactivate later, simply run:"
echo "  deactivate"