import re

# 1. Password list
passwords = ["abc", "123456", "Pass@123", "Admin"]

# 2. Validation function
def validate_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"\d", pwd):        # at least 1 number
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):  # special char
        return False
    return True

# 3. Test & report
print("PASSWORD STRENGTH REPORT")
print("-" * 30)

for pwd in passwords:
    if validate_password(pwd):
        print(f"{pwd}  --> PASS ✅")
    else:
        print(f"{pwd}  --> FAIL ❌")
