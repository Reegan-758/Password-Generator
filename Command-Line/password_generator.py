import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_user_preferences():
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters? (yes/no): ").lower() in ["yes", "y"]
    use_numbers = input("Include numbers? (yes/no): ").lower() in ["yes", "y"]
    use_symbols = input("Include symbols? (yes/no): ").lower() in ["yes", "y"]
    
    return length, use_letters, use_numbers, use_symbols

def main():
    print("Welcome to the Command-Line Password Generator!")
    length, use_letters, use_numbers, use_symbols = get_user_preferences()
    try:
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
