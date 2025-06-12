# modules/google_sheets.py

import pandas as pd

def get_sheet_data(client, sheet_name: str):
    sheet = client.open(sheet_name).sheet1
    data = sheet.get_all_records()
    return pd.DataFrame(data)

def write_data(client, sheet_name: str, df: pd.DataFrame):
    sheet = client.open(sheet_name).sheet1
    sheet.clear()
    sheet.update([df.columns.values.tolist()] + df.values.tolist())
