import datetime
import os

FILE_NAME = "journal.txt"

def add_entry():
    entry = input("Write your journal entry: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_NAME, "a") as f:
        f.write(f"{date} - {entry}\n")
    print("✅ Entry saved!")

def view_entries():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            print("\n📖 Your Journal Entries:\n")
            print(f.read())
    else:
        print("❌ No entries yet.")

if __name__ == "__main__":
    while True:
        print("\n--- Personal Journal ---")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
