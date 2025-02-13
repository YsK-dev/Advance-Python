# Automated Email Sender with Gemini AI Integration

This project demonstrates how to automate the process of generating and sending professional emails using Python, the Gemini AI model, and an SMTP server. The script allows you to generate email content based on a given topic and recipient name, and then send the email using an SMTP server.

---

## Features

- **Gemini AI Integration**: Uses the Gemini AI model to generate professional email content based on user input.
- **SMTP Email Sending**: Sends the generated email using an SMTP server.
- **Customizable**: Easily configure the SMTP server, login credentials, and email addresses.
- **User-Friendly**: Takes user input for the recipient's name and email topic.

---

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x**: The script is written in Python. Download and install Python from [python.org](https://www.python.org/).
2. **Gemini API Key**: Obtain an API key from [Google's Gemini AI](https://ai.google/).
3. **SMTP Credentials**: Ensure you have access to an SMTP server (e.g., Brevo, Gmail, etc.) and the necessary login credentials.
4. **Required Python Libraries**:
   - `smtplib`: Built-in Python library for sending emails.
   - `email.mime.text`: Built-in Python library for creating email messages.
   - `google.generativeai`: Python library for interacting with the Gemini AI model.

   Install the required libraries using pip:
   ```bash
   pip install google-generativeai
   ```

---

## Configuration

1. **SMTP Configuration**:
   - Update the following variables in the script with your SMTP server details:
     ```python
     SMTP_SERVER = "smtp-relay.brevo.com"  # Replace with your SMTP server
     SMTP_PORT = 587  # Replace with your SMTP port
     SMTP_LOGIN = "your_smtp_login"  # Replace with your SMTP login
     SMTP_PASSWORD = "your_smtp_password"  # Replace with your SMTP password
     EMAIL_SENDER = "your_email@example.com"  # Replace with your email address
     EMAIL_RECEIVER = "recipient_email@example.com"  # Replace with the recipient's email address
     ```

2. **Gemini API Key**:
   - Replace the placeholder with your Gemini API key:
     ```python
     GEMINI_API_KEY = "your_gemini_api_key"  # Replace with your Gemini API key
     ```

---

## How It Works

1. **User Input**:
   - The script prompts the user to enter the recipient's name and the email topic.

2. **Email Content Generation**:
   - The script uses the Gemini AI model to generate professional email content based on the provided topic and recipient name.

3. **Email Sending**:
   - The script sends the generated email using the configured SMTP server.

---

## Usage

1. Clone or download the repository.
2. Open the script in a text editor and update the configuration variables (SMTP and Gemini API key).
3. Run the script:
   ```bash
   python automated_email_sender.py
   ```
4. Follow the prompts to enter the recipient's name and email topic.
5. The script will generate the email content and send it to the recipient.

---

## Example

### Input:
```
Enter to who we write the E-mail: Umut sezer
Enter the topic or project requirement: Project Deadline Extension
```

### Output:
```
Generating email content...
Generated Email Content:
 Dear Umut Sezer,

I hope this email finds you well. I am writing to inform you about the need for a deadline extension for the ongoing project. Due to unforeseen circumstances, we require an additional week to complete the project requirements.

Please let me know if this is acceptable.

Best regards,
Yusuf Sertkaya

Email sent successfully!
```

---

## Notes

- Ensure your SMTP server allows sending emails from the configured email address.
- If you encounter authentication issues, double-check your SMTP login credentials.
- The Gemini API key must be valid and have sufficient permissions to generate content.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Author

- **Yusuf Sertkaya**
- GitHub: [Ysk-dev](https://github.com/Ysk-dev)
- Email: srtkyyusuf@gmail.com

---

Enjoy automating your emails with Gemini AI! 🚀