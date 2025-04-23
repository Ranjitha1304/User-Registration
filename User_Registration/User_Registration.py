import re

def is_valid_username(username):
    return username.isalpha() and len(username) >= 3

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password) and not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        errors.append("Password must contain at least one digit or one special character.")
    return errors

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
        password_errors = validate_password(password)
        if password_errors:
            for err in password_errors:
                print(err)
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
