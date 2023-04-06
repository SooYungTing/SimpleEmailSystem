import tkinter as tk
import os
from datetime import datetime



def display_emails(logged_in_email):
    emails_listbox.delete(0, tk.END)
    try:
        with open(f"{logged_in_email}.txt", "r") as file:
            lines = file.readlines()
            emails = []
            for i in range(0, len(lines), 5):
                email_parts = lines[i:i + 5]
                email = {
                    "From": email_parts[0].strip()[6:],
                    "To": email_parts[1].strip()[4:],
                    "Subject": email_parts[3].strip(),
                    "Message": email_parts[4].strip(),
                    "Date": datetime.strptime(email_parts[2].strip()[6:], '%Y-%m-%d %H:%M:%S.%f')
                }
                emails.append(email)
            emails = sorted(emails, key=lambda x: x["Date"], reverse=True)
            for email in emails:
                if email["To"] == logged_in_email:
                    emails_listbox.insert(tk.END, f"From: {email['From']}")
                    emails_listbox.insert(tk.END, f"Subject: {email['Subject']}")
                    emails_listbox.insert(tk.END, f"Date: {email['Date'].strftime('%b %d, %Y %I:%M %p')}")
                    emails_listbox.insert(tk.END, "")
    except FileNotFoundError:
        print("No emails found.")


def open_email(event):
    selection = emails_listbox.curselection()
    if selection:
        selected_email = emails_listbox.get(selection)
        email_window = tk.Toplevel(root)
        email_window.title("Email")
        email_window.geometry("500x500")
        email_text = tk.Text(email_window)
        email_text.pack()
        email_text.insert(tk.END, selected_email)


def show_inbox(logged_in_email):
    global from_email
    from_email = logged_in_email
    inbox_file = f"{from_email}.txt"
    if not os.path.exists(inbox_file):
        with open(inbox_file, "w") as file:
            pass
    display_emails(from_email)


def logout():
    root.destroy()


def compose():
    import email
    email.send_email(from_email)


root = tk.Tk()
root.title("Inbox")
root.geometry("1000x1000")

emails_label = tk.Label(root, text="Inbox", font=("Helvetica", 20))
emails_listbox = tk.Listbox(root, width=60, font=("Helvetica", 12), bg="white", fg="black")
scrollbar = tk.Scrollbar(root, command=emails_listbox.yview)
emails_listbox.config(yscrollcommand=scrollbar.set)

show_inbox("example@gmail.com")
emails_listbox.bind("<<ListboxSelect>>", open_email)

send_button = tk.Button(root, text="Compose", font=("Helvetica", 12), command=compose)
logout_button = tk.Button(root, text="Logout", font=("Helvetica", 12), command=logout)

emails_label.pack(pady=10)
emails_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
scrollbar.pack(side=tk.LEFT, fill=tk.Y, pady=10)
logout_button.pack(side=tk.BOTTOM, pady=10)
send_button.pack(side=tk.BOTTOM, pady=20)

root.mainloop()
