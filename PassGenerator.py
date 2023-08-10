import tkinter as tk
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        characters = ""
        if complexity == "Low":
            characters = string.ascii_lowercase + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        password_display.config(text=f"Generated Password: {password}")
    except ValueError:
        password_display.config(text="Invalid input. Please enter a valid positive integer.")


def reset_fields():
    name_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    complexity_var.set("Low")
    password_display.config(text="")


app = tk.Tk()
app.title("Password Generator")


name_label = tk.Label(app, text="Enter Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(app, width=30, font=('Arial', 14))
name_entry.pack(pady=5)


length_label = tk.Label(app, text="Enter Password Length:")
length_label.pack(pady=5)

length_entry = tk.Entry(app, width=10, font=('Arial', 14))
length_entry.pack(pady=5)


complexity_var = tk.StringVar(app)
complexity_var.set("Low")
complexity_choices = ["Low", "Medium", "High"]
complexity_menu = tk.OptionMenu(app, complexity_var, *complexity_choices)
complexity_menu.pack(pady=5)


generate_button = tk.Button(app, text="Generate Password", command=generate_password, font=('Arial', 14))
generate_button.pack(pady=10)


reset_button = tk.Button(app, text="Reset", command=reset_fields, font=('Arial', 14))
reset_button.pack(pady=5)


accept_var = tk.BooleanVar()
accept_checkbox = tk.Checkbutton(app, text="I accept the generated password.", variable=accept_var, font=('Arial', 12))
accept_checkbox.pack(pady=5)


password_display = tk.Label(app, text="", font=('Arial', 14))
password_display.pack(pady=5)


app.mainloop()
