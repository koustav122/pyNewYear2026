
import time

firework = [
    "        *",
    "       ***",
    "    *********",
    "       ***",
    "        *"
]

for _ in range(3):
    for line in firework:
        print(line)
        time.sleep(0.1)
    print("\n🎆 BOOM! 🎆\n")
    time.sleep(0.5)
