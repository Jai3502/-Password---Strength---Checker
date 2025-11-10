import string



def check_password_strength(password):
    # Conditions
    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_symbol = any(ch in string.punctuation for ch in password)
    length_ok = len(password) >= 8

    # Check strength
    if all([has_upper, has_lower, has_digit, has_symbol, length_ok]):
        print("Strong password!")
    else:
        print(" Weak password!")
        print("Here’s what’s missing:")
        if not length_ok:
            print("- Minimum length should be 8 characters")
        if not has_upper:
            print("- At least one uppercase letter required")
        if not has_lower:
            print("- At least one lowercase letter required")
        if not has_digit:
            print("- At least one number required")
        if not has_symbol:
            print("- At least one special character required")

# Take input from user
password = input("Enter your password: ")
check_password_strength(password)


