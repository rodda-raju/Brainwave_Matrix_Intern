import re

# Common weak passwords (you can expand this list)
COMMON_PASSWORDS = ["password", "123456", "qwerty", "abc123", "letmein", "admin", "welcome"]

def check_password_strength(password):
    strength_score = 0
    recommendations = []

    # Length check
    if len(password) >= 8:
        strength_score += 1
    else:
        recommendations.append("Increase password length to at least 8 characters.")

    # Upper and lower case check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength_score += 1
    else:
        recommendations.append("Use both uppercase and lowercase letters.")

    # Number check
    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        recommendations.append("Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        recommendations.append("Use at least one special character (!@#$%^&* etc.).")

    # Common password check
    if password.lower() in COMMON_PASSWORDS:
        strength_score = 0  # Weak if it's a common password
        recommendations.append("Avoid using common passwords.")

    # Strength rating
    strength_levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Moderate",
        3: "Strong",
        4: "Very Strong"
    }
    
    return strength_levels[strength_score], recommendations

# User input
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
if suggestions:
    print("Suggestions to improve your password:")
    for suggestion in suggestions:
        print(f"- {suggestion}")