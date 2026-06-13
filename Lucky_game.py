import random

def lucky_number_game():
    print("🎲 Welcome to the Lucky Number Game!")
    print("Guess the lucky number between 1 and 20.")

    lucky_number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == lucky_number:
                print(f"✅ Congrats! You found the lucky number {lucky_number} in {attempts} attempts!")
                break
            elif guess < lucky_number:
                print("⬆️ Try a higher number!")
            else:
                print("⬇️ Try a lower number!")
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    lucky_number_game()
