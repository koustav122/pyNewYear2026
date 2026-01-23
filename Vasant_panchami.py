import time
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    YELLOW = Fore.YELLOW + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    CYAN = Fore.CYAN
except ImportError:
    YELLOW = WHITE = CYAN = ""
    def slow_print(text, delay=0.05):
        for ch in text:
            print(ch, end=" ", flush=True)
            time.sleep(delay)
            print()
print(YELLOW + "🌼✨ Happy Vasant Panchami ✨🌼\n")
time.sleep(0.5)
print(WHITE + "🙏 Saraswati Puja Greetings 🙏", 0.06)
print(CYAN + "📚 May Goddess Saraswati bless you with knowledge and wisdom 📚", 0.04)
print(YELLOW + "🎶 Let learning, creativity, and peace fill your life 🎶", 0.04)

print( WHITE + "🙏 সরস্বতী পূজার শুভেচ্ছা 🙏")
print(CYAN + "📖 বিদ্যার দেবী মা সরস্বতীর কৃপায় জীবন ভরে উঠুক জ্ঞান ও প্রজ্ঞায় 📖", 0.04)
print(YELLOW + "🎵 শিক্ষা, সৃজনশীলতা ও শান্তিতে ভরে উঠুক আপনার জীবন 🎵", 0.04)
print(WHITE + "🌼 শুভ বসন্ত পঞ্চমী 🌼", 0.04)