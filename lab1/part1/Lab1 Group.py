import string
import random

# Input and validation for total password length
valid_input = False
while not valid_input:
    try:
        total_length = int(input("Enter the total length of the password (min 8): "))
        if total_length >= 8:
            valid_input = True
        else:
            print("Password must be at least 8 characters. Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Input and validation for the number of letters
valid_input = False
while not valid_input:
    try:
        num_letters = int(input("Enter the number of letters: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a number.")

# Input and validation for the number of digits
valid_input = False
while not valid_input:
    try:
        num_digits = int(input("Enter the number of digits: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a number.")

# Input and validation for the number of special characters
valid_input = False
while not valid_input:
    try:
        num_specials = int(input("Enter the number of special characters: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a number.")

# Ensure the total number of components matches the total length
while num_letters + num_digits + num_specials != total_length:
    print("The total of letters, digits, and special characters must equal the total length.")
    
    # Input and validation for the number of letters
    valid_input = False
    while not valid_input:
        try:
            num_letters = int(input("Enter the number of letters: "))
            valid_input = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input and validation for the number of digits
    valid_input = False
    while not valid_input:
        try:
            num_digits = int(input("Enter the number of digits: "))
            valid_input = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Input and validation for the number of special characters
    valid_input = False
    while not valid_input:
        try:
            num_specials = int(input("Enter the number of special characters: "))
            valid_input = True
        except ValueError:
            print("Invalid input. Please enter a number.")

# Generate random password components
letters = random.choices(string.ascii_letters, k=num_letters)
digits = random.choices(string.digits, k=num_digits)
specials = random.choices("!@#$%^&*()_+", k=num_specials)

# Combine and shuffle them
password_list = letters + digits + specials
random.shuffle(password_list)

# Join to form the final password string
password = ''.join(password_list)

# Output the password
print("Generated password:", password)


