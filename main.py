password = input("Enter a password: ")
score = 0
if len(password) >= 8:
    print("✓ Length is at least 8 characters")
    score += 1
else:
    print("✗ Length is less than 8 characters")
has_upper = False

for character in password:
    if character.isupper():
        has_upper = True
if has_upper:
    print("✓ Contains uppercase letters")
    score += 1
else:
    print("✗ No uppercase letters")
has_lower = False

for character in password:
    if character.islower():
        has_lower = True
if has_lower:
    print("✓ Contains lowercase letters")
    score += 1
else:
    print("✗ No lowercase letters")
has_number = False

for character in password:
    if character.isdigit():
        has_number = True
if has_number:
    print("✓ Contains numbers")
    score += 1
else:
    print("✗ No numbers")
has_special = False

for character in password:
    if not character.isalnum():
        has_special = True
if has_special:
    print("✓ Contains special characters")
    score += 1
else:
    print("✗ No special characters")

print()

if score <= 2:
    print("Strength: Weak")
elif score == 3:
    print("Strength: Fair")
elif score == 4:
    print("Strength: Strong")
else:
    print("Strength: Very Strong")