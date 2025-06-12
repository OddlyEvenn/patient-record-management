# modules/delete_patient.py

from modules.google_sheets import write_data

def delete_patient(client, sheet_name, df, patient_id):
    # Normalize input
    patient_id = str(patient_id).strip().upper()
    df['Patient Id'] = df['Patient Id'].astype(str).str.strip().str.upper()

    initial_len = len(df)
    df = df[df['Patient Id'] != patient_id]

    if len(df) == initial_len:
        return False, "Patient ID not found."

    write_data(client, sheet_name, df)
    return True, "Patient deleted successfully."
