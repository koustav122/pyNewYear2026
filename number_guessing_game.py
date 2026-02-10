
import random
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess = input("Enter your guess (or type 'exit' to quit)): ")
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
        break
