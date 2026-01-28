import re
import tkinter as tk
from tkinter import messagebox

# Password validation logic
def validate_password(pwd):
    if len(pwd) < 8:
        return False
    if not re.search(r"\d", pwd):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd):
        return False
    return True

# Button action
def check_password():
    pwd = entry.get()
    if validate_password(pwd):
        result_label.config(text="Password Strength: PASS ✅", fg="green")
    else:
        result_label.config(text="Password Strength: FAIL ❌", fg="red")

# GUI Window
root = tk.Tk()
root.title("Password Strength Tester")
root.geometry("400x200")

# UI Elements
tk.Label(root, text="Enter Password", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Password", command=check_password).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
