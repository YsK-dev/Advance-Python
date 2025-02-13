import smtplib
from email.mime.text import MIMEText

# SMTP Configuration
PORT = 587
SMTP_SERVER = "smtp-relay.brevo.com"
login = "85a5cd001@smtp-brevo.com"  # Replace with your SMTP login
password = "G5gdz9mjtkMJx46R"  # Replace with your SMTP password

# Email Details
Email_sender = "srtkyyusuf@gmail.com"
Email_receiver = "221805081@stu.adu.edu.tr"

# Email Content
text = """
SATILIKMIŞ C^İLE UNİTY YAP OYUN KONUSUDA GTA 6 GİBİ BİŞİ OLSUN hemen başla demo istiyorum pazartesi
"""

# Create the Email Message
message = MIMEText(text, "plain", "utf-8")  # Specify encoding
message["Subject"] = "Mustafa Samsung Başarıcı"  # Ensure subject is properly formatted
message["From"] = Email_sender
message["To"] = Email_receiver

# Send the Email
try:
    with smtplib.SMTP(SMTP_SERVER, PORT) as s:
        s.starttls()  # Start TLS encryption
        s.login(login, password)  # Log in to the SMTP server
        s.sendmail(Email_sender, Email_receiver, message.as_string())  # Send the email
    print("E-Mail sent successfully!")
except smtplib.SMTPAuthenticationError:
    print("Error: Authentication failed. Check your login credentials.")
except smtplib.SMTPException as e:
    print(f"Error: Unable to send email. {e}")