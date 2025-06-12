import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# --- Setup ---
SHEET_NAME = "patient_records"
CREDS_PATH = "config/creds.json"

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# --- Load client ---
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDS_PATH, scope)
client = gspread.authorize(creds)

# --- Access sheet ---
try:
    sheet = client.open(SHEET_NAME).sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)

    print("✅ Sheet Accessed Successfully.")
    print("🔍 Raw Data from Sheet:", data)
    print("📋 DataFrame Columns:", df.columns.tolist())
    print("📄 DataFrame Preview:")
    print(df.head())

except Exception as e:
    print("❌ Error:", e)
