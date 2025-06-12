from modules.google_sheets import write_data

def edit_patient(client, sheet_name, df, patient_id, updated_data):
    # Normalize for case and whitespace
    patient_id = patient_id.strip().upper()
    df['Patient Id'] = df['Patient Id'].astype(str).str.strip().str.upper()

    index = df[df['Patient Id'] == patient_id].index
    if index.empty:
        return False, "Patient ID not found."

    for key in updated_data:
        value = updated_data[key]

    # Auto-convert empty string to NaN (optional) or just string
    if df[key].dtype == 'int64' or df[key].dtype == 'float64':
        try:
            value = float(value) if value else 0.0
        except:
            value = 0.0

    df.at[index[0], key] = value

    # for key in updated_data:
    #     df.at[index[0], key] = updated_data[key]

    write_data(client, sheet_name, df)
    return True, "Patient details updated successfully."
