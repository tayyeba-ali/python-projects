          #password Genrater 2
  
import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    while True:
        password = ''.join(random.choice(characters) for _ in range(length))
        
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            (not use_digits or any(c.isdigit() for c in password)) and
            (not use_symbols or any(c in string.punctuation for c in password))):
            break 

    return password

length = int(input("Enter the length of password: "))
use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").strip().lower() == 'y'

password = generate_password(length, use_digits, use_symbols)

print("\nGenerated Password:", password)
