# modules/add_patient.py

import pandas as pd
from modules.utils import is_valid_email, is_duplicate
from modules.email_confirmation import send_confirmation_email
from modules.google_sheets import write_data

def add_patient(client, sheet_name, df, patient_data):
    patient_id = patient_data['Patient Id']
    
    if is_duplicate(df, patient_id):
        return False, "Patient ID already exists."

    if not is_valid_email(patient_data['Email-id']):
        return False, "Invalid email address."

    df = pd.concat([df, pd.DataFrame([patient_data])], ignore_index=True)
    write_data(client, sheet_name, df)

    send_confirmation_email(patient_data['Email-id'], patient_data['Name'], patient_id, patient_data['Fees'])
    
    return True, "Patient added successfully."
