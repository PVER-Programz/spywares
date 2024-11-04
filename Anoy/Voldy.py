import pyautogui
from pynput import keyboard
import time
import os
import sys

# Mapping of keys to spooky phrases in alphabetical order
key_mapping = {
    'A': 'vada Kedavra ',
    'B': 'eware the Dark Lord ',
    'C': 'hamber of secrets has been opened ',
    'D': 'ark forces are rising ',
    'E': 'vil will always find a way ',
    'F': 'ear the unknown ',
    'G': 'rave danger is near ',
    'H': 'e who must not be named ',
    'I': 'n darkness, he thrives ',
    'J': 'oin the ranks of the fallen ',
    'K': 'illing curse awaits you ',
    'L': 'ord of Dark magic ',
    'M': 'y power is eternal ',
    'N': 'agini ',
    'O': 'nly the brave face the dark ',
    'P': 'ower beyond imagination ',
    'Q': 'uiet whispers in the shadows ',
    'R': 'ise from the ashes, dark one ',
    'S': 'lytherin is calling you ',
    'T': 'om Riddle ',
    'U': 'nleash your inner darkness ',
    'V': 'oldemort ',
    'W': 'ands at the ready, prepare for battle ',
    'X': ' marks the spot of doom ',
    'Y': 'ou cannot escape your fate ',
    'Z': 'ombies rise in the night ',
}

# Flag to control typing state
is_typing = False

def on_press(key):
    global is_typing
    try:
        # Check if F11 is pressed to stop the program
        if key == keyboard.Key.f11:
            print("Exiting the program...")
            return False  # Stop the listener

        # Check if the pressed key is in the mapping and we are not currently typing
        if key.char in key_mapping and not is_typing:
            is_typing = True  # Set flag to true to prevent recursion
            phrase = key_mapping[key.char]
            type_phrase(phrase)
            is_typing = False  # Reset flag after typing
            
            # Wait for 30 seconds before restarting
            print("Waiting for 30 seconds before restarting...")
            time.sleep(1)
            restart_script()

    except AttributeError:
        # Handle special keys
        pass

def type_phrase(phrase):
    # Use pyautogui to type the phrase
    pyautogui.write(phrase)  # Slight delay for realism

def restart_script():
    # Restart the script by calling the same script
    os.execv(sys.executable, ['python'] + [sys.argv[0]])

# Add a delay before starting the key listener
print("Starting in 30 seconds...")
time.sleep(10)

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    print("Press any letter key to see the magic. Press F11 to exit...")
    listener.join()
