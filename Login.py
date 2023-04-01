import tkinter as tk
from tkinter import messagebox
import os

def login():
    email = email_entry.get()
    password = password_entry.get()

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_data = user.strip().split(",")
        if user_data[5] == email and user_data[6] == password:
            messagebox.showinfo("Info", "Login successful!")
            app.quit()
            return

    messagebox.showerror("Error", "Invalid email or password!")

app = tk.Tk()
app.title("Login")
app.geometry("300x150")

email_label = tk.Label(app, text="Email:")
password_label = tk.Label(app, text="Password:")

email_entry = tk.Entry(app, width=30)
password_entry = tk.Entry(app, show="*")

login_button = tk.Button(app, text="Login", command=login)

email_label.grid(row=0, column=0, padx=5, pady=5)
email_entry.grid(row=0, column=1, padx=5, pady=5)
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)
login_button.grid(row=2, column=1, pady=(10, 0))

app.mainloop()
