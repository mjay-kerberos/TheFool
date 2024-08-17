#!/bin/bash

# This script assumes that you are running it in an environment where such actions are authorized
# The script will kill the current terminal, open a new one, and display ASCII art

# Kill the current terminal session
# This command may vary depending on the environment; some terminals might not allow being killed easily
pkill -TERM -u $USER gnome-terminal

# Open a new terminal and display the ASCII art
gnome-terminal --full-screen -- bash -c 'cat /path/to/jack.txt; bash'
