import gspread
from google.oauth2.service_account import Credentials

SCOPE = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
CREDS_FILE = "D:/DSA-daily/email-dsa-daily-eb3f9d3425b9.json"

creds = Credentials.from_service_account_file(CREDS_FILE, scopes=SCOPE)
client = gspread.authorize(creds)

spreadsheet = client.open("DSA-Topics")  # Replace with your sheet name
print("✅ Success! Connected to:", spreadsheet.title)
