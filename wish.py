import time

# Try importing colorama, else use fallback
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

def color_text(text, color=""):
    if COLOR:
        return color + text
    return text

print(color_text("🎆 Countdown Begins 🎆", "\033[96m"))
time.sleep(1)

for i in range(5, 0, -1):
    print(color_text(f"{i}...", "\033[93m"))
    time.sleep(1)

print()
print(color_text("🎉✨ HAPPY NEW YEAR 2026 ✨🎉", "\033[92m"))
print(color_text("🌟 May this year bring happiness, success & peace 🌟", "\033[95m"))
print(color_text("🥳 Wishing everyone joy and prosperity 🥳", "\033[94m"))