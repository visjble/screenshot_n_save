# README.md for Screenshot Utility Script

## Overview
This Python script provides a simple utility for taking screenshots in a Linux environment, specifically using the `gnome-screenshot` tool. The script allows the user to select an area for the screenshot and then gives the option to save the screenshot to a specified directory.

## Features
- **User-selected Screenshot**: Utilizes `gnome-screenshot` to capture a user-defined area of the screen.
- **Custom Save Location**: Allows the user to choose where to save the screenshot.
- **GUI File Dialog**: Uses a Tkinter-based file dialog for easy navigation and file saving.

## Requirements
- Linux-based operating system with `gnome-screenshot` installed.
- Python 3.x.
- Tkinter (usually comes pre-installed with Python).

## Usage
1. Run the script using Python.
2. Select the area of the screen you want to capture when prompted.
3. Choose a location to save the screenshot using the file dialog.
4. The script will save the screenshot in the chosen location and print the file path.

## Script Breakdown
### `take_screenshot()`
This function handles the screenshot capturing process. It uses the `subprocess` module to call `gnome-screenshot` with specific arguments to capture an area of the screen selected by the user. The screenshot is temporarily saved to `/tmp/screenshot.png`.

### `save_screenshot(screenshot_file)`
This function is responsible for saving the captured screenshot to a location specified by the user. It first initializes a Tkinter window and hides it. Then, it opens a file dialog asking the user to choose the save location. The screenshot is then moved to the chosen path.

### `main()`
The main function of the script. It calls `take_screenshot()` to capture the screenshot and then `save_screenshot()` to save the screenshot file.

## Notes
- This script is designed for Linux environments with `gnome-screenshot`. It may require modifications for other environments.
- The default directory in the save file dialog is set to `/home/dir`. Adjust this path according to your needs.

## Future Enhancements
- Add error handling for scenarios such as `gnome-screenshot` not being installed, or the user closing the file dialog without choosing a save location.
- Extend compatibility to other Linux desktop environments and screenshot tools.

## Setting Up an Alias for the Script
Make running the script convenient by setting up a bash alias.

Step 1: Create a Bash Script
In the script directory, create run_snapshot.sh:
#!/bin/bash
python /path/to/snapshot.py
Replace /path/to/snapshot.py with the full script path.

Make the bash script executable:

chmod +x run_snapshot.sh

Step 2: Add Alias in .bash_aliases
Edit or create .bash_aliases in your home directory:
nano ~/.bash_aliases

Add the alias command:

alias snapshot='/path/to/run_snapshot.sh'
Replace /path/to/run_snapshot.sh with the bash script path.
Step 3: Activate the Alias
Reload .bash_aliases:

source ~/.bash_aliases
Run the script using snapshot.
##Notes
Designed for Linux with gnome-screenshot. Adjust for different environments.
