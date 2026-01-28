# Password Strength GUI Tester

## 1. Project Title & Goal

A simple Python GUI application that checks whether a password is strong enough based on length, numeric, and special‑character rules using regex.

---

## 2. Setup Instructions

Follow these steps to run the project locally:

### Prerequisites

* Python 3.x installed on your system
* No external libraries required (Tkinter is built‑in)

### Steps to Run

```bash
# Clone the repository
git clone https://github.com/USERNAME/Password-Strength-GUI.git

# Move into the project directory
cd Password-Strength-GUI

# Run the application
python password_gui.py
```

---

## 3. The Logic (How I Thought)

### Why I chose this approach

* I used **regex** because it is the most efficient and standard way to validate password rules.
* **Tkinter** was chosen for the GUI since it is lightweight, built into Python, and easy to use for quick interfaces.
* The logic is separated into functions to keep the code clean and readable.

### Hardest bug I faced & how I fixed it

* The main issue was the **special character regex not matching correctly**.
* I fixed it by carefully escaping special characters inside the regex pattern and testing it with multiple passwords.

---

## 4. Output Screenshots

Below are screenshots proving the application works correctly:

### Password FAIL Example

<img width="400" height="200" alt="Password Strength Tester 28-01-2026 11_51_24" src="https://github.com/user-attachments/assets/1b594795-6385-4ae9-9ab8-15ec657fd35b" />


### Password PASS Example

<img width="1185" height="750" alt="Screenshot (11)" src="https://github.com/user-attachments/assets/0dff1056-efd6-456b-98d5-547d7e453e88" />


---

## 5. Future Improvements

If I had 2 more days, I would:

* Add **real‑time password strength meter** (Weak / Medium / Strong)
* Allow **bulk password testing** from a list
* Convert the project into a **.exe file** for Windows users
* Improve UI design with better styling and icons

---

### Author

**Koshik Barkhane**
