# main.py

import tkinter as tk
from gui import PatientGUI

from modules.auth import get_gsheet_client
from modules.google_sheets import get_sheet_data
from modules.add_patient import add_patient
from modules.edit_patient import edit_patient
from modules.delete_patient import delete_patient
from modules.display_patient import get_patient_by_id
from modules.export_data import export_to_csv
from modules.report_summary import get_summary

# --- CONFIG ---
SHEET_NAME = "patient_records"
CREDENTIALS_PATH = "config/creds.json"

class App:
    def __init__(self, root):
        self.client = get_gsheet_client(CREDENTIALS_PATH)
        self.df = get_sheet_data(self.client, SHEET_NAME)
        print("ACTUAL COLUMNS LOADED FROM SHEET:", self.df.columns.tolist())

        self.gui = PatientGUI(root, {
            "add": self.add_patient,
            "edit": self.edit_patient,
            "delete": self.delete_patient,
            "display": self.display_patient,
            "export": self.export_data,
            "summary": self.show_summary
        }, logo_path="assets/logo.png")

    def refresh_df(self):
        self.df = get_sheet_data(self.client, SHEET_NAME)

    def add_patient(self):
        data = self.gui.get_form_data()
        success, message = add_patient(self.client, SHEET_NAME, self.df, data)
        self.gui.show_message(message, success)
        if success:
            self.refresh_df()

    def edit_patient(self):
        data = self.gui.get_form_data()
        patient_id = data['Patient Id']
        success, message = edit_patient(self.client, SHEET_NAME, self.df, patient_id, data)
        self.gui.show_message(message, success)
        if success:
            self.refresh_df()

    def delete_patient(self):
        data = self.gui.get_form_data()
        patient_id = data['Patient Id']
        success, message = delete_patient(self.client, SHEET_NAME, self.df, patient_id)
        self.gui.show_message(message, success)
        if success:
            self.refresh_df()

    def display_patient(self):
        data = self.gui.get_form_data()
        record = get_patient_by_id(self.df, data['Patient Id'])
        if record:
            self.gui.set_form_data(record)
            self.gui.show_message("Patient details loaded.", True)
        else:
            self.gui.show_message("Patient ID not found.", False)

    def export_data(self):
        success, message = export_to_csv(self.df)
        self.gui.show_message(message, success)

    def show_summary(self):
        summary = get_summary(self.df)
        msg = f"📋 Total Patients: {summary['total_patients']}\n💰 Total Revenue: ₹{summary['total_revenue']}\n\nRecent Registrations:\n"
        for _, row in summary['recent'].iterrows():
            msg += f"- {row['Name']} (ID: {row['Patient Id']})\n"
        self.gui.show_message(msg)
        
    # pid = self.gui.get_form_data()['Patient Id'].strip()
    # if not pid:
    #     self.gui.show_message("Please enter a valid Patient ID.", success=False)
    #     return

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
