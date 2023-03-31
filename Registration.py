import tkinter as tk
from tkinter import messagebox
import os

def check_email(email):
    with open("emails.txt", "r") as file:
        emails = file.readlines()
    return any([email == e.strip() for e in emails])

def register_account():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    dob = dob_entry.get()
    gender = gender_var.get()
    phone = phone_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()

    if not ('@' in email and '.' in email):
        messagebox.showerror("Error", "Enter a valid email!")
        return

    if check_email(email):
        messagebox.showerror("Error", "Email already taken!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    with open("emails.txt", "w") as file:
        file.write(email + "\n")

    with open(f"{email}.txt", "w") as file:
        file.write(f"{first_name},{last_name},{dob},{gender},{phone},{email},{password}\n")

    messagebox.showinfo("Info", "Account registered!")
    app.quit()

app = tk.Tk()
app.title("Account Registration")
app.geometry("400x400")

email_label = tk.Label(app, text="Email:")
password_label = tk.Label(app, text="Password:")
confirm_password_label = tk.Label(app, text="Confirm Password:")
dob_label = tk.Label(app, text="Date of Birth:")
gender_label = tk.Label(app, text="Gender:")
phone_label = tk.Label(app, text="Phone:")
first_name_label = tk.Label(app, text="First Name:")
last_name_label = tk.Label(app, text="Last Name:")

email_entry = tk.Entry(app, width=30)
password_entry = tk.Entry(app, show="*")
confirm_password_entry = tk.Entry(app, show="*")
dob_entry = tk.Entry(app, width=30)
gender_var = tk.StringVar()
gender_entry = tk.OptionMenu(app, gender_var, "Male", "Female", "Other")
gender_var.set("Select")
phone_entry = tk.Entry(app, width=30)
first_name_entry = tk.Entry(app, width=30)
last_name_entry = tk.Entry(app, width=30)

register_button = tk.Button(app, text="Register Account", command=register_account)

email_label.grid(row=0, column=0)
email_entry.grid(row=0, column=1)
first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)
dob_label.grid(row=3, column=0)
dob_entry.grid(row=3, column=1)
gender_label.grid(row=4, column=0)
gender_entry.grid(row=4, column=1)
phone_label.grid(row=5, column=0)
phone_entry.grid(row=5, column=1)
password_label.grid(row=6, column=0)
password_entry.grid(row=6, column=1)
confirm_password_label.grid(row=7, column=0)
confirm_password_entry.grid(row=7, column=1)
register_button.grid(row=8, column=1, pady=(10, 0))

app.mainloop()