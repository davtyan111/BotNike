# config.py

# --- MYSQL ---
MYSQL_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'secret',
    'database': 'photo_bot_db',
    'port': 3306
}

# --- GOOGLE DRIVE ---
GOOGLE_DRIVE_FOLDER_ID = '1DfhhoiskfpW4-o5Q3OWxeaEU2VyxIb1O'
GOOGLE_CREDENTIALS_FILE = 'drive.json' 

# --- TELEGRAM ---
BOT_TOKEN = '6653187242:AAGNpZlddjRf9IPc3fOXcHKQ7GINBptBgjM'
URL = f'https://api.telegram.org/bot{BOT_TOKEN}'
