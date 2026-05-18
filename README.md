# Clack-CLI ⌨️

A native, lightweight mechanical sound engine written in Python for the command line. `Clack-CLI` listens for global keypresses and synthesizes realistic mechanical switch tactile feedback completely in system memory (RAM), requiring zero external audio file downloads.

## 🚀 Features
* **Zero Audio Files:** Generates sharp, tactile plastic-housing bottom-out impacts dynamically using mathematically calculated sine waves.
* **Low Latency:** Configured with optimization flags specifically for Linux audio subsystems to eliminate sound lag.
* **Global Listener:** Captures keystrokes globally, letting you enjoy typing soundscapes while working across different terminal windows or applications.

## 🛠️ Prerequisites & Installation

Ensure you have Python 3 and the required system audio development libraries installed on your Linux machine:

```bash
# Install audio dependencies for Kali/Debian systems
sudo apt update
sudo apt install python3-dev libasound2-dev -y

# Install Python modules
pip3 install pygame pynput

 

