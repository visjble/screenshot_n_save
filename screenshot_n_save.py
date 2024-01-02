import os
import subprocess
from tkinter import filedialog
from tkinter import Tk

def take_screenshot():
    # Take a screenshot with gnome-screenshot and save it temporarily
    temp_file = "/tmp/screenshot.png"
    subprocess.run(["gnome-screenshot", "-a", "-f", temp_file])
    return temp_file

def save_screenshot(screenshot_file):
    # Hide the main Tkinter window
    root = Tk()
    root.withdraw()

    # Set the default directory
    default_dir = "/home/docs"
    
    # Ask the user where to save the screenshot
    file_path = filedialog.asksaveasfilename(initialdir=default_dir,
                                             defaultextension=".png",
                                             filetypes=[("PNG files", "*.png")],
                                             title="Save screenshot as...")
    if file_path:
        # Save the screenshot to the selected location
        os.rename(screenshot_file, file_path)
        print(f"Screenshot saved to {file_path}")
    else:
        print("Screenshot save cancelled.")

    root.destroy()

def main():
    screenshot_file = take_screenshot()
    save_screenshot(screenshot_file)

if __name__ == "__main__":
    main()
