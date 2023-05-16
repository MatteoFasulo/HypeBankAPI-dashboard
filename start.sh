#!/bin/bash

# Install requirements.txt
pip install -r requirements.txt

# Clear the screen
clear

# Prompt the user for EMAIL
read -p "Enter your email: " EMAIL

# Prompt the user for BIRTHDATE
read -p "Enter your birthdate (YYYY-MM-DD): " BIRTHDATE

# Prompt the user for LIMIT
read -p "Enter limit of transaction fetched (Default 50): " LIMIT

# Execute the main.py script with the provided arguments
if command -v python &> /dev/null; then
    python main.py -m "$EMAIL" -b "$BIRTHDATE" -l "$LIMIT"
# Fallback to python3 if python is not available
elif command -v python3 &> /dev/null; then
    python3 main.py -m "$EMAIL" -b "$BIRTHDATE" -l "$LIMIT"
else
    echo "Python interpreter not found. Please install Python or Python3."
    exit 1
fi

docker build -t hype_dashboard:latest .