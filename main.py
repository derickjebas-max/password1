print("===================================")
print("     PASSWORD STRENGTH ANALYZER")
print("===================================")

password = input("Enter your password: ")

upper = 0
lower = 0
number = 0
special = 0

for ch in password:
    if 'A' <= ch <= 'Z':
        upper = 1
    elif 'a' <= ch <= 'z':
        lower = 1
    elif '0' <= ch <= '9':
        number = 1
    else:
        special = 1

score = 0

if len(password) >= 8:
    score += 1
if upper == 1:
    score += 1
if lower == 1:
    score += 1
if number == 1:
    score += 1
if special == 1:
    score += 1

print("\n========== PASSWORD REPORT ==========")
print("Password Length:", len(password))
print("Uppercase Letters:", "Available" if upper else "Missing")
print("Lowercase Letters:", "Available" if lower else "Missing")
print("Numbers:", "Available" if number else "Missing")
print("Special Characters:", "Available" if special else "Missing")

print("\nPassword Strength:")
if score <= 2:
    print("WEAK")
elif score <= 4:
    print("MEDIUM")
else:
    print("STRONG")

print("\n========== SUGGESTIONS ==========")
if len(password) < 8:
    print("- Use at least 8 characters.")
if upper == 0:
    print("- Add uppercase letters.")
if lower == 0:
    print("- Add lowercase letters.")
if number == 0:
    print("- Add numbers.")
if special == 0:
    print("- Add special characters.")
if score == 5 and len(password) >= 12:
    print("Your password meets all the basic checks!")

print("\nThank you for using Password Analyzer!")
