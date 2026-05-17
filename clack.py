#!/usr/bin/env python3
import os
import sys
import math
import array
from pynput import keyboard

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

SAMPLE_RATE = 44100
pygame.mixer.init(frequency=SAMPLE_RATE, size=-16, channels=1, buffer=256)

def generate_mechanical_clack():
    duration = 0.06
    num_samples = int(SAMPLE_RATE * duration)
    buf = array.array('h', [0] * num_samples)
    for i in range(num_samples):
        t = i / SAMPLE_RATE
        freq1 = 280
        freq2 = 1100
        decay = math.exp(-65 * t)
        wave = (0.6 * math.sin(2 * math.pi * freq1 * t) + 0.4 * math.sin(2 * math.pi * freq2 * t)) * decay
        buf[i] = int(wave * 32767 * 0.5)
    return pygame.mixer.Sound(buffer=buf)

click_sound = generate_mechanical_clack()

def on_press(key):
    try:
        click_sound.play()
    except Exception:
        pass

def print_banner():
    print("-" * 55)
    print(" ⌨️  Clack-CLI (Synth Mode) is now active...")
    print(" 🛠️  Developed By: SUDAIS AHMAD DURANI")
    print(" 🛑 Press Ctrl+C to terminate the engine.")
    print("-" * 55)

if __name__ == "__main__":
    print_banner()
    with keyboard.Listener(on_press=on_press) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\n[+] Clack-CLI stopped successfully. Goodbye!")
            sys.exit(0)
