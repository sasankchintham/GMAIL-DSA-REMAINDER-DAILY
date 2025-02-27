import smtplib
import gspread
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets API Setup
SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "email-dsa-daily-eb3f9d3425b9.json"  # Update with your credentials file
SPREADSHEET_NAME = "DSA-Topics"  # Update with your sheet name

# Gmail Setup
SENDER_EMAIL = "pepsisasank32@gmail.com"  # Update with your email
SENDER_PASSWORD = "ajhx vzcs ujwm ocpl"  # Use an App Password (not your real password)
RECEIVER_EMAIL = "venkateshmandala116@gmail.com"  # Email where you want to receive the topics

# Connect to Google Sheets
def get_google_sheet():
    creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_FILE, SCOPE)
    client = gspread.authorize(creds)
    return client.open(SPREADSHEET_NAME).sheet1

# Fetch the next unsent topic
def get_next_topic(sheet):
    data = sheet.get_all_records()
    for index, row in enumerate(data, start=2):  # Start from row 2 (after headers)
        if row["Status"] == "":
            return index, row["Topic"], row["Subtopic"], row["Link"]
    return None, None, None, None  # No topics left

# Send Email
def send_email(topic, Subtopic, link):
    subject = f"Today's DSA Topic: {Subtopic}"
    body = f"Hi,\n\nToday's topic is **{topic} - {Subtopic}**.\nHere is the link to learn more: {link}\n\nHappy Learning! 🚀"
    
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())

# Mark topic as "Sent" in Google Sheets
def mark_topic_as_sent(sheet, row_number):
    sheet.update_cell(row_number, 4, "Sent")  # Column D (Status)

# Main function
def main():
    sheet = get_google_sheet()
    row_number, topic, Subtopic, link = get_next_topic(sheet)

    if topic:
        send_email(topic, Subtopic, link)
        mark_topic_as_sent(sheet, row_number)
        print(f"Email sent for {topic} - {Subtopic}")
    else:
        print("All topics have been sent!")

if __name__ == "__main__":
    main()
