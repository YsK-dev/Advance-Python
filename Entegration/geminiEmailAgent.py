import smtplib
from email.mime.text import MIMEText
import google.generativeai as genai
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Configuration
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_LOGIN = "85a5cd001@smtp-brevo.com"   # Replace with your SMTP login
SMTP_PASSWORD = "your-smtp-key"  # Replace with your SMTP password
EMAIL_SENDER = "srtkyyusuf@gmail.com"
EMAIL_RECEIVER = "satılıkmışEmail"

# Set up your Gemini API key
GEMINI_API_KEY = "your-api-key"  # Replace with your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Function to generate email content using Gemini
def generate_email_content(topic, name):
    prompt = f"Write a professional email about the following topic: {topic}. Include project requirements, deadlines, and any other relevant details. to {name} YOUR NAME İS yusuf sertkaya"

    try:
        # Generate content using Gemini
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error: Failed to generate email content. {e}")
        return None

# Function to send email
def send_email(subject, body):
    # Create the email message
    message = MIMEText(body, "plain", "utf-8")
    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    # Send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as s:
            s.starttls()  # Start TLS encryption
            s.login(SMTP_LOGIN, SMTP_PASSWORD)  # Log in to the SMTP server
            s.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message.as_string())  # Send the email
        print("Email sent successfully!")
        messagebox.showinfo("Success", "Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your login credentials.")
        messagebox.showerror("Error", "Authentication failed. Check your login credentials.")
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email. {e}")
        messagebox.showerror("Error", f"Unable to send email. {e}")

# Function to handle the "Generate Email" button click
def on_generate_email():
    name = name_entry.get()
    topic = topic_entry.get()

    if not name or not topic:
        messagebox.showwarning("Input Error", "Please enter both the recipient's name and the topic.")
        return

    # Generate email content using Gemini
    email_body = generate_email_content(topic, name)

    if email_body:
        email_text.delete(1.0, tk.END)  # Clear the text area
        email_text.insert(tk.END, email_body)  # Insert the generated email content

        # Automatically set the subject in the subject field
        subject_entry.delete(0, tk.END)  # Clear the subject field
        subject_entry.insert(0, f"Project Requirements: {topic} to {name}")  # Set the subject
    else:
        messagebox.showerror("Error", "Failed to generate email content. Please check your Gemini API key and configuration.")

# Function to handle the "Send Email" button click
def on_send_email():
    subject = subject_entry.get()
    body = email_text.get(1.0, tk.END)

    if not subject or not body.strip():
        messagebox.showwarning("Input Error", "Please ensure the subject and email body are filled.")
        return

    # Send the email
    send_email(subject, body)

# Create the main window
root = tk.Tk()
root.title("Email Generator and Sender")

# Create and place widgets
tk.Label(root, text="Recipient's Name:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Email Topic:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
topic_entry = tk.Entry(root, width=50)
topic_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="🪄Generate Email", command=on_generate_email)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Email Subject:").grid(row=3, column=0, padx=10, pady=10, sticky="e")
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="Email Body:").grid(row=4, column=0, padx=10, pady=10, sticky="ne")
email_text = scrolledtext.ScrolledText(root, width=60, height=15)
email_text.grid(row=4, column=1, padx=10, pady=10)

send_button = tk.Button(root, text="📩Send Email", command=on_send_email)
send_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()