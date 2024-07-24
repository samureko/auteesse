def validate_password(password):
    if len(password) < 8:
        return False
    elif not any(char.isdigit() for char in password):
        return False
    elif not any(char.isalpha() for char in password):
        return False
    else:
        return True

# Example usage
user_password = "SecurePassword123"
if validate_password(user_password):
    print("Password meets the criteria. Account created.")
else:
    print("Password does not meet the criteria. Please choose a different password.")
