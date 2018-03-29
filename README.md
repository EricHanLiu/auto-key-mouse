# Usage
1. Download auto-key-mouse.py
2. Install the [PyAutoGUI library](http://pyautogui.readthedocs.io/en/latest/install.html)
3. Run with `python auto-key-mouse [genre]`, where [genre], a string, is any music genre you feel like listening to. Must be written with quotes if it's multiple words.
4. Must use Python 2.

Example usage:
- `python auto-key-mouse jazz` 
- `python auto-key-mouse "vaporwave lofi chillhop"` 

# What it does
As of now, this will navigate to youtube and get you the first video from search using the keyword [genre]. Uses the PyAutoGUI library.

Not entirely compatible with every setup, since this relies on a shortcut to open the browser. This can be averted by starting with your browser open in the background. Works best with resolutions similar to 1366x768. 
