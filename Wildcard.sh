#!/bin/bash

# This script assumes that you are running it in an environment where such actions are authorized
# The script will kill the current terminal, open a new one, and display ASCII art

# Configuration
ASCII_ART_PATH="./Jack.txt" # Default path to ASCII art file. Change if needed.

# Check if gnome-terminal is available
if ! command -v gnome-terminal &> /dev/null
then
    echo "gnome-terminal could not be found. Please install it or modify the script to use your terminal."
    exit 1
fi

# Check if ASCII art file exists
if [ ! -f "$ASCII_ART_PATH" ]; then
    echo "Error: ASCII art file not found at $ASCII_ART_PATH" 
    exit 1
fi

# Kill the current terminal session
# This command may vary depending on the environment; some terminals might not allow being killed easily
# Consider making this part optional or more robust based on expected environments.
pkill -TERM -u $USER gnome-terminal

# Open a new terminal and display the ASCII art
# The --full-screen option might not be supported by all terminal emulators or versions.
gnome-terminal --full-screen -- bash -c "cat \"$ASCII_ART_PATH\"; exec bash"
