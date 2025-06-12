# modules/display_patient.py

def get_patient_by_id(df, patient_id):
    # Normalize input
    patient_id = str(patient_id).strip().upper()
    df['Patient Id'] = df['Patient Id'].astype(str).str.strip().str.upper()

    record = df[df['Patient Id'] == patient_id]
    if record.empty:
        return None
    return record.to_dict(orient='records')[0]

def get_patient_by_name(df, name):
    # Optional: if you ever use this
    name = name.strip().lower()
    df['Name'] = df['Name'].astype(str).str.strip().str.lower()

    record = df[df['Name'] == name]
    if record.empty:
        return None
    return record.to_dict(orient='records')
