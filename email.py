import tkinter as tk
from tkinter import filedialog, messagebox


class Email:
    def __init__(self, sender, recipient, subject, message, attachment=None):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.message = message
        self.attachment = attachment
    def format_email(self):
        email_str = f"From: {self.sender}\nTo: {self.recipient}\nSubject: {self.subject}\n\n{self.message}"
        if self.attachment:
            email_str += f"\n\nAttachment: {self.attachment}"
        return email_str
    def attach_file(self):
        file_path = filedialog.askopenfilename(title="Select file to attach")
        if file_path:
            self.attachment = file_path
            messagebox.showinfo("Attachment", "File attached successfully.")
        else:
            messagebox.showwarning("Attachment", "No file selected.")
def send_email():
    global email
    sender = sender_entry.get()
    recipient = recipient_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end").strip()
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
    app.destroy()

def attach_file():
    global email
    email.attach_file()


app = tk.Tk()
app.title("Email Client")
app.geometry("800x600")

sender_label = tk.Label(app, text="From:")
recipient_label = tk.Label(app, text="To:")
subject_label = tk.Label(app, text="Subject:")
message_label = tk.Label(app, text="Message:")

sender_entry = tk.Entry(app, width=30)
recipient_entry = tk.Entry(app, width=30)
subject_entry = tk.Entry(app, width=30)
message_text = tk.Text(app, height=10)

send_button = tk.Button(app, text="Send Email", command=send_email)
attach_button = tk.Button(app, text="Attach File", command=attach_file)

sender_label.grid(row=0, column=0)
sender_entry.grid(row=0, column=1)
recipient_label.grid(row=1, column=0)
recipient_entry.grid(row=1, column=1)
subject_label.grid(row=2, column=0)
subject_entry.grid(row=2, column=1)
message_label.grid(row=3, column=0)
message_text.grid(row=3, column=1)
send_button.grid(row=4, column=1, pady=(10, 0))
attach_button.grid(row=4, column=0)

email = Email(None, None, None, None, None)

app.mainloop()
