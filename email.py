import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class Email:
    def __init__(self, sender, recipient, subject, message, attachment=None):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.attachment = attachment 
        
    def format_email(self):
        email_str = f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\nMessage: {self.message}"
        if self.attachment:
            email_str += f"\n{self.attachment}"
        return email_str
    
    def attach_file(self):
        file_path = filedialog.askopenfilename(title="Select file to attach")
        if file_path:
            self.attachment = file_path
            messagebox.showinfo("Attachment", "File attached successfully.")
        else:
            messagebox.showwarning("Attachment", "No file selected.")


def send_email():
    global email, sender_entry, recipient_entry, subject_entry, message_text, Email
    sender = sender_entry.get()
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end").strip()
    if len(message) >= 1000:
        messagebox.showwarning("Error", "Message exceeds 1000 characters.")
        return
    if not sender or not recipient or not subject or not message:
        messagebox.showwarning("Error", "Please fill in all fields.")
        return
    email = Email(sender, recipient, subject, message, email.attachment)

    if not email.attachment:
        email.attachment = None

    formatted_email = email.format_email()
    with open("emails.txt", "a") as file:
        file.write(formatted_email + "\n\n")
    messagebox.showinfo("Success", "Email sent successfully.")
    root.destroy()

def attach_file():
    global email
    email.attach_file()


def limit_characters(text):
    if len(text) > 1000:
        message_text.delete("1000.0", "end")
        message_text.insert("end", text[:1000])
    return True


root = tk.Tk()
root.title("Email Client")
root.geometry("800x600")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.configure(background='#C6DEFF')


# Calculate x and y coordinates for the Tk root window
x = int((screen_width / 2) - (1000 / 2))
y = int((screen_height / 2) - (1000 / 2))

root.geometry(f"800x600+{x}+{y}")

sender_label = tk.Label(root, text="From:", bg='#C6DEFF')
recipient_label = tk.Label(root, text="To:", bg='#C6DEFF')
subject_label = tk.Label(root, text="Subject:", bg='#C6DEFF')
message_label = tk.Label(root, text="Message:", bg='#C6DEFF')

sender_entry = tk.Entry(root, width=30)
recipient_entry = tk.Entry(root, width=30)
subject_entry = tk.Entry(root, width=30)
message_text = tk.Text(root, height=30, borderwidth=2, relief=tk.SOLID)

send_button = tk.Button(root, text="Send Email", command=send_email)
attach_button = tk.Button(root, text="Attach File", command=attach_file)

sender_label.grid(row=0, column=0)
sender_entry.grid(row=0, column=1)
recipient_label.grid(row=1, column=0)
recipient_entry.grid(row=1, column=1)
subject_label.grid(row=2, column=0)
subject_entry.grid(row=2, column=1)
message_label.grid(row=3, column=0)
message_text.grid(row=3, column=1)
send_button.grid(row=4, column=2, pady=(10, 0))
attach_button.grid(row=4, column=0, padx=(10, 0))

email = Email(None, None, None, None, None)

root.mainloop()
