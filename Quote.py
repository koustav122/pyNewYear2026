import requests
import random
import time

def get_quote():
    response = requests.get("https://type.fit/api/quotes")
    if response.status_code == 200:
        quotes = response.json()
        return random.choice(quotes)
    else:
        return {"text": "Keep pushing forward!", "author": "Unknown"}

def display_quote():
    quote = get_quote()
    text = quote.get("text", "Stay motivated!")
    author = quote.get("author", "Anonymous")
    print("\n✨ Inspirational Quote ✨")
    print(f"\"{text}\"")
    print(f"— {author}\n")

if __name__ == "__main__":
    print("Welcome to the Random Quote Generator!")
    while True:
        display_quote()
        time.sleep(5)  # refresh every 5 seconds
