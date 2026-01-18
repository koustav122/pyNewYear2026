import time
print(" ⌚Live Clock (Press Ctrl+C to stop)")
while True:
    print(time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)