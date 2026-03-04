# Happy Holi Wish Program 🌈

import time

# ANSI color codes
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

reset = "\033[0m"

message = """
🌸 Wishing You a Very Happy Holi! 🌸
May your life be filled with
Colors of Happiness 🎨
Colors of Success 🌟
Colors of Love ❤️
And endless Joy 😄
"""

print("\n")

for color in colors:
    print(color + message + reset)
    time.sleep(0.5)

print("\n🎉 Have a Safe and Colorful Holi! from KmPro 🎉\n")