import re
import string

def password_strength(password, username=None):

    # Check password length
    if len(password) < 8:
        return "Password is too short, must be at least 8 characters long."

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."

    # Check for numbers
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one number."

    # Check for special characters
    if not re.search(r'[@$!%*?_&^#]', password):
        return "Password must contain at least one special character."

    # Check for common passwords
    common_passwords = ["password", "123456", "qwerty", "letmein", "welcome", "123123", "qwerty123"]
    if password.lower() in common_passwords:
        return "Password is too common, choose a more unique one."

    # Check for repetitive characters
    if re.search(r'(.)\1{2,}', password):
        return "Password should not contain repeating characters (e.g., 'aaa' or '111')."

    # Check if password is similar to username
    if username and username.lower() in password.lower():
        return "Password should not contain the username."

    # Check for dictionary words
    dictionary_words = ["password", "123456", "qwerty", "admin", "user", "welcome", "letmein"]
    if any(word in password.lower() for word in dictionary_words):
        return "Password contains easily guessable words. Choose a more complex one."

    # Check for entropy
    character_classes = [
        sum(c in string.ascii_lowercase for c in password),
        sum(c in string.ascii_uppercase for c in password),
        sum(c in string.digits for c in password),
        sum(c in string.punctuation for c in password),
    ]
    if any(count == 0 for count in character_classes):
        return "Password does not have enough variety. Include characters from all types (lowercase, uppercase, digits, special)."

    return "Password is strong."


# Input and check password
password = input("Enter your password: ")
username = input("Enter your username (optional): ")
print(password_strength(password, username))
