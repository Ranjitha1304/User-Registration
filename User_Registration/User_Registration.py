import re

def is_valid_username(username):
    return username.isalpha() and len(username) >= 3

def is_valid_email(email):
    # Basic email regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    has_digit = re.search(r'[0-9]', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    if not (has_digit or has_special):
        return False
    return True

def register_user():
    print("=== User Registration ===")
    
    while True:
        username = input("Enter username: ")
        if not is_valid_username(username):
            print("Username must be only characters and minimum length of 3.")
        else:
            break

    while True:
        email = input("Enter email: ")
        if not is_valid_email(email):
            print("Invalid email format.")
        else:
            break

    while True:
        password = input("Enter password: ")
        if not is_strong_password(password):
            print("Password must be at least 8 characters long, with uppercase, lowercase, number or special character.")
            continue
        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            print("Passwords do not match.")
        else:
            break

    print("Registration successful!")
    return {
        "username": username,
        "email": email,
        "password": password  
    }

user_data = register_user()
print("\nRegistered User:")
print(user_data)
