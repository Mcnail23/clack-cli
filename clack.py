#!/usr/bin/env python3
"""
===================================================================
   ______ _               _         _____ _      _____ 
  / ____/| |             | |       / ____| |    |_   _|
 | |     | |  __ _  ___  | | __   | |    | |      | |  
 | |     | | / _` |/ __| | |/ /   | |    | |      | |  
 | |____ | || (_| | (__  |   <    | |____| |____ _| |_ 
  \_____||_| \__,_|\___| |_|\_\    \_____|______|_____|
                                                       
 Tool Name: Clack-CLI (Synth-Engine v2.0)
 Developed By: SUDAIS AHMAD DURANI (Mcnail23)
 Description: A native, lightweight mechanical sound engine
              requiring zero external file downloads.
===================================================================
"""

import os
import sys
import math
import array
from pynput import keyboard

# Hide the annoying pygame welcome banner on startup
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

# Initialize audio engine with low latency settings
SAMPLE_RATE = 44100
pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=256)

def generate_mechanical_clack():
    """Generates a sharp tactile mechanical switch sound completely in RAM."""
    duration = 0.05  # 50ms fast click response
    num_samples = int(SAMPLE_RATE * duration)
    buf = array.array('h', [0] * num_samples)
    
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        
        # Audio frequencies simulating standard plastic keycap housing impacts
        freq1 = 300  # Deep mechanical bottom-out thud
        freq2 = 1200 # Crisp tactile snap metallic chime
        
        # Aggressive exponential decay simulating the rapid drop-off of physical impact
        decay = math.exp(-75 * t)
        
        # Combine wave layers
        wave = (0.6 * math.sin(2 * math.pi * freq1 * t) + 
                0.4 * math.sin(2 * math.pi * freq2 * t)) * decay
        
        # Standardize data to 16-bit signed integers
        buf[i] = int(wave * 32767 * 0.5)
        
    return pygame.mixer.Sound(buffer=buf)

# Cache generated sound matrix directly into volatile memory
click_sound = generate_mechanical_clack()

def on_press(key):
    try:
        click_sound.play()
    except Exception:
        pass

def print_banner():
    # Adding 'r' before the string to prevent SyntaxWarnings from backslashes
    banner = r"""
===================================================================
   ______ _               _         _____ _      _____ 
  / ____/| |             | |       / ____| |    |_   _|
 | |     | |  __ _  ___  | | __   | |    | |      | |  
 | |     | | / _` |/ __| | |/ /   | |    | |      | |  
 | |____ | || (_| | (__  |   <    | |____| |____ _| |_ 
  \_____||_| \__,_|\___| |_|\_\    \_____|______|_____|
==================================================================="""
    print(banner)
    print(" ⌨️  CLACK-CLI v2.0 IS LIVE")
    print(" 👤 AUTHOR: SUDAIS AHMAD DURANI (Mcnail23)")
    print(" 🛑 Press Ctrl+C in this window to stop the sound engine.")
    print("===================================================================")

if __name__ == "__main__":
    print_banner()
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[+] Clack-CLI engine stopped smoothly. Goodbye!")
            sys.exit(0)
