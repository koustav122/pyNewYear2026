import random
import time
import os

# ANSI colors
colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

reset = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def splash_animation():
    for _ in range(20):
        color = random.choice(colors)
        stars = "*" * random.randint(10, 50)
        print(color + stars + reset)
        time.sleep(0.1)

def banner():
    text = "🌈 HAPPY HOLI 🌈"
    for _ in range(5):
        clear()
        color = random.choice(colors)
        print("\n\n")
        print(color + text.center(60) + reset)
        time.sleep(0.5)

# Run animation
clear()
print("\n🎨 Splashing Colors...\n")
splash_animation()
time.sleep(1)

banner()

print("\n✨ May your life be filled with vibrant colors of joy and success! ✨\n")