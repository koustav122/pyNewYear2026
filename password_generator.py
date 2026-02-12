
import random
import string

print("🔐 Secure Password Generator 🔐")

# Get password length safely
while True:
    user_input = input("Enter password length (minimum 6): ")

    if not user_input.isdigit():
        print("❗ Please enter numbers only (6 or more).")
        continue

    length = int(user_input)

    if length < 6:
        print("❗ Password length must be at least 6.")
        continue

    break  # valid input

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lowercase + uppercase + digits + symbols

# Ensure strong password
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(symbols)
]

# Fill remaining length
password += random.choices(all_chars, k=length - 4)

random.shuffle(password)

final_password = "".join(password)

print("\n✅ Your secure password is:")
print(final_password)