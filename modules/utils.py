# modules/utils.py
# from modules.google_sheets import write_data

def is_valid_email(email: str) -> bool:
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def is_duplicate(df, patient_id: str) -> bool:
    return patient_id in df['Patient Id'].values

def generate_patient_id(df) -> str:
    import uuid
    new_id = str(uuid.uuid4())[:8]
    while new_id in df['Patient Id'].values:
        new_id = str(uuid.uuid4())[:8]
    return new_id

# def edit_patient(client, sheet_name, df, patient_id, updated_data):
#     # Normalize for case and whitespace
#     patient_id = patient_id.strip().upper()
#     df['Patient Id'] = df['Patient Id'].astype(str).str.strip().str.upper()

#     index = df[df['Patient Id'] == patient_id].index
#     if index.empty:
#         return False, "Patient ID not found."

#     for key in updated_data:
#         df.at[index[0], key] = updated_data[key]

#     write_data(client, sheet_name, df)
#     return True, "Patient details updated successfully."