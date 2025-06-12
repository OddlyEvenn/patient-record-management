# modules/auth.py

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_gsheet_client(creds_file_path: str):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file",
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file_path, scope)
    client = gspread.authorize(creds)
    return client
