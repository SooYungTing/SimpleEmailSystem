import tkinter as tk
import os
import re

# create a GUI window
root = tk.Tk()
root.title("My Mailbox")
root.geometry("1000x1000")

# read the login information from a text file
with open("login.txt", "r") as file:
    login_info = file.read().splitlines()

with open('emails.txt', 'r') as f:
    email_data = f.read()

# Split email data into individual emails
emails = email_data.strip().split('\n\n')

def search_email():
    # get the search query from the entry widget
    search_query = search_entry.get()

    # clear the listbox
    listbox.delete(0, tk.END)

    # iterate over each email and search for the query in all fields
    for email in emails:
        fields = email.split(",")
        for field in fields:
            if search_query.lower() in field.lower():
                listbox.insert(tk.END, email)
                break


def sign_out():
    os.remove("login.txt")
    root.destroy()

filtered_emails = []
for email in emails:
    # Extract "To" field from email
    to_field = re.findall('To: .*', email)
    if len(to_field) > 0:
        to_address = to_field[0].replace('To: ', '').strip()
    else:
        to_address = None
    if to_address == login_info[0]:
        # Extract subject field from email
        subject_field = re.findall('Subject: .*', email)
        if len(subject_field) > 0:
            subject = subject_field[0].replace('Subject: ', '').strip()
        else:
            subject = '(no subject)'
        filtered_emails.append(subject)


# create a frame for the search bar and button
search_frame = tk.Frame(root)
search_frame.pack(side=tk.TOP, fill=tk.X)

# create an entry widget for the search bar
search_entry = tk.Entry(search_frame, width=50)
search_entry.pack(side=tk.LEFT, padx=10)

# create a search button
search_button = tk.Button(search_frame, text="Search", command=search_email)
search_button.pack(side=tk.LEFT, padx=10)

# create a compose email button
compose_button = tk.Button(root, text="Compose", command=lambda: exec(open("email.py").read()))
compose_button.pack(side=tk.TOP, padx=10, pady=10, anchor="nw")

# create a sign-out button
sign_out_button = tk.Button(root, text="Sign Out", command=sign_out)
sign_out_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="se")

# create a listbox to display the emails
listbox = tk.Listbox(root, width=80)
listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

print("Filtered emails:", filtered_emails)
# add the filtered emails to the listbox
for email in filtered_emails:
    print("Adding email to listbox:", email)
    listbox.insert(tk.END, email)


# start the GUI main loop
root.mainloop()
