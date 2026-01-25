
import time

# Try colorama, fallback if not installed
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    SAFFRON = Fore.YELLOW + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    BLUE = Fore.BLUE + Style.BRIGHT
except ImportError:
    SAFFRON = WHITE = GREEN = BLUE = ""

def slow_print(text, delay=0.05):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

print(SAFFRON + "🧡🤍💚 Happy Republic Day 🧡🤍💚\n")
time.sleep(0.5)

slow_print(WHITE + "📜 Celebrating the Spirit of the Constitution 📜", 0.05)
slow_print(BLUE + "⚖️ Justice • Liberty • Equality • Fraternity ⚖️", 0.05)
slow_print(GREEN + "🌿 Proud to be an Indian 🌿", 0.05)

print("\n"  +  SAFFRON +"🇮🇳 26 January – Republic Day of India 🇮🇳")
print(WHITE + "🙏 Let us honor our freedom fighters and constitution 🙏")
print(GREEN + "✨ Unity in Diversity ✨")
