import tkinter as tk
import os

# create a GUI window
root = tk.Tk()
root.title("My Mailbox")
root.geometry("1000x1000")

# read the login information from a text file
with open("login.txt", "r") as file:
    login_info = file.read().splitlines()

# read the emails from a text file
with open("emails.txt", "r") as file:
    emails = file.read().splitlines()

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

# filter the emails that have the "to" field equal to the current login information
filtered_emails = []
for email in emails:
    fields = email.split(",")
    if len(fields) >= 2 and fields[1] == login_info[0]:
        filtered_emails.append(email)

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

# create a sign out button
sign_out_button = tk.Button(root, text="Sign Out", command=sign_out)
sign_out_button.pack(side=tk.BOTTOM, padx=10, pady=10, anchor="se")


# create a listbox to display the emails
listbox = tk.Listbox(root, width=80)
listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# add the filtered emails to the listbox
for email in filtered_emails:
    listbox.insert(tk.END, email)


# start the GUI main loop
root.mainloop()
