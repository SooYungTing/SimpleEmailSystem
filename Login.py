import tkinter as tk
from tkinter import messagebox
import os


def login():
    global email_entry, password_entry

    email = email_entry.get()
    password = password_entry.get()

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_data = user.strip().split(",")
        if user_data[5] == email and user_data[6] == password:
            with open("login.txt", "w") as file:
                file.write(email)
            messagebox.showinfo("Info", "Sign in successful!")
            root.destroy()
            import inbox

    email_entry.config(highlightbackground="red", highlightthickness=2)
    password_entry.config(highlightbackground="red", highlightthickness=2)
    messagebox.showerror("Error", "Invalid email or password!")


def open_registration():
    root.destroy()
    import Registration


root = tk.Tk()
root.title("Login")
root.geometry("1000x1000")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (1000 / 2))
y = int((screen_height / 2) - (1000 / 2))

root.geometry(f"1000x1000+{x}+{y}")

root.configure(background='#C6DEFF')


email_label = tk.Label(root, text="Email:", font=("Times New Roman", 15, "bold"), bg='#C6DEFF')
password_label = tk.Label(root, text="Password:", font=("Times New Roman", 15, "bold"), bg='#C6DEFF')

email_entry = tk.Entry(root, width=30)
password_entry = tk.Entry(root, show="*", width=30)

login_button = tk.Button(root, text="Sign in", font=("Times New Roman", 15), command=login)
create_button = tk.Button(root, text="Sign up", font=("Times New Roman", 15), command=open_registration)

x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2

email_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
email_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
password_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
password_entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
create_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

root.mainloop()
