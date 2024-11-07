import random
import time
from colorama import Fore, init
import sys

# Initialize colorama for colored text
init(autoreset=True)

# Function to display ASCII art banner line by line
def display_banner():
    print(Fore.GREEN + " ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓ ▒█████   ▒█████   ██▓    ")
    print(Fore.GREEN + "▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ")
    print(Fore.GREEN + "▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ")
    print(Fore.GREEN + "░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ")
    print(Fore.GREEN + "░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄  ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒")
    print(Fore.GREEN + " ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░")
    print(Fore.GREEN + " ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░")
    print(Fore.GREEN + " ░  ░░ ░  ░   ▒   ░        ░ ░░ ░   ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ")
    print(Fore.GREEN + " ░  ░  ░      ░  ░░ ░      ░  ░                ░ ░      ░ ░      ░  ░")

# List of startup phrases for the "hacking" sequence
startup_phrases = [
    "Initializing hacking module...",
    "Bypassing firewall...",
    "Hacking into the mainframe...",
    "Establishing secure connection...",
    "Accessing encrypted data...",
    "Gathering user credentials...",
    "Decrypting passwords...",
    "Extracting sensitive information...",
    "Uploading trojan...",
    "Complete access granted!"
]

# Sample lists for realistic name and pet-based passwords
male_names = ["James", "Ethan", "Michael", "Alexander", "Noah", "Benjamin", "William", "Lucas", "Mason"]
female_names = ["Olivia", "Isabella", "Emma", "Ava", "Mia", "Sophia", "Charlotte", "Amelia", "Harper", "Evelyn"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", 
              "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", 
              "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", 
              "Walker", "Young", "Allen", "King", "Wright"]
pet_names = ["Bailey", "Max", "Bella", "Charlie", "Lucy", "Daisy", "Molly", "Buddy", "Rocky", "Sadie", "Toby", "Luna", 
             "Cooper", "Zoe", "Buster", "Lola", "Oliver", "Bear", "Maggie", "Milo", "Rosie", "Chloe", "Roxy", 
             "Dexter", "Ginger"]

# Word parts for username combinations
word_parts = ["dark", "shadow", "light", "wolf", "star", "void", "alpha", "beta", "omega", "spark", "night", "fire", 
              "stone", "storm", "blade", "rocket", "dino", "xXcOd", "xXmon", "xX_vOiD"]
suffixes = ["_lord", "_master", "_king", "123", "99", "pro", "gamer", "elite", "alpha", "prime", "_xyz", "com", "<3", 
            "_i<3him", "_i<3her", "V0Id", "_heartsforhimXx", "_heartsforherXx"]

# Function to generate realistic-looking usernames
def generate_username():
    # Decide randomly if this will be a real name or a word-based username
    if random.random() < 0.5:  # 50% chance
        first_name = random.choice(male_names + female_names)
        last_name = random.choice(last_names)
        return f"{first_name}{last_name}{random.randint(1, 99)}"
    else:
        return random.choice(word_parts) + random.choice(word_parts) + random.choice(suffixes)

# Function to generate realistic-looking passwords
def generate_password():
    if random.random() < 0.45:  # 45% chance for readable combinations
        base = random.choice(["mama", "dada", "dog", "cat", "pet", "buddy", "friend", "bestfriend",])
        if base == "mom":
            name = random.choice(female_names + pet_names)
        elif base == "dad":
            name = random.choice(male_names + pet_names)
        else:
            name = random.choice(male_names + female_names + pet_names)
        return f"{base}{name}{random.randint(100, 999)}"
    else:
        return ''.join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()", k=12))

# Function to simulate the "hacking" process
def hack_website():
    print(Fore.GREEN + "Enter the website URL to hack:")
    target_website = input(Fore.CYAN + "Website URL: ")

    print(Fore.GREEN + f"\nStarting hack on {target_website}...\n")
    time.sleep(1)

    # Display the startup sequence
    for phrase in startup_phrases:
        print(Fore.GREEN + phrase)
        time.sleep(0.5)

    print(Fore.GREEN + "\n[+] Success! Extracting user data...\n")
    time.sleep(1)

    # Generate and display 1000001  usernames and passwords
    for i in range(1000001):
        username = generate_username()
        password = generate_password()
        print(Fore.GREEN + f"Username: {username}   Password: {password}")
        time.sleep(0.0000000000000001)  # Simulate a slight delay for a realistic effect

    print(Fore.GREEN + "\nHacking simulation complete. All credentials 'retrieved'.\n")

# Main menu function
def main():
    # Display banner and menu options
    display_banner()
    print(Fore.GREEN + "\nWelcome to Author's HACKTOOL!")
    print(Fore.GREEN + "1. Hack website - steal website credentials")
    print(Fore.GREEN + "2. Exit\n")

    choice = input(Fore.CYAN + "Select an option: ")

    if choice == '1':
        hack_website()
    elif choice == '2':
        print(Fore.GREEN + "Exiting program.")
        sys.exit()
    else:
        print(Fore.RED + "Invalid option. Please try again.")

if __name__ == "__main__":
    main()
