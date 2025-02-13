import smtplib
from email.mime.text import MIMEText  # bu otamatik mail için
import google.generativeai as genai

# Configuration
SMTP_SERVER = "smtp-relay.brevo.com"
SMTP_PORT = 587
SMTP_LOGIN = "stmplogin"  # Replace with your SMTP login
SMTP_PASSWORD = "yourpassword"  # Replace with your SMTP password
EMAIL_SENDER = "yourmail"
EMAIL_RECEIVER = "recivermail"

# Set up your Gemini API key
GEMINI_API_KEY = "yourkey"  # Replace with your Gemini API key
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
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Check your login credentials.")
    except smtplib.SMTPException as e:
        print(f"Error: Unable to send email. {e}")

# Main function
def main():
    name = input("Enter to who we write the E-mail: ")
    # Get user input for the topic
    topic = input("Enter the topic or project requirement: ")

    # Generate email content using Gemini
    print("Generating email content...")
    email_body = generate_email_content(topic, name)

    if email_body:
        print("Generated Email Content:\n", email_body)

        # Send the email
        email_subject = f"Project Requirements: {topic} to {name}"
        send_email(email_subject, email_body)
    else:
        print("Failed to generate email content. Please check your Gemini API key and configuration.")

# Run the script
if __name__ == "__main__":
    main()