import tkinter as tk
from tkinter import messagebox, ttk
import os

def check_email(email):
    with open("users.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        user_info = line.strip().split(",")
        if user_info[5] == email:
            return True
    return False

def register_account():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    day = day_var.get()
    month = month_var.get()
    year = year_var.get()
    dob = f"{day} {month} {year}"
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

    with open("users.txt", "a") as file:
        file.write(f"{first_name},{last_name},{dob},{gender},{phone},{email},{password}\n")

    messagebox.showinfo("Info", "Account registered!")
    root.quit()

root = tk.Tk()
root.title("Account Registration")
root.geometry("1000x1000")

email_label = tk.Label(root, text="Email:")
password_label = tk.Label(root, text="Password:")
confirm_password_label = tk.Label(root, text="Confirm Password:")
dob_label = tk.Label(root, text="Date of Birth:")
gender_label = tk.Label(root, text="Gender:")
phone_label = tk.Label(root, text="Phone:")
first_name_label = tk.Label(root, text="First Name:")
last_name_label = tk.Label(root, text="Last Name:")

email_entry = tk.Entry(root, width=30)
password_entry = tk.Entry(root, show="*")
confirm_password_entry = tk.Entry(root, show="*")
day_var = tk.StringVar()
month_var = tk.StringVar()
year_var = tk.StringVar()
day_options = list(range(1, 32))
month_options = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
year_options = list(range(1900, 2023))
day_combo = ttk.Combobox(root, textvariable=day_var, values=day_options, state='readonly', width=5)
month_combo = ttk.Combobox(root, textvariable=month_var, values=month_options, state='readonly', width=10)
year_combo = ttk.Combobox(root, textvariable=year_var, values=year_options, state='readonly', width=7)
day_var.set("Date")
month_var.set("Month")
year_var.set("Year")
gender_var = tk.StringVar()
gender_entry = tk.OptionMenu(root, gender_var, "Male", "Female", "Rather Not Say", "Other")
gender_var.set("Select")
phone_entry = tk.Entry(root, width=30)
first_name_entry = tk.Entry(root, width=30)
last_name_entry = tk.Entry(root, width=30)

register_button = tk.Button(root, text="Register Account", command=register_account)

email_label.grid(row=0, column=0)
email_entry.grid(row=0, column=1)
first_name_label.grid(row=1, column=0)
first_name_entry.grid(row=1, column=1)
last_name_label.grid(row=2, column=0)
last_name_entry.grid(row=2, column=1)
dob_label.grid(row=3, column=0, padx=(0, 10))
day_combo.grid(row=3, column=1, padx=(0, 5), sticky="w")
month_combo.grid(row=3, column=1, padx=(67, 5), sticky="w")
year_combo.grid(row=3, column=1, padx=(180, 0), sticky="w")
gender_label.grid(row=4, column=0)
gender_entry.grid(row=4, column=1)
phone_label.grid(row=5, column=0)
phone_entry.grid(row=5, column=1)
password_label.grid(row=6, column=0)
password_entry.grid(row=6, column=1)
confirm_password_label.grid(row=7, column=0)
confirm_password_entry.grid(row=7, column=1)
register_button.grid(row=8, column=1, pady=(10, 0))

root.mainloop()