SPECIAL_CHARACTERS = "!@#$%^&*()~"

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password must include at least one uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password must include at least one lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password must include at least one number.")

    if any(char in SPECIAL_CHARACTERS for char in password):
        score += 1
    else:
        feedback.append("Password must include at least one special character.")

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return score, feedback, strength


print("Password Strength Analyzer")
print("Type 'exit' anytime to quit.\n")

while True:
    user_password = input("Enter your password: ")

    if user_password.lower() == "exit":
        print("Goodbye.")
        break

    score, feedback, strength = analyze_password(user_password)

    print("\nPassword Strength:", strength)
    print("Score:", str(score) + "/5")

    if score == 5:
        print("Great job! You created a strong password.")
        print("You can type 'exit' to stop the program.")

    if len(feedback) > 0:
        print("Suggestions:")
        for item in feedback:
            print("-", item)

    print()
