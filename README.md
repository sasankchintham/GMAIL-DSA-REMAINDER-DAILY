Overview

# GMAIL-DSA-REMAINDER-DAILY

## 📌 Overview
GMAIL-DSA-REMAINDER-DAILY is an automated system that sends a daily email reminder with a DSA (Data Structures & Algorithms) topic to help users stay consistent in their DSA learning journey. The topics are stored in a Google Sheet, and the script fetches one topic per day and emails it to the user.

## ⚡ Features
- Automates daily email reminders with DSA topics
- Fetches topics from a Google Sheet
- Uses Gmail SMTP for email sending
- Can be scheduled using a cron job (Linux) or Task Scheduler (Windows)

## 🚀 Technologies Used
- Python
- Google Sheets API (gspread)
- Gmail SMTP
- Pandas

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```bash
   git clone https://github.com/sasankchintham/GMAIL-DSA-REMAINDER-DAILY.git
   cd GMAIL-DSA-REMAINDER-DAILY
```

### 2️⃣ Create and Activate Virtual Environment (Optional but Recommended)
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 3️⃣ Install Required Dependencies
```bash
   pip install -r requirements.txt
```

### 4️⃣ Set Up Google Sheets API
- Create a Google Cloud Project and enable the Sheets API
- Generate credentials and download the JSON file
- Move the JSON file to the project directory and update `.gitignore` to exclude it

### 5️⃣ Configure Environment Variables
Create a `.env` file and add the following details:
```
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
SHEET_NAME=DSA-Topics
```

### 6️⃣ Run the Script Manually
```bash
   python DSA-Daily.py
```

## ⏰ Automate Execution
- **Linux (cron job):** Add this line to `crontab -e`
```bash
0 9 * * * /usr/bin/python3 /path/to/DSA-Daily.py
```
(This runs the script every day at 9 AM)

- **Windows (Task Scheduler):**
  - Open Task Scheduler → Create Basic Task
  - Set the trigger to daily at your preferred time
  - Set the action to start a program → Browse to `python.exe` and add `DSA-Daily.py` as an argument

## 📧 How It Works
1. The script connects to the Google Sheet and fetches the next DSA topic.
2. It formats the topic and generates an email.
3. Sends the email to the specified recipients using Gmail SMTP.
4. Marks the topic as sent and moves to the next one in the next execution.

Feel Free To Connect with me.




