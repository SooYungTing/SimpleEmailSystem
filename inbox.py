import tkinter as tk
import os
import re
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("My Mailbox")
root.geometry("1000x1000")

with open("login.txt", "r") as file:
    login_info = file.read().splitlines()

with open('emails.txt', 'r') as f:
    email_data = f.read()

emails = email_data.strip().split('\n\n')

root.configure(background='#C6DEFF')


def search_email():
    search_query = search_entry.get()

    listbox.delete(0, tk.END)

    for email in emails:
        fields = email.split(",")
        for field in fields:
            if search_query.lower() in field.lower():
                subject_field = re.findall('Subject: .*', email)
                if len(subject_field) > 0:
                    subject = subject_field[0].replace('Subject: ', '').strip()
                else:
                    subject = '(no subject)'
                listbox.insert(tk.END, subject)
                break


def sign_out():
    os.remove("login.txt")
    root.destroy()


def get_email_data(subject):
    for email in emails:
        if f"Subject: {subject}" in email:
            return email


def delete_email():
    selection = listbox.curselection()
    if selection:
        subject = listbox.get(selection[0])
        email_data = get_email_data(subject)
        emails.remove(email_data)
        listbox.delete(selection[0])


def show_email_data(event):
    selection = event.widget.curselection()
    if selection:
        subject = event.widget.get(selection[0])
        email_data = get_email_data(subject)
        email_window = tk.Toplevel(root)
        email_window.title(subject)
        email_window.geometry("800x600")

        email_text = tk.Text(email_window)
        email_text.pack(fill="both", expand=True)

        email_text.insert(tk.END, email_data)


def inbox():
    filtered_emails = []
    for email in emails:
        to_field = re.findall('To: .*', email)
        if len(to_field) > 0:
            to_address = to_field[0].replace('To: ', '').strip()
        else:
            to_address = None
        if to_address == login_info[0]:
            subject_field = re.findall('Subject: .*', email)
            if len(subject_field) > 0:
                subject = subject_field[0].replace('Subject: ', '').strip()
            else:
                subject = '(no subject)'
            filtered_emails.append(subject)


filtered_emails = []
for email in emails:
    to_field = re.findall('To: .*', email)
    if len(to_field) > 0:
        to_address = to_field[0].replace('To: ', '').strip()
    else:
        to_address = None
    if to_address == login_info[0]:
        subject_field = re.findall('Subject: .*', email)
        if len(subject_field) > 0:
            subject = subject_field[0].replace('Subject: ', '').strip()
        else:
            subject = '(no subject)'
        filtered_emails.append(subject)

def sent_email():
    listbox.delete(0, tk.END)
    sent_emails = []
    for email in emails:
        from_field = re.findall('From: .*', email)
        if len(from_field) > 0:
            from_address = from_field[0].replace('From: ', '').strip()
        else:
            from_address = None
        if from_address == login_info[0]:
            subject_field = re.findall('Subject: .*', email)
            if len(subject_field) > 0:
                subject = subject_field[0].replace('Subject: ', '').strip()
            else:
                subject = '(no subject)'
            sent_emails.append(subject)
    for email in sent_emails:
        listbox.insert(tk.END, email)


def compose_email():
    import email


search_frame = tk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X)

search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Search", command=search_email)
search_button.pack(side=tk.LEFT, padx=10)

button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

compose_button = tk.Button(button_frame, text="Compose", command=compose_email)
compose_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="nw")

sent_button = tk.Button(button_frame, text="Sent", command=sent_email)
sent_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="nw")


delete_button = tk.Button(button_frame, text="Delete", command=delete_email)
delete_button.pack(side=tk.LEFT, padx=10, pady=10, anchor="nw")

sign_out_button = tk.Button(root, text="Sign Out", command=sign_out)
sign_out_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="se")

listbox = tk.Listbox(root, width=80)
listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

for email in filtered_emails:
    listbox.insert(tk.END, email)

listbox.bind("<<ListboxSelect>>", show_email_data)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (1000 / 2))
y = int((screen_height / 2) - (1000 / 2))

root.geometry(f"1000x1000+{x}+{y}")

root.mainloop()
